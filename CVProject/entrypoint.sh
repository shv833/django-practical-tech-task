#!/bin/sh
# echo "$PWD"

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata main/fixtures/cv_fixture.json
uvicorn CVProject.asgi:application --host 0.0.0.0 --port 8000

exec "$@"
