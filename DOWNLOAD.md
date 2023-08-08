Dataset **Food Recognition 2022** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/g/x/8C/uFOBz66enoXsEMPzMcLCPLbr13xU07IOTI9nHHP0qumJalbd5xOhq1WD9IwMlNneg8RDqN9i53ke58w7JdAsk2fRelMmpkDeFhcd7cBWb53z3KayMNLqJc469r6W.tar)

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

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/awsaf49/food-recognition-2022-dataset/download?datasetVersionNumber=1)