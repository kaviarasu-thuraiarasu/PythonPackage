from genericpath import exists
import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format="[%(asctime)s : %(levelname)s-]:%(message)s")

while True:
    project_name = input("Enter the project Name:")
    if project_name!="":
        break

logging.info(f"creating project by name: {project_name}")

# creating Folder structure using python code:

list_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    "test/__init__.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
]

for filePath in list_files:
    filePath = Path(filePath)
    file_dir, file_name = os.path.split(filePath)
    if(file_dir!=""):
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"creating a directory at : {file_dir} for file :{file_name}")
    
    if((not os.path.exists(filePath)) or (os.path.getsize(filePath))):
        with open(filePath,"w") as f: # This line will create the file if not available
            pass

        logging.info(f"File create in the {filePath}")            
    else:
        logging.info(f"File path {filePath} already exist")

