import firebase_admin
from firebase_admin import db
import json

KEY_PATH = 'privateKey/volunteerapp-1dc3a-firebase-adminsdk-2ntz8-d21784bfbf.json'
DB_URL = 'https://volunteerapp-1dc3a-default-rtdb.firebaseio.com/'
cred_obj = firebase_admin.credentials.Certificate(KEY_PATH)
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': DB_URL})



# takes parameters, stores it to the database
def createUserProfile(username, password, age):
    file_contents = {"username": username, "password": password, "age": age}
    ref = db.reference("/")
    ref.child("users").push(file_contents)

if __name__ == "__main__":
    createUserProfile("bobsmith", "", 30)
    createUserProfile("lilycarter", "", 22)