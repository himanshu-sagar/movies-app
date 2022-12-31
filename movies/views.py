from flask import make_response, views, request
from movies.models import Movie, db
from movies.serializers import MovieSerializer


class MovieView(views.MethodView):
    def get(self, movie_id):
        data = Movie.query.get({"movie_id": movie_id})
        serializer = MovieSerializer()
        return make_response({"data": serializer.dump(data)})

    def post(self):
        data = request.get_json()
        serializer = MovieSerializer()
        new_movie = Movie(**data)
        db.session.add(new_movie)
        db.session.commit()
        return make_response({"data": serializer.dump(new_movie)}, 201)


# from flask import Blueprint
# from movies import views

# # movie_blueprint = Blueprint('movie_blueprint', __name__)

# # movie_blueprint.add_url_rule('/movie', view_func=views.MovieView.as_view('movies'))