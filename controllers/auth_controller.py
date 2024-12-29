# controllers/auth_controller.py

from fastapi import HTTPException
from services.auth_service import AuthService

class AuthController:
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service

    def register_user(self, username: str, email: str, dob: str, password: str):
        """
        Controller method to register a new user.

        Args:
            email (str): User's email address.
            password (str): User's password.
            
        Returns:
            dict: A dictionary containing a success message.
        """
        try:
            print ("controller")
            return self.auth_service.register_user(username, email, dob, password)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def login_user(self, email: str, password: str):
        """
        Controller method to authenticate a user.

        Args:
            email (str): User's email address.
            password (str): User's password.
            
        Returns:
            dict: A dictionary containing a success message if login is successful,
                  otherwise raises an HTTPException.
        """
        try:
            return self.auth_service.login_user(email, password)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
