from flask_wtf.csrf import CSRFProtect
from app import app
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, TextAreaField, TextField, SelectField 
from flask_wtf.file import FileField, FileRequired, FileAllowed


class AddPropertyForm(FlaskForm):
    csrf = CSRFProtect(app)
    title = TextField('Title', validators=[DataRequired()])
    propertyDesc = TextAreaField('Property Description', validators=[DataRequired()])
    NoOfBedrooms = TextField('Number of Bedrooms', validators=[DataRequired()])
    NoOfBathrooms = TextField('Number of Bathrooms', validators=[DataRequired()])
    price = TextField('Price', validators=[DataRequired()])
    propertyType = SelectField("Property Type", choices=[('1', 'House'), ('2', 'Apartment')], validators = [DataRequired()]) 
    location = TextField('Location', validators=[DataRequired()])
    photo = FileField('Property Image', validators=[DataRequired()])

