from services.gallery_service import GalleryService

class GalleryController:
    def __init__(self):
        self.gallery_service = GalleryService()

    def create_gallery(self, username, content, file):
        return self.gallery_service.create_gallery(username, content,file)

    def view_gallery(self, user_name):
        return self.gallery_service.view_gallery(user_name)
    def edit_gallery(self, gall_id, content):
        return self.gallery_service.edit_gallery(gall_id, content)

    def delete_gallery(self, gall_id):
        return self.gallery_service.delete_gallery(gall_id)

    def get_gallery(self, gall_id):
        return self.gallery_service.get_gallery(gall_id)
