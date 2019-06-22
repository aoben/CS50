
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
        #posts = db.relationship('Post', backref = 'author', lazy = True)

        def __repr__(self):
                return "%s, %s, %s" %( self.image_file, self.username, self.email)
        
class Post(db.Model):
        #__tablename__ = 'Post'
        id = db.Column(db.Integer, primary_key = True)
        title = db.Column(db.String, nullable = False)
        content = db.Column(db.Text, nullable = False)
        date_posted = db.Column(db.DateTime, default = datetime.utcnow)
        #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
