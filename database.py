import firebase_admin
from firebase_admin import db

KEY_PATH = 'privateKey/volunteerapp-1dc3a-firebase-adminsdk-2ntz8-d21784bfbf.json'
DB_URL = 'https://volunteerapp-1dc3a-default-rtdb.firebaseio.com/'
cred_obj = firebase_admin.credentials.Certificate(KEY_PATH)
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': DB_URL})

# takes parameters, stores it to the database, returns user id
def createUserProfile(username, password, age):
    info = {"password": password, "age": age}
    ref = db.reference("/")
    ref.child("users").child(username).set(info)
    return username

# given user id, returns user info
def getUserProfile(username):
    ref = db.reference("/")
    return ref.child("users").child(username).get()

if __name__ == "__main__":
    k1 = createUserProfile("bobsmith", "", 30)
    k2 = createUserProfile("lilycarter", "", 22)
    k3 = createUserProfile("jaycarter", "", 39)
    print(getUserProfile(k3))