from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

#configure session for database, 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mgultkmabtmtfo:63bbf2d3b7a2eedf489c1ee0919bf0b83a938da5076e5e2ca1b1f80e0cb69e26@ec2-54-83-61-142.compute-1.amazonaws.com:5432/d10jbj0bu0oie5' #'sqlite://///Users/Oben/Documents/CS50/Project1/dazreads/site.db' 
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = '250d2a22815f08b89db09f804cef4f09'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_categroy = 'info'

from dazreads import  routes