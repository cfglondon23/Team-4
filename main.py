#https://flask.palletsprojects.com/en/2.2.x/quickstart/

# To run, execute following commands:
# venv\Scripts\activate
# flask --app hello run

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def homePage():
    return 'Home page'

@app.route('/volunteerLogin')
def volunteerLogin():
    return 'Volunteer login'

@app.route('/schoolLogin')
def schoolLogin():
    return 'School login'

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