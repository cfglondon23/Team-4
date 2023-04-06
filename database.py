import firebase_admin
from firebase_admin import db

KEY_PATH = 'privateKey/volunteerapp-1dc3a-firebase-adminsdk-2ntz8-d21784bfbf.json'
DB_URL = 'https://volunteerapp-1dc3a-default-rtdb.firebaseio.com/'
cred_obj = firebase_admin.credentials.Certificate(KEY_PATH)
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': DB_URL})

# takes parameters, stores it to the database, returns user id
def storeUserProfile(username, password, age):
    info = {"password": password, "age": age}
    ref = db.reference("/")
    ref.child("users").child(username).set(info)
    return username

# given user id, returns user info
def getUserProfile(username):
    ref = db.reference("/")
    return ref.child("users").child(username).get()

def userExists(username):
    ref = db.reference("/")
    return ref.child("users").child(username).get() != None

def getLocations():
    ref = db.reference("/")
    return ref.child("locations").get()

if __name__ == "__main__":
    k1 = storeUserProfile("bobsmith", "", 30)
    k2 = storeUserProfile("lilycarter", "", 22)
    k3 = storeUserProfile("jaycarter", "", 39)
    print(getUserProfile(k3))