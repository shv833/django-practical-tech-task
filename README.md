# django-practical-tech-task

# How to run project locally
1. Rename `.env.example` to `.env`
2. Set values in `.env` file
3. Run command `make` and the project is starting 
* Fixtures are loaded automatically via `entrypoint.sh` — no manual action needed.
* Deployed at: https://django-practical-tech-task.onrender.com.
⚠️ Note: This is a free Render.com plan, so startup may be slow or the server may go offline. Please contact me if it's unavailable.
* Celery worker is not running on the deployed version due to free tier limitations. It can be tested locally or redeployed with a paid plan.
* AI translation may stop working if the free OPENAI_API_KEY usage limit is exceeded.

# Setup (powershell)
## Pyenv
```Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"```

## Poetry
```(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -```

If you don't have 'make' utility, run `winget install ezwinports.make`

Use commands from makefile to install specific python version and dependencies
```
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
```

# Usefull commands
* To load fixture, run `make load-fixture`
* To run migrations, run `make mmigrate`
* To run tests, run `make run-tests`
* To run project, run `make run`
* Install this and add bin folder to global path so you can generate pdf. `https://wkhtmltopdf.org/downloads.html`


## API Usage (CRUD for CV)
- List all CVs: `GET /api/cv/`
- Retrieve a CV: `GET /api/cv/<id>/`
- Create a CV: `POST /api/cv/` (JSON body)
- Update a CV: `PUT /api/cv/<id>/` (JSON body)
- Delete a CV: `DELETE /api/cv/<id>/`

Example (using curl):

```
curl -X GET http://localhost:8000/api/cv/

curl -X POST http://localhost:8000/api/cv/ -H "Content-Type: application/json" -d "{\"firstname\": \"Alan\", \"lastname\": \"a\", \"skills\": [\"Math\"], \"projects\": [], \"bio\": \"Pioneer\", \"contacts\": {\"email\": \"alan@example.com\"}}"

curl -X PUT http://localhost:8000/api/cv/1/ -H "Content-Type: application/json" -d "{\"firstname\": \"Alan\", \"lastname\": \"a\", \"skills\": [\"Math\", \"CS\"], \"projects\": [], \"bio\": \"Pioneer\", \"contacts\": {\"email\": \"alan@example.com\"}}"

curl -X DELETE http://localhost:8000/api/cv/1/
```

## Other endpoints
* settings - `http://localhost:8000/settings/`
* logs - `http://localhost:8000/logs/`
* list of cvs - `http://localhost:8000/`
* cv details - `http://localhost:8000/cv/1/`

# Requirements:
Follow PEP 8 and other style guidelines, use clear and concise commit messages and docstrings where needed, structure your project for readability and maintainability, optimize database access using Django's built-in methods, and provide enough details in your README.

# Version Control System
1. Create a public GitHub repository for this practical test.
2. Put the text of this test (all instructions) into README .md.
3. For each task, create a separate branch (for example, tasks/task-1, tasks/task-2, etc.).
4. When you finish each task, merge that branch back into main but do not delete the original task branch.

# Python Virtual Environment
1. Use pyenv to manage the Python version. Create a file named .python-version in yourrepository to store the exact Python version.
2. Use Poetry to manage and store project dependencies. This will create a pyproject.toml file.
3. Update your README .md with clear instructions on how to set up and use pyenv and Poetry for this project.

# Tasks
## Task 1: Django Fundamentals
1. Create a New Django Project
* Name it something like CVProject.
* Use the Python version set up in Task 2 and the latest stable Django release.
* Use SQLite as your database for now.
2. Create an App and Model
* Create a Django app (for example, main).
* Define a CV model with fields like firstname, lastname, skills, projects, bio, and contacts.
* Organize the data in a way that feels efficient and logical.
3. Load Initial Data with Fixtures
* Create a fixture that contains at least one sample CV instance.
* Include instructions in README .md on how to load the fixture.
4. List Page View and Template
* Implement a view for the main page (e.g., `/`) to display a list of CV entries.
* Use any CSS library to style them nicely.
* Ensure the data is retrieved from the database efficiently.
5. Detail Page View
* Implement a detail view (e.g., `/cv/<id>/`) to show all data for a single CV.
* Style it nicely and ensure efficient data retrieval.
6. Tests
* Add basic tests for the list and detail views.
* Update README.md with instructions on how to run these tests.

## Task 2: PDF Generation Basics
1. Choose and install any HTML-to-PDF generating library or tool.
2. Add a'Download PDF' button on the CV detail page that allows users to download the CV as a
PDF.

## Task 3: REST API Fundamentals
1. Install Django REST Framework (DRF).
2. Create CRUD endpoints for the CV model (create, retrieve, update, delete).
3. Add tests to verify that each CRUD action works correctly.

## Task 4: Middleware & Request Logging
1. Create a RequestLog Model
* You can put this in the existing app or a new app (e.g., audit ).
* Include fields such as timestamp, HTTP method, path, and optionally other details like query string, remote IP, or logged-in user.
2. Implement Logging Middleware
* Write a custom Django middleware class that intercepts each incoming request.
* Create a RequestLog record in the database with the relevant request data.
* Keep it efficient.
3. Recent Requests Page
* Create a view (e.g., /logs/) showing the 10 most recent logged requests, sorted by timestamp descending.
* Include a template that loops through these entries and displays their timestamp, method, and path.
4. Test Logging
* Ensure your tests verify the logging functionality.

## Task 5: Template Context Processors
1. Create settings_context
* Create a context processor that injects your entire Django settings into all templates.
2. Settings Page
* Create a view (e.g., /settings/ ) that displays DEBUG and other settings values made available by the context processor.

## Task 6: Docker Basics
1. Use Docker Compose to containerize your project.
2. Switch the database from SQLite to PostgreSQL in Docker Compose.
3. Store all necessary environment variables (database credentials, etc.) ina .env file.

## Task 7: Celery Basics
1. Install and configure Celery, using Redis or RabbitMQ as the broker.
2. Add a Celery worker to your Docker Compose configuration.
3. On the CV detail page, add an email input field and a 'Send PDF to Email' button to trigger a
Celery task that emails the PDF.

## Task 8: OpenAl Basics
1. On the CV detail page, add a 'Translate' button and a language selector.
2. Include these languages: Cornish, Manx, Breton, Inuktitut, Kalaallisut, Romani, Occitan, Ladino, Northern Sami, Upper Sorbian, Kashubian, Zazaki, Chuvash, Livonian, Tsakonian, Saramaccan, Bislama,
3. Hook this up to an OpenAIl translation API or any other translation mechanism you prefer. The idea is to translate the CV content into the selected language.

## Task 9: Deployment
Deploy this project to DigitalOcean or any other VPS.
That's it!

Complete each task thoroughly, commit your work following the branch-and-merge structure, and make sure your README .md clearly explains how to install, run, and test everything. We look forward to reviewing your submission!

Thank you!
