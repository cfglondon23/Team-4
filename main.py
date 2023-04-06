#https://flask.palletsprojects.com/en/2.2.x/quickstart/

# To run, execute following commands:
# venv\Scripts\activate
# flask --app main run

from flask import Flask, render_template
from markupsafe import escape
import database

app = Flask(__name__)

@app.route('/')
def homePage():
    return "home page"

# Volunteer
@app.route('/login')
def volunteerLogin():
    return render_template('login.html')

@app.route('/register')
def volunteerRegister():
    return render_template('register.html')

@app.route('/user/<username>')
def volunteerPage(username):
    return f'Volunteer page: {escape(username)}'

@app.route('/user/<username>/profile')
def volunteerProfile(username):
    return f'Volunteer profile: {escape(username)}'

@app.route('/user/<username>/rewards')
def volunteerRewards(username):
    return f'Volunteer rewards: {escape(username)}'

@app.route('/user/<username>/vacancySearch')
def volunteerVacancySearch(username):
    return f'Volunteer vacancy search: {escape(username)}'

# School

@app.route('/login')
def schoolLogin():
    return render_template('login.html')

@app.route('/register')
def schoolRegister():
    return render_template('register.html')

@app.route('/school/<school>')
def vacancyListing(school):
    return f'Vacancy listing: {escape(school)}'

@app.route('/school/<school>/applications')
def applicationListing(school):
    return f'Application listing: {escape(school)}'