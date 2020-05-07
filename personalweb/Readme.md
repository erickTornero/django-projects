# A simple portfolio example

## Requirements 
```
django2
```

## Install & usage


```
git clone https://github.com/erickTornero/django-projects.git
```

```
cd django-projects/personalweb/
```

Create a superuser to access to the admin interface

```
python manage.py createsuperuser
```

Apply migrations, these migrations has been created on /portfolio/migrations

```
python manage.py migrate
```

Run the debug server 

```
python manage.py runserver
```

access to the admin server and login with the user previously created, the add new projects.

```
127.0.0.1:8000/admin
```