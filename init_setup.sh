echo [$(date)]: "START"


echo [$(date)]: "creating env with python 3.8 version" 


conda create --prefix ./env python=3.8 -y


echo [$(date)]: "activating the environment" 

source activate ./env
#some times in wont work directly then type it bash terminal
echo [$(date)]: "installing the dev requirements" 

pip install -r requirements.txt

echo [$(date)]: "END" 

#only works with linux (bash)
#bash init_setup.sh