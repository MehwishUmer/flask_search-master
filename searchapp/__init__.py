# Programmer: Sina Fathi-Kazerooni
# Email: sina@sinafathi.com
# WWW: sinafathi.com 

from flask import Flask
from config import Config

searchapp = Flask(__name__)
searchapp.config.from_object(Config)
searchapp.jinja_env.add_extension('jinja2.ext.do')
from searchapp import routes

from flask_bootstrap import Bootstrap # import twitter bootstrap library
bootstrap = Bootstrap(searchapp)
