import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movie(db.Model):
    __tablename__ = 'movies'
    movie_id = sa.Column(sa.Integer, sa.Sequence('id_seq'), primary_key=True, index=True)  # Primary key | Indexed field
    title = sa.Column(sa.String(100), nullable=False)
    poster_path = sa.Column(sa.String(250), nullable=False)
    language = sa.Column(sa.String(20), nullable=False)
    overview = sa.Column(sa.String(500))
    release_date = sa.Column(sa.Date, nullable=False)

    def __init__(self, title, poster_path, language, overview, release_date):
        #self.movie_id = movie_id
        self.title = title
        self.poster_path = poster_path
        self.language = language
        self.overview = overview
        self.release_date = release_date

    def __repr__(self):
        return '<id {}>'.format(self.movie_id)
