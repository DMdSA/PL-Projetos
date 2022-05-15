from flask import Flask

__all__ = [
    "views",
]

#inicializing flask
def create_html():
    app = Flask(__name__)

    #incrypt/secure cookies 
    app.config['SECRET_KEY']='THIS IS A SECRET KEY'

    #importing our blueprints from views
    from .views import views 
    #registring the blueprints. url_prefix is what comes before the url page you want to acess
    #Ex1: www.example.com/home <- this has url_prefix ='/'
    #Ex2: www.example.com/Ply-simplex/home <- this has url_prefix = '/Ply-simplex/'
    app.register_blueprint(views, url_prefix='/')

    return app 