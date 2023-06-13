Dataset **Food Recognition 2022** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/g/x/8C/uFOBz66enoXsEMPzMcLCPLbr13xU07IOTI9nHHP0qumJalbd5xOhq1WD9IwMlNneg8RDqN9i53ke58w7JdAsk2fRelMmpkDeFhcd7cBWb53z3KayMNLqJc469r6W.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Food Recognition 2022', dst_path='~/dtools/datasets/Food Recognition 2022.tar')
```
The data in original format can be 🔗[downloaded here.](https://www.kaggle.com/datasets/awsaf49/food-recognition-2022-dataset/download?datasetVersionNumber=1)