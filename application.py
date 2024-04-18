from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
import json

with open('templates/config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True

application = Flask(__name__)
application.config.update(
    MAIL_SERVER='smtp.mail.yahoo.com',
    MAIL_PORT='465',
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password'],
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True
)

mail = Mail(application)

if local_server:
    # Update this line to point to your AWS RDS instance
    application.config["SQLALCHEMY_DATABASE_URI"] = "mysql://admin:123456789@blog-rds.cz8mq6s44e7a.ap-south-1.rds.amazonaws.com/blog_page_database"
else:
    application.config["SQLALCHEMY_DATABASE_URI"] = "mysql://admin:123456789@blog-rds.cz8mq6s44e7a.ap-south-1.rds.amazonaws.com/blog_page_database"

db = SQLAlchemy(application)

class Contact(db.Model):
    '''
    sno, name, phone_num, msg, date, email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    phone_num = db.Column(db.String(12), unique=True, nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    slug = db.Column(db.String(21), unique=True, nullable=False)
    content = db.Column(db.String(120), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(50), nullable=True)

@application.route('/dashboard', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        return render_template('login.html', params=params)

@application.route('/')
def home():
    posts = Posts.query.filter_by().all()[0:params['no_of_posts']]
    return render_template('index.html', params=params, posts=posts)



@application.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)

if __name__ == "__main__":
    application.run(debug=True)
