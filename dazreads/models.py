
from dazreads import db, login_manager
from flask_login import UserMixin
from datetime import datetime

#login_manager helps with user authentication.
@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))


class User(db.Model, UserMixin):
        #__tablename__ = 'User'
        id = db.Column(db.Integer, primary_key = True)
        username = db.Column(db.String(20), unique = True)
        email = db.Column(db.String(80), nullable = False)
        password = db.Column(db.String(80), nullable = False)
        image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
        reviews = db.relationship('Reviews', backref = 'users_id', lazy = True)
        rates = db.relationship('Rates', backref = 'users_id', lazy = True)

        def __repr__(self):
                return "%s, %s, %s" %( self.image_file, self.username, self.email)
        
class Post(db.Model):
        #__tablename__ = 'Post'
        id = db.Column(db.Integer, primary_key = True)
        title = db.Column(db.String, nullable = False)
        content = db.Column(db.Text, nullable = False)
        date_posted = db.Column(db.DateTime, default = datetime.utcnow)
        #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

class Books(db.Model):
        #__tablename__ = 'books'
        isbn = db.Column(db.String, primary_key = True)
        title = db.Column(db.String)
        author = db.Column(db.String)
        year = db.Column(db.String)
        reviews = db.relationship('Reviews', backref = 'books_id', lazy = True)
        rates = db.relationship('Rates', backref = 'books_id', lazy = True)

class Reviews(db.Model):
        #__tablename__='reviews'
        id = db.Column(db.Integer, primary_key = True)
        content = db.Column(db.Text, nullable = False)
        date_posted = db.Column(db.DateTime, default = datetime.utcnow)
        book_id = db.Column(db.String, db.ForeignKey('books.isbn'), nullable = False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique = True, nullable = False)
        

class Rates(db.Model):
        #__tablename__='rates'
        id = db.Column(db.Integer, primary_key = True)
        rating = db.Column(db.Integer)
        book_id = db.Column(db.Integer, db.ForeignKey('books.isbn'), nullable = False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
