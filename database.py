import firebase_admin
from firebase_admin import db
import json

KEY_PATH = 'privateKey/volunteerapp-1dc3a-firebase-adminsdk-2ntz8-d21784bfbf.json'
DB_URL = 'https://volunteerapp-1dc3a-default-rtdb.firebaseio.com/'
cred_obj = firebase_admin.credentials.Certificate(KEY_PATH)
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': DB_URL})

def writeToDb():
    with open("test.json", "r") as f:
        file_contents = json.load(f)
    ref = db.reference("/")
    ref.set(file_contents)

if __name__ == "__main__":
    writeToDb()