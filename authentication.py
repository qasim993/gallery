# authentication.py

from firebase_config import db

def register(username, email, dob, password):
    user_ref = db.collection('users').document(email)
    if not user_ref.get().exists:
        user_data={
            'username': username, 'email': email, 'dob': dob, 'password': password
        }
        db.collection('users').document(email).set(user_data)
    else:
        print("User already exist")

    #user_ref.set({'username': username, 'email': email, 'dob': dob, 'password': password})

def login(email, password):
    user_ref = db.collection('users').document(email)
    user_data = user_ref.get()
    if user_data.exists and user_data.to_dict()['password'] == password:
        return True
    else:
        return False

