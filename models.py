__author__ = 'ajrenold'

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Flaskr(db.Model):

    __tablename__ = 'flaskr'

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return '<title {}>'.format(self.title)

class Book(db.Model):

    __tablename__ = 'books'

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    publisher = db.Column(db.String, nullable=False)
    cover_large = db.Column(db.String, nullable=False)
    cover_thumb = db.Column(db.String, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('author.author_id'))

    #genres = ["Fiction","Romance"]

    def __init__(self, title, author, publisher, cover_large, cover_thumb):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.cover_large = cover_large
        self.cover_thumb = cover_thumb

    @staticmethod
    def book_from_dict(**kwargs):
        return Book(kwargs.get('title', ""),
                    kwargs.get('author', ""),
                    kwargs.get('publisher', ""),
                    kwargs.get('cover_large', ""),
                    kwargs.get('cover_thumb', ""))

    def __repr__(self):
        return '<title {}>'.format(self.title)

class Author(db.Model):

    __tablename__ = 'author'

    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    bio = db.Column(db.String, nullable=False)
    picture = db.Column(db.String, nullable=False)
    website = db.Column(db.String, nullable=False)
    blog = db.Column(db.String, nullable=False)
    books = db.relationship('Book', backref='author',
                                lazy='dynamic')

    def __init__(self, name, bio, picture, website, blog, twitter_id):
        self.name = name
        self.bio = bio
        self.picture = picture
        self.website = website
        self.blog = blog
        self.twitter_id = twitter_id

    @staticmethod
    def author_from_dict(**kwargs):
        return Author(kwargs.get('name', ""),
                      kwargs.get('bio', ""),
                      kwargs.get('picture', ""),
                      kwargs.get('website', ""),
                      kwargs.get('blog', ""),
                      kwargs.get('twitter_id', ""))

    def __repr__(self):
        return '<author {}>'.format(self.name)