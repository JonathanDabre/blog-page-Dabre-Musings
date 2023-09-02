# # from flask import Flask, render_template
# # app = Flask(__name__)

# # @app.route('/')
# # def hello():
# #     return render_template('index.html')

# # @app.route("/harry")
# # def harry():
# #     return "Hello Harry Bhai!"

# # @app.route('/about')
# # def about():
# #     name = 'Jonathan1'
# #     return render_template('about.html', naav= name)

# # app.run(debug=True)
# # -------------------------------------------------------


# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return render_template('index.html')

# @app.route("/harry")
# def harry():
#     return "Hello Harry Bhai!"

# @app.route('/about')
# def about():
#     name = 'Jonathan1'
#     return render_template('about.html', naav= name)

# @app.route('/bootstrap')
# def bootstrap():
#     return render_template('bootstrap.html')

# app.run(debug=True)

#In flask there is jinja template inheritance which can be used if our website has some common parts on all pages
# in jinja template inheritance there's a file called layout
#layout file structure in this way.
#suppos we are building a blog website, in which navigation bar and footer is same on all pages
#so layout.html page will be this way
# all the doctype and html header files and links here.
#then the navigation part html
# then there will be this part
# {% block body %}
#  
# {% end block %}

#we will surrond both those commands on every page of our website. This block contains the part which is not common
# then there will be footer part in the layout page

#on each page we will remove the common part and at start of page we will write {% extends "layout.html" %}
#and will surrond the part  which is unique/ not common with 
# {% block body %}
#  
# {% end block %}