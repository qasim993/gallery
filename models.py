# models.py

from pydantic import BaseModel

class User:
    def __init__(self, username: str, email: str, dob: str, password: str):
        self.username = username
        self.email = email
        self.dob = dob
        self.password = password
        
class Login:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
