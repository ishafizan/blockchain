# 'Hello world' with django, web3.py, infura.io, rinkeby

Simple mods from https://github.com/ishafizan/blockchain/tree/master/learning/hello_world
Set/Get methods via REST with Django

### Prerequisites
- Linux or Mac is recommended, and you need Python 3.6+. If you are using Windows, either setup a VM or use the Linux Subsystem

Python 3.7
Django 2.1
web3.py 4.6.0

```
python3 -m venv project_name
source project_name/bin/activate
which python3
which python
pip3 install web3==4.6.0
pip3 install -e django/
```
- contract has been deployed to rinkeby & address available

### Create django project
- git clone the project into dir of choosing 
- create project (within venv) via django-admin
```
django-admin startproject web
```
- From the command line, cd into web/ directory
- edit web/urls.py
- copy hello_world folder into django web project
- edit web/hello_world/settings.py & edit necessary info (eg: contract location/addr)

![Alt text](static/Screen%20Shot%202018-08-28%20at%206.51.34%20PM.png)

### Start internal server
```
python manage.py runserver
```
### Browser
- set message
```
http://127.0.0.1:8000/hello_world/message/set/?message=hello world !!!
```
![Alt text](static/Screen%20Shot%202018-08-29%20at%204.50.35%20PM.png)

- get message
```
http://127.0.0.1:8000/hello_world/message/get/
```
![Alt text](static/Screen%20Shot%202018-08-29%20at%204.47.35%20PM.png)

- tester
```
http://127.0.0.1:8000/hello_world/test/
```

## Author
* **Ishafizan Ishak**


