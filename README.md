# Movies Application

## Features & Tech Stack
---
* Movies related REST APIs
* Logging & Monitoring of the application on Elastic APM
* Built using SQLAlchemy ORM
* Caching on redis
* Deployment on Docker
* Tech Stack: Python, Flask, SQLAlchemy, Elastic-APM, PostgreSQL, REST API, Docker
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

### Run application in Docker using Dockerfile and docker-compose.yml
Note: add ```.env_docker``` for this
```sh
$ docker compose build
$ docker compose up
```

# Screenshots
![image](https://user-images.githubusercontent.com/49094337/210155651-8fcd3bae-2c6b-4409-ac62-d444ccc74eb5.png)

![image](https://user-images.githubusercontent.com/49094337/210155626-dc0f4f84-2e5d-4f45-9cbb-6e2f8ce33434.png)
![image](https://user-images.githubusercontent.com/49094337/210155732-3ddc4ef9-418c-4fa5-845d-4fdef0f57e23.png)

![image](https://user-images.githubusercontent.com/49094337/210155661-3e9da15e-8932-4318-b024-d9cb94c98185.png)

![image](https://user-images.githubusercontent.com/49094337/210155670-dc0d87c9-ba93-4211-9363-b22160a10a06.png)

![image](https://user-images.githubusercontent.com/49094337/210155702-884cd0ef-a6e8-4a80-9813-6b2cc40abfd1.png)
