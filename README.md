# Basic API with Flask and Python
## API Creation using Flask

Basic opearations of Create(POST), Retrieve(GET), Update(PUT), Delete(DELETE)


## Setting up the environment
OS: Ubuntu
JupyterLab, Python3, Sqlite, Flask

Type the following commands in the terminal:

```sh
mkdir api
cd api
python -m venv .env
source .env/bin/activate
```

This will create a project folder and a virtual environment for dependecies seclusion

Install the following libraries

```sh
pip install flask
pip install flask-sqlalchemy
pip freeze > requirements.txt
```
Create the following two files
```sh
touch application.py
touch db_config.py
```

These files are present in the repository with proper commenting

Create the following environmental variables in the TERMINAL:

```sh
export FLASK_APP = application.py
export FLASK_ENV = development
```
These environment variables are lost as soon as the terminal is exited. There might be a need to declare them again once the project is to be run again.

To run the server
```sh
flask run
```

the server will run on [https://127.0.0.1:5000](https://127.0.0.1:5000)

Execute the db_config.py file in the terminal using the following command in the .env virtual environment:

```sh
python db_config.py
```

## ACCESS LINKS

### Retrieve (GET)

[https://127.0.0.1:5000/drinks](https://127.0.0.1:5000/drinks)

### Update (PUT)

[https://127.0.0.1:5000/drinks/&lt;id:int&gt;](https://127.0.0.1:5000/drinks/&lt;id:int%gt;)

### Update (POST)

[https://127.0.0.1:5000/drinks](https://127.0.0.1:5000/drinks)

### Update (DELETE)

[https://127.0.0.1:5000/drinks/&lt;id:int&gt;](https://127.0.0.1:5000/drinks/&lt;id:int%gt;)

This JSON requests for the PUT, POST, DELETE are sent through [POSTMAN - SOFTWARE](https://www.postman.com/downloads/)


#### To install the dependencies

```sh
pip install -r requirements.txt
```
#### To Deactivate the virtual environment

```sh
deactivate
```

