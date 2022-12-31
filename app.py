from flask import Flask
from flask_migrate import Migrate
from flask_script import Manager
from movies.urls import movie_blueprint
from movies.models import db
from helpers.logger import init_logger


def initialize_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    #db = SQLAlchemy(app=app)
    db.init_app(app)
    migrate = Migrate(app, db)
    manager = Manager(app)

    # Start logging and monitoring
    init_logger(app)

    # Register Blueprints
    app.register_blueprint(movie_blueprint)

    @app.route("/")
    def index():
        return "Welcome to Movies App"

    app.logger.info("Starting the application...")
    #manager.run()
    return app


# if __name__ == '__main__':

#     initialize_app()
