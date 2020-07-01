# django-demo


##### Install Django 3.0.7 in virtual environment for python3

Run below commands to activate virtual environment.

```
source bin/activate

pip install django==3.0.7

pip freeze
asgiref==3.2.10
Django==3.0.7
pytz==2020.1
sqlparse==0.3.1

```

pip freeze should show output like above.

Now run below command to run django as server.

```
python manage.py runserver
```

Check http://localhost:8000 or http://127.0.0.1:8000 for the dynamo code.


###### There are 2 applications currently in this repo.
1. Password generator
2. Token generator
