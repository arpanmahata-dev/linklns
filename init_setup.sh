echo [$(date)]: "START"
echo [$(date)]: "Create conda env using Python 3.8"
conda create --prefix ./env python=3.8 -y

echo [$(date)]: "Activate conda env"
source activate ./env

echo [$(date)]: "Install dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"