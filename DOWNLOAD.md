Dataset **Food Recognition 2022** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/w/N/fw/tNoPTiEUnD3NMug1oKmMvGAk5MtUkE4Gfn2HT1mxTVirTauBxbeRTaDILAw0wlk3NUMuRyCUJKcNQ7NVwn8fPaIL5vrznPv6fuAcKJp31q9I5oJtgy5c3zMLB8eL.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Food Recognition 2022', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/awsaf49/food-recognition-2022-dataset/download?datasetVersionNumber=1).