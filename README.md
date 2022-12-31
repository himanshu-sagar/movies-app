# Movies Application

## Features & Tech Stack
---
* Movies related REST APIs
* Logging & Monitoring of the application on Elastic APM
* Built using SQLAlchemy ORM
* Tech Stack: Python, Flask, SQLAlchemy, Elastic-APM, PostgreSQL, REST API 
## Steps to Setup
---
* Add ```.env``` file, using ```.env_example```
## Commands
--------------
### Install all dependencies
```sh
$ pip install pipenv
$ pipenv shell
$ pipenv install
```

### Set up Migrations
```sh
$ flask db init
$ flask db migrate
$ flask db upgrade
```
### Running the application

```sh
$ sh run.sh
```