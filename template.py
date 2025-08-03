import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s')


project_name = "Containerized Bank Customer Churn Prediction"


list_of_files= [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",     
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "DockerFile",
    "requirments.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py",
    "exp.py"
]


for files in list_of_files:
    files = Path(files) #işletim sistemine göre yolda gereken ayarları yaptığı için tercih edilir
    filedir,filename = os.path.split(files)

    if filedir != "":
        os.makedirs(filedir,exist_ok = True)
        print(f"klasör oluşturuluyor >>>>>{filedir}//{filename}")

    if (not os.path.exists(files)) or (os.path.getsize(files)==0):
        with open(files, "w") as f:
            pass 
            logging.info(f"boş dosya oluşturuluyor:{files}")

    else:
        print(f" bu dosya zaten mevcut!!")