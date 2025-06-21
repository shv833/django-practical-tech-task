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
