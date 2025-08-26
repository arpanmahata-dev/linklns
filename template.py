import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s : %(levelname)s]: %(message)s')

while True:
    project_name = input("Project Name")

    if project_name != "":
        break
    
logging.info(f"creating Project :-> {project_name}")

#file tree
pack_tree = [
    ".github/workflows/.gitkeep"
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    f"init_setup.sh",
    "requirements_dev.txt",
    "requirements.txt",
    "setup.py",
    "setup.cfg",
    "tox.ini",
    "pyproject.toml",
]

for filepath in pack_tree:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"created directory at;-> {filedir} for file {filename}")
    if (not os.path.exists(filename)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"created file :-> {filename} at path: {filepath}")
    else:
        logging.info(f"file already exists :-> {filename} at path: {filepath}")

#init Files