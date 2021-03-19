from flask_wtf.csrf import CSRFProtect
from app import app
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, TextAreaField, TextField, SelectField 
from flask_wtf.file import FileField, FileRequired, FileAllowed


class AddPropertyForm(FlaskForm):
    csrf = CSRFProtect(app)
    title = TextField('Title', validators=[DataRequired()])
    NoOfBedrooms = TextField('NoOfBedrooms', validators=[DataRequired()])
    NoOfBathrooms = TextField('NoOfBathrooms', validators=[DataRequired()])
    location = TextField('location', validators=[DataRequired()])
    price = TextField('price', validators=[DataRequired()])
    propertyType = SelectField('propertyType', validators=[DataRequired()])
    propertyDesc = TextAreaField('propertyDesc', validators=[DataRequired()])
    photo = FileField('propertyImage', validators=[DataRequired()])

