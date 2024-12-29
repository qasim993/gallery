from firebase_config import db as firebase_db
from fastapi import HTTPException
from authentication import register as auth_register, login as auth_login

class AuthService:
    def register_user(self,username: str, email: str, dob: str, password: str):
        """
        Service method to register a new user.

        Args:
            email (str): User's email address.
            password (str): User's password.
            username (str): User's username.
            dob (str): User's date of birth.

        Returns:
            dict: A dictionary containing a success message.
        """
        try:
            # Register the user
            print("services")
            auth_register(username, email, dob, password)

            # Save user data to Firestore database
            user_ref = firebase_db.collection("users").document(email)
            user_ref.set({
                "username": username,
                "email": email,
                "dob": dob,
                "password": password
            })

            return {"message": "User registered successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def login_user(self, email: str, password: str):
        """
        Service method to authenticate a user.

        Args:
            email (str): User's email address.
            password (str): User's password.

        Returns:
            dict: A dictionary containing a success message if login is successful,
                  otherwise raises an HTTPException.
        """
        try:
            # Login the user
            authen_user=auth_login(email, password)
            user_ref = firebase_db.collection("users").document(email)
            user_data = user_ref.get()
            if user_data.exists:
                username = user_data.get("username")
            if authen_user:
                return {"user":username}
            else:
                raise HTTPException(status_code=401, detail="Invalid credentials")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
