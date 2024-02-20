from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime


###
# Routing for your application.
###

#Global Variables


location = 'Kingston, Jamaica'
bio = """My name is Nicholas Joiles. A third year Com Sci major student with a big heart willing to contribute towards positive change 
I am the President of UWI Mona Circle k, a student-led service organization in the Caribbean District 
Our tenets, Service, leadership, and fellowship are exercised with every initiative we take on. Live to serve. Loooove to serve"""
posts_val = "40 "
foll_val = "90 "
fng_val = "140 "

def format_date_joined(yyyy,m,d):
    date_joined = datetime.date(yyyy, m, d) 
    return("Joined " + date_joined.strftime("%B, %Y"))

date = format_date_joined(2024, 2, 18)

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name = 'Nicholas Joiles')


@app.route('/profile')
def profile():
    return render_template('profile.html', name = 'Nicholas Joiles', alias = 'github: @Prxnce14', location = 'Kingston, Jamaica' 
                           , biography = ' My name is Nicholas Joiles. A third year Com Sci major student with a big heart willing to contribute towards positive change.\
                                    I am the President of UWI Mona Circle k, a student-led service organization in the Caribbean District.  \
                                    Our tenets, service, leadership, and fellowship are exercised with every initiative we take on. Live to serve. Loooove to serve', 
                                    date = format_date_joined(2024, 2, 18), post_val = "40 ", foll_val = "90 ", fng_val = "140 ")




###
# The functions below should be applicable to all Flask apps.
###

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
