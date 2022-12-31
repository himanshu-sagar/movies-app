from flask import Blueprint
from movies import views
import os
from config import VERSION

movie_blueprint = Blueprint('movie_blueprint', __name__, url_prefix=f'/{VERSION}')

movie_blueprint.add_url_rule('/movie/<int:movie_id>', view_func=views.MovieView.as_view('movies'))
movie_blueprint.add_url_rule('/movie', view_func=views.MovieView.as_view('add-movies'))
