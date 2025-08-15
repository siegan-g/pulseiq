# Python API

- The backbones of the project
- Implemented in Fast API 

- Using a Ports and Adapters/ Component and Strategy Pattern so its easier to mock tests and scale each service layer into seperate instances e.g. containers

## 
- Be sure to use a retry pattern for self healing on request handling
- 


## Setting up the developer environment

- Create a virtual environment
```
python -m venv venv
```

- Activate the virtual environment with the below
```
source /venv/bin/activate
```

- or on Windows

```
./venv/bin/activate
```
- if you are on Arch Linux and are having environment issues install the package `python-virtualenv` and create the venv with `virtualenv venv`


- Install dependencies with the below:
```
pip install -r requirements.txt
```