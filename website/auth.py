from distutils.command.build_scripts import first_line_re, flash
import email
from unicodedata import category
from flask import Blueprint, render_template, request
# storing roots for our site..., 

auth = Blueprint('auth', __name__) # set up Blueprint for flask app (auth Blueprint)...

@auth.route('/login', methods=['GET', 'POST']) # type requests it can accept...
def login():
    data = request.form # get data (from form attribute)
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # get all variables from form... (right?)
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email)<4: 
            flash('Email must be greater than 3 characters.', category='error') # know what categories mean?
        elif len(firstName) < 2: 
            flash('First name must be greater than 1 characters.', category='error') # know what categories mean?

        elif password1 != password2: 
            flash('Passwords don\'t match.', category='error') # know what categories mean?
        elif len(password1)<7: 
            flash('Password must be at least 7 characters.', category='error') # know what categories mean?
        else: # flash method on screen...
            flash('Account created!', category='error') # know what categories mean?

    return render_template("sign_up.html")
