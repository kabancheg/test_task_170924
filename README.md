## Docker

### lets migrate and createsuperuser
`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py createsuperuser`

### Start new project. Creates app folder with manage.py etc...
`docker compose run --rm app sh -c "django-admin startproject app"`
`docker compose run --rm app sh -c "python manage.py startapp test"`

### To run makemigrations without exec.
`docker compose run --rm app sh -c "python manage.py makemigrations"`
`docker compose run --rm app sh -c "python manage.py createsuperuser"`

### import logs
`docker compose run --rm app sh -c "python manage.py import_logs /nginx_json_logs.txt"`

### test request
`http://localhost:8000/api/logitems?status=304&timestamp_gte=04-06-2015`