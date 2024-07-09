# Vue-Flask Web App Framework
## Introduction
This repository will hold the minimum amount of code to get started with the following:

* Backend

    * Flask
    * Flask blueprints
    * Flask-SQLAlchemy
    * Flask-migrate
    * Postgres SQL database
* Frontend

    * Vue 3 + Vite
    * Vue-Router
    * Pinia (State management)
    * Javascript
    * TailwindCSS
* Deployment

    * Docker + Docker Compose
    * Frontend served using Ngnix
    * Backend served using Gunicorn
    * CI/CD pipeline using Github Actions
* Testing

    * Pytest
    * Vitest

# Setting up postgreSQL database on macOS
## Install postgres and create user
```sh
brew install postgresql
createuser -s postgres
brew services restart postgresql
```
## Setup pgAdmin/dBeaver

## Initialise migrations folder
```sh
cd backend
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```


