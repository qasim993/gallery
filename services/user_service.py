# user_service.py
from firebase_config import db

class UserService:
    def follow_user(self, current_user_id, user_to_follow_id):
        current_user_ref = db.collection('users').document(current_user_id)
        user_to_follow_ref = db.collection('users').document(user_to_follow_id)
        
        current_user_data = current_user_ref.get().to_dict()
        user_to_follow_data = user_to_follow_ref.get().to_dict()
        
        current_user_followees = current_user_data.get('followees', [])
        user_to_follow_followers = user_to_follow_data.get('followers', [])
        
        if user_to_follow_id not in current_user_followees:
            current_user_followees.append(user_to_follow_id)
            current_user_ref.update({'followees': current_user_followees})
        
        if current_user_id not in user_to_follow_followers:
            user_to_follow_followers.append(current_user_id)
            user_to_follow_ref.update({'followers': user_to_follow_followers})
        
        return {"message": "User followed successfully"}

    def unfollow_user(self, current_user_id, user_to_unfollow_id):
        current_user_ref = db.collection('users').document(current_user_id)
        user_to_unfollow_ref = db.collection('users').document(user_to_unfollow_id)
        
        current_user_data = current_user_ref.get().to_dict()
        user_to_unfollow_data = user_to_unfollow_ref.get().to_dict()
        
        current_user_followees = current_user_data.get('followees', [])
        user_to_unfollow_followers = user_to_unfollow_data.get('followers', [])
        
        if user_to_unfollow_id in current_user_followees:
            current_user_followees.remove(user_to_unfollow_id)
            current_user_ref.update({'followees': current_user_followees})
        
        if current_user_id in user_to_unfollow_followers:
            user_to_unfollow_followers.remove(current_user_id)
            user_to_unfollow_ref.update({'followers': user_to_unfollow_followers})
        
        return {"message": "User unfollowed successfully"}
