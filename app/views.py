"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, send_from_directory
from app.add_property_form import AddPropertyForm
from app.models import PropertyModel
from werkzeug.utils import secure_filename
import os

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/property/', methods=['POST', 'GET'])
def addProperty():
    form = AddPropertyForm()
    if form.validate_on_submit() and request.method == 'POST':
        # get property data
        title = request.form["title"]
        propertyDesc = request.form["propertyDesc"]
        NoOfBedrooms = request.form["NoOfBedrooms"]
        NoOfBathrooms = request.form["NoOfBathrooms"]
        price = request.form["price"]
        propertyType = request.form["propertyType"]
        location = request.form["location"]
        
        #handle image upload
        imageString = form.photo.data
        secureImageString = secure_filename(imageString.filename)
        imageString.save(os.path.join(app.config['UPLOAD_FOLDER'], secureImageString))

        data = PropertyModel(title,propertyDesc, NoOfBedrooms, NoOfBathrooms, price, propertyType, location, secureImageString)

        db.session.add(data)
        db.session.commit()

        flash('Property was successfully Added!')
        return redirect(url_for('allProperties'))
        flash_errors(form)
    """Render the website's about page."""
    return render_template('add_property.html', form=form)

@app.route('/properties/')
def allProperties():
    properties = PropertyModel.query.all()
    """Render the website's about page."""
    return render_template('all_properties.html', properties = properties)

@app.route('/property/<propertyId>')
def singleProperty(propertyId):
    properties = PropertyModel.query.filter_by(id=propertyId).first()

    """Render the website's about page."""
    return render_template('single_property.html', properties=properties)

@app.route('/images/<filename>')
def fetchImage(filename):
    rootdirectory = os.getcwd()
    return  send_from_directory(os.path.join(rootdirectory,app.config['UPLOAD_FOLDER']),filename)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
