# user_service.py
from firebase_config import db


class UserGalleryService:
    def create_user(self, current_user_id):
        user_ref = db.collection("users").document(current_user_id)
        user_ref.set(user.dict())

