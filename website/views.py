from flask import Blueprint, render_template
# storing roots for our site...

views = Blueprint('views', __name__) # set up Blueprint for flask app (views Blueprint)...

@views.route('/') # typical root for "home" page
def home():
    return render_template("home.html")



