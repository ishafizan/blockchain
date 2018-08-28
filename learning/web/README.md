# 'Hello world' with django, web3.py

Basically simple mods from https://github.com/ishafizan/blockchain/tree/master/learning/hello_world

### Prerequisites
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

### Create django project
- git clone the project into dir of choosing
- From the command line, cd into web/ directory
```
python manage.py runserver
```
### Browser
set message
```
http://127.0.0.1:8000/hello_world/message/set/?message=hello
```
![Alt text](static/Screen%20Shot%202018-08-28%20at%206.00.45%20PM.png)
get message
```
http://127.0.0.1:8000/hello_world/message/get/
```
![Alt text](static/Screen%20Shot%202018-08-28%20at%206.00.36%20PM.png)

- tester
```
http://127.0.0.1:8000/hello_world/test/
```

## Author
* **Ishafizan Ishak**


