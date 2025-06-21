# variables
DOCKER_COMPOSE = docker compose
DEV_COMPOSE_FILE = docker-compose.yml


# dev
dev:
	$(DOCKER_COMPOSE) -f $(DEV_COMPOSE_FILE) up --force-recreate --remove-orphans

cdev:
	$(DOCKER_COMPOSE) -f $(DEV_COMPOSE_FILE) up --force-recreate --remove-orphans --build


# poetry
p-install:
	poetry install

p-install-shell:
	poetry self add poetry-plugin-shell

p-activate:
	poetry shell


# pyenv
pe-install:
	pyenv install 3.13.2

pe-set-py:
	pyenv local 3.13.2

# django cmd
mmigrate:
	cd CVProject && poetry run python manage.py makemigrations && poetry run python manage.py migrate

run:
	cd CVProject && poetry run python manage.py runserver

run-tests:
	cd CVProject && poetry run python manage.py test

load-fixture:
	cd CVProject && poetry run python manage.py loaddata main/fixtures/cv_fixture.json
