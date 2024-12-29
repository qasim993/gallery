# user_controller.py

from services.user_service import UserService

class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def follow_user(self, current_user_id: int, user_to_follow_id: int):
        try:
            return await self.user_service.follow_user(current_user_id, user_to_follow_id)
        except Exception as e:
            # Handle any exceptions or errors
            raise e

    async def unfollow_user(self, current_user_id: int, user_to_unfollow_id: int):
        try:
            return await self.user_service.unfollow_user(current_user_id, user_to_unfollow_id)
        except Exception as e:
            # Handle any exceptions or errors
            raise e
