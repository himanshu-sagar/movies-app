from flask import views, request
from movies.models import Movie, db
from movies.serializers import MovieSerializer
from helpers.response_handlers import throw_response, throw_error


class MovieView(views.MethodView):
    def get(self, movie_id):
        data = Movie.query.get({"movie_id": movie_id})
        serializer = MovieSerializer()
        data = serializer.dump(data)
        return throw_response(data, 200)

    def post(self):
        data = request.get_json()
        serializer = MovieSerializer()

        try:
            if serializer.load(data):
                new_movie = Movie(**data)
                db.session.add(new_movie)
                db.session.commit()
        except Exception as e:
            return throw_error(error=type(e).__name__, status=400, message=str(e))
        return throw_response({"data": serializer.dump(new_movie)}, 201)
