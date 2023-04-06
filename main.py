#https://flask.palletsprojects.com/en/2.2.x/quickstart/

# To run, execute following commands:
# venv\Scripts\activate
# flask --app main run

from flask import Flask, render_template, request, redirect
from markupsafe import escape
import database as db
import pdb

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('simplehomepage.html')

@app.route('/aboutus')
def aboutUs():
    return render_template('aboutus.html')

# Volunteer
@app.route('/login')
def volunteerLogin():
    return render_template('login.html')

@app.route('/loginAction', methods =["GET", "POST"])
def loginAction():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        userInfo = db.getUserProfile(username)
        if userInfo == None:
            # username does not exist
            return "username does not exist"
        elif userInfo["password"] != password:
            return "incorrect password"
        else:
            # login success
            return redirect('user/'+username)
    return render_template("login.html")

@app.route('/register')
def volunteerRegister():
    return render_template('register.html')

@app.route('/registerAction', methods =["GET", "POST"])
def registerAction():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        age = request.form.get("age")
        # check if username exists in db already
        if db.userExists(username):
            return "username already exists"
        else:
            db.storeUserProfile(username, password, age)
            return redirect('user/'+username)
    return render_template("register.html")

@app.route('/user/<username>')
def volunteerPage(username):
    return render_template("profiledash.html", data=[f"/user/{username}/vacancySearch", f"/user/{username}/rewards"])

@app.route('/user/<username>/rewards')
def volunteerRewards(username):
    return render_template("rewards.html")

@app.route('/user/<username>/vacancySearch')
def volunteerVacancySearch(username):
    locations = db.getLocations()
    vacantLocations = []
    for key in locations:
        if locations[key]["isVacant"]:
            vacantLocations.append(key)

    data = [list(locations.keys()), vacantLocations]
    return render_template("volunteerVacancySearch.html", data=data)

# School

@app.route('/login')
def schoolLogin():
    return render_template('login.html')

@app.route('/register')
def schoolRegister():
    return render_template('register.html')

@app.route('/school/<school>')
def vacancyListing(school):
    return render_template('listingvacancies.html')

@app.route('/school/<school>/applications')
def applicationListing(school):
    return render_template("applicationsreceived.html")
 
if __name__=='__main__':
   app.run(debug=True)