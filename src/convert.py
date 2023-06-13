# https://www.kaggle.com/datasets/awsaf49/food-recognition-2022-dataset

import os
import supervisely as sly
from supervisely.io.fs import get_file_name_with_ext, file_exists
from supervisely.io.json import load_json_file
from collections import defaultdict
from tqdm import tqdm


dataset_path = "/Users/almaz/Downloads/FoodRecognition"
download_bbox = False

batch_size = 30
images_folder_name = "images"
ann_json_name = "annotations.json"


def convert_and_upload_supervisely_project(api, workspace_id, project_name):
    def _create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        ann_data = image_name_to_ann_data[get_file_name_with_ext(image_path)]
        for curr_ann_data in ann_data:
            category_id = curr_ann_data[0]
            polygons_coords = curr_ann_data[1]
            for coords in polygons_coords:
                exterior = []
                for i in range(0, len(coords), 2):
                    exterior.append([int(coords[i + 1]), int(coords[i])])
                if len(exterior) < 3:
                    continue
                poligon = sly.Polygon(exterior)
                label_poly = sly.Label(poligon, idx_to_obj_class[category_id][0])
                labels.append(label_poly)

            if download_bbox:
                bbox_coord = curr_ann_data[2]
                rectangle = sly.Rectangle(
                    top=int(bbox_coord[0]),
                    left=int(bbox_coord[1]),
                    bottom=int(bbox_coord[0] + bbox_coord[2]),
                    right=int(bbox_coord[1] + bbox_coord[3]),
                )
                label_rectangle = sly.Label(rectangle, idx_to_obj_class[category_id][1])
                labels.append(label_rectangle)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


    project_info = api.project.create(workspace_id, project_name)
    meta = sly.ProjectMeta()

    ds_folders = os.listdir(dataset_path)

    idx_to_obj_class = {}

    for sub_folder in ds_folders:
        if sub_folder == ".DS_Store":
            continue
        ds_name = sub_folder.split("_")[1]
        dataset = api.dataset.create(project_info.id, ds_name, change_name_if_conflict=True)
        image_id_to_name = {}
        image_name_to_ann_data = defaultdict(list)

        images_path = os.path.join(dataset_path, sub_folder, images_folder_name)
        images_names = os.listdir(images_path)
        ann_path = os.path.join(dataset_path, sub_folder, ann_json_name)
        if file_exists(ann_path):
            ann = load_json_file(ann_path)
            for curr_category in ann["categories"]:
                if idx_to_obj_class.get(curr_category["id"]) is None:
                    obj_class_poly = sly.ObjClass(curr_category["name"], sly.Polygon)
                    meta = meta.add_obj_class(obj_class_poly)
                    obj_class_rect = sly.ObjClass(curr_category["name"] + "_bbox", sly.Rectangle)
                    if download_bbox:
                        meta = meta.add_obj_class(obj_class_rect)
                    idx_to_obj_class[curr_category["id"]] = (obj_class_poly, obj_class_rect)
            api.project.update_meta(project_info.id, meta.to_json())

            for curr_image_info in ann["images"]:
                image_id_to_name[curr_image_info["id"]] = curr_image_info["file_name"]

            for curr_ann_data in ann["annotations"]:
                image_id = curr_ann_data["image_id"]
                image_name_to_ann_data[image_id_to_name[image_id]].append(
                    [curr_ann_data["category_id"], curr_ann_data["segmentation"], curr_ann_data["bbox"]]
                )

        progress = tqdm(desc=f"Create dataset {ds_name}", total=len(images_names))

        for img_names_batch in sly.batched(images_names, batch_size=batch_size):
            images_pathes_batch = [
                os.path.join(images_path, image_path) for image_path in img_names_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            if file_exists(ann_path):
                anns_batch = [_create_ann(image_path) for image_path in images_pathes_batch]
                api.annotation.upload_anns(img_ids, anns_batch)

            progress.update(len(img_names_batch))

    return project_info