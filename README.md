# this is my end to end project

# first initialize git 

"""
git init
"""

"""
git add abc.txt

git add .
"""

"""
git commit -m "this is my first commit"
"""

"""
git pull
"""
# another way you can mention -e . in your requirement file and you can run

```
pip install -r requirements.txt
```

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### local cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/shelkekunal90/fsdsmendtoend.mlflow 
MLFLOW_TRACKING_USERNAME=shelkekunal90 
MLFLOW_TRACKING_PASSWORD=654cde79efc37a8d0050cdfa4da919e4664891e4 
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/shelkekunal90/fsdsmendtoend.mlflow

export MLFLOW_TRACKING_USERNAME=shelkekunal90

export MLFLOW_TRACKING_PASSWORD=654cde79efc37a8d0050cdfa4da919e4664891e4

```


### DVC cmd
- dvc init
- dvc repro
- dvc dag

