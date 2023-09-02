from flask import Flask, render_template, request
from flask_sqlalchemy import  SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
import json


with open('templates/config.json', 'r') as c:
    params = json.load(c)["params"]
    
local_server = True
     
app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.mail.yahoo.com',
    MAIL_PORT = '465',
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-password'],  
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True
)

mail = Mail(app)

if(local_server): 
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']
    
    
db = SQLAlchemy(app)

class Contact(db.Model):
    '''
    sno, name, phone_num, msg, date, email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    phone_num = db.Column(db.String(12), unique=True, nullable = False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)
    
class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    slug = db.Column(db.String(21), unique=True, nullable = False)
    content= db.Column(db.String(120), nullable=False)
    tagline= db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(50), nullable=True)
    
@app.route('/dashboard', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        return render_template('login.html', params = params)    
   
@app.route('/')
def home():
    posts = Posts.query.filter_by().all()[0:params['no_of_posts']]
    return render_template('index.html', params= params, posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', params= params)

# methods=["GET","POST"] security provide krta, parameters not shown in url
@app.route("/contact", methods=["GET","POST"])
def contact():
    if(request.method == 'POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone') # a local variable stores value got from form accesed with value of name attribute in form
        message = request.form.get('message')  
        
        # sno, name, phone_num, msg, date, email
        entry = Contact(name=name, phone_num= phone, msg= message, email = email, date = datetime.now())
        db.session.add(entry)
        db.session.commit()
        # msg = Message("Hey", sender=email, recipients=params['gmail-user'])
        # msg.body = "Hey how are you? is everything okay?"
        # mail.send(msg)
        
             
    return render_template('contact.html', params= params)

@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug= post_slug).first() 
    return render_template('post.html', params= params, post=post)


app.run(debug=True)