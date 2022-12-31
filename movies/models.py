import sqlalchemy as sa
from helpers.init_apps import db


class Movie(db.Model):
    __tablename__ = 'movies'
    movie_id = sa.Column(sa.Integer, primary_key=True, index=True)  # Primary key | Indexed field
    title = sa.Column(sa.String(100), nullable=False)
    poster_path = sa.Column(sa.String(250), nullable=False)
    language = sa.Column(sa.String(20), nullable=False)
    overview = sa.Column(sa.String(500))
    release_date = sa.Column(sa.Date, nullable=False)

    def __init__(self, movie_id, title, poster_path, language, overview, release_date):
        self.movie_id = movie_id
        self.title = title
        self.poster_path = poster_path
        self.language = language
        self.overview = overview
        self.release_date = release_date

    def __repr__(self):
        return '<id {}>'.format(self.movie_id)
