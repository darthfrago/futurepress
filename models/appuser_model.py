__author__ = 'ajrenold'

from core import db
from model_utils import stormpathUserHash

user_books = db.Table('user_books',
    db.Column('book_id', db.Integer, db.ForeignKey('books.book_id')),
    db.Column('user_id', db.String(128), db.ForeignKey('app_users.user_id'))
)

class AppUser(db.Model):

    __tablename__ = 'app_users'

    # primary key
    user_id = db.Column(db.String(128), primary_key=True)

    # relationships
    author = db.relationship('Author', uselist=False, backref='app_user')
    # user_books table
    books = db.relationship('Book', secondary=user_books,
                           backref=db.backref('app_users', lazy='joined'), lazy='dynamic')

    #other columns
    user_href = db.Column(db.String(1024), nullable=False)
    is_author = db.Column(db.Boolean, nullable=False)
    test_column = db.Column(db.String(1024))

    def __init__(self, storm_path_user_href, author=None):
        self.user_id = stormpathUserHash(storm_path_user_href)
        self.user_href = storm_path_user_href
        self.author = author
        self.is_author = True if author is not None else False
        self.test_column = '1'

    def __repr__(self):
        return '<user {}>'.format(self.user_id)

    def as_dict(self):
        return {
            'user_id': self.user_id,
            'user_href': self.user_href,
            'is_author': self.is_author,
            'test_column': self.test_column
        }