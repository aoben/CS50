from flask import render_template, url_for, flash, redirect, request
from dazreads import app, db, bcrypt
from dazreads.forms import RegistrationForm, LoginForm, SearchForm
from dazreads.models import User, Post, Books  #this is put here to avoid a circular error...so this runs after db = SQLAlchemy(app)
from flask_login import login_user, current_user, logout_user, login_required




posts=[{'author':'corey schafer',
        'title':'Blog post 1', 
        'content':'First post content',
        'date_posted':'April 20, 2018'},
        {'author':'Jane Doe',
        'title':'Blog post 2', 
        'content':'Second post content',
        'date_posted':'April 21, 2018'

        }]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
        if current_user.is_authenticated:
                return redirect(url_for('home'))
        form = RegistrationForm()
        if form.validate_on_submit():
                hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                user = User(username = form.username.data, email = form.email.data, password = hashed_password)
                db.session.add(user)
                db.session.commit()
                flash('Your Account has been created! You are now able to log in', 'success')
                return redirect(url_for('login'))
        return render_template('register.html', title = 'Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
        if current_user.is_authenticated:
                return redirect(url_for('home'))
        form = LoginForm()
        if form.validate_on_submit():
                user = User.query.filter_by(email = form.email.data).first()
                if user and bcrypt.check_password_hash(user.password, form.password.data):
                        flash('Log in successful. Please check email and password', 'success')
                        login_user(user, remember = form.remember.data)
                        next_page = request.args.get('next')
                        return redirect(next_page) if next_page else redirect(url_for('home'))
                else:
                        flash('Login Unsuccessful. Please check email and password', 'danger')
        return render_template('login.html', title = 'Login', form=form)

books = []

@app.route("/search", methods=['GET', 'POST'])
@login_required
def search():
        form = SearchForm()
        if form.isbn != None or form.title!= None or form.author != None:
                #The data from the froms need to be transformed first before passing it to ORM query
                isbn_data = '%' + str.capitalize(form.isbn.data) + '%'
                title_data = '%' + str.capitalize(form.title.data) + '%'
                author_data = '%' + str.capitalize(form.author.data) + '%'
                books = Books().query.filter(Books.isbn.like(isbn_data), Books.title.like(title_data), Books.author.like(author_data)).all()
                flash('See results of search!', 'success')
       
        return render_template('search.html', title = 'Search', form = form, posts = books)



@app.route("/logout")
def logout():
        logout_user()
        return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
        return render_template('account.html', title = 'Account')