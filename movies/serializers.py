import flask_marshmallow as ma


class MovieSerializer(ma.Schema):
    class Meta:
        fields = ('movie_id', 'poster_path', 'language', "overview", "release_date")


# movie_schema = MovieSerializer(strict=True)