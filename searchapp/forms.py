# Programmer: Sina Fathi-Kazerooni
# Email: sina@sinafathi.com
# WWW: sinafathi.com 

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class query_form(FlaskForm):
    title = StringField('Search in a Title:')
    submit = SubmitField('Search')


