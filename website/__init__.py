from flask import Flask

def create_app():
    app = Flask(__name__) # name of file ran??
    app.config['SECRET_KEY'] = 'fhsdjkfhsdkjfhdfjk'

    from website.views import views
    from website.auth import auth

    app.register_blueprint(views, url_prefix='/') # prefix at home? meaning all roots start at '/'?
    app.register_blueprint(auth, url_prefix='/') # prefix at home? meaning all roots start at '/'?

    return app
