from flask_wtf import FlaskForm
from wtforms import SubmitField

class TVForm(FlaskForm):
    submit = SubmitField('Wake Up TV!')
