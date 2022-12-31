from flask import Flask
from flask_migrate import Migrate
from flask_script import Manager
from movies.urls import movie_blueprint
import os
from movies.models import db
from helpers.logger import init_logger

app = Flask(__name__)

app.config.from_pyfile('config.py')

#db = SQLAlchemy(app=app)
db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)

init_logger(app)


@app.route("/")
def index():
    return "Welcome to Movies App"


app.register_blueprint(movie_blueprint)

if __name__ == '__main__':
    app.logger.info("Starting the application...")
    manager.run()
    # db.create_all()
    # app.run()
