#!/bin/sh
# echo "$PWD"
set -e

if [ "$1" = "celery" ]; then
    echo "Starting Celery worker..."
    exec poetry run celery -A CVProject worker --loglevel=debug
else
    echo "Starting Django app..."
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic --noinput
    python manage.py loaddata main/fixtures/cv_fixture.json
    uvicorn CVProject.asgi:application --host 0.0.0.0 --port 8000
fi
exec "$@"
