import flask_marshmallow as ma
from movies.models import Movie, db
from marshmallow import fields, validate


class MovieSerializer(ma.Schema):
    """Serialize the data"""
    title = fields.Str(required=True, validate=validate.Length(max=100))
    poster_path = fields.Str(required=True, validate=validate.Length(max=250))
    language = fields.Str(required=True, validate=validate.Length(max=20))
    overview = fields.Str(required=True, validate=validate.Length(max=500))
    release_data = fields.Date(required=True)

    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'poster_path', 'language', "overview", "release_date")
