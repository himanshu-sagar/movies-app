# Movies Application


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
$ flask run
```