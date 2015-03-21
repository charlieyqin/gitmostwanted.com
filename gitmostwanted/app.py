from os import environ
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.oauthlib.client import OAuth

env = environ.get('GMW_APP_ENV', 'development').capitalize()

app = Flask(__name__)
app.config.from_object('gitmostwanted.config.Config' + env)
app.config.from_envvar('GMW_APP_SETTINGS', silent=True)

db = SQLAlchemy(app)

oauth = OAuth()
oauth.remote_app('github', app_key='OAUTH_GITHUB')
oauth.init_app(app)
