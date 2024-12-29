from firebase_config import db, bucket, bucket_name

class GalleryService:
    def create_gallery(self, username, content,file):
        # Save the image to Cloud Storage
        blob = bucket.bucket(bucket_name).blob(file.filename)
        blob.upload_from_file(file.file)
        # Save metadata (e.g., image URL) to Firestore
        image_url = f"https://storage.googleapis.com/{bucket_name}/{file.filename}"
        gall_ref = db.collection('gallery').document()
        # Set the document fields
        gall_ref.set({
            'username':username,
            'content': content,
            'filename': file.filename,
            'url': image_url
        })
        print("Gallery created successfully")
        return gall_ref.id  # Return the ID of the newly created tweet

    def edit_gallery(self, gall_id, content):
        # Update the content of the tweet with the given ID
        gall_ref = db.collection('gallery').document(gall_id)
        gall_ref.update({'content': content})

    def delete_gallery(self, gall_id):
        # Delete the tweet with the given ID
        db.collection('gallery').document(gall_id).delete()

    def view_gallery(self, user_name) -> list:
        # Assuming 'gallery' is the name of your Firestore collection
        gallery_ref = db.collection('gallery')
        query = gallery_ref.where('username', '==', user_name).get()

        # Initialize an empty list to store the matching documents
        gallery_docs = []

        for doc in query:
            gallery_docs.append(doc.to_dict())
        print (gallery_docs)

        return gallery_docs

    def get_gallery(self, gall_id) -> dict:
        # Retrieve the tweet with the given ID
        gall_ref = db.collection('gallery').document(gall_id)
        gall_doc = gall_ref.get()
        if gall_doc.exists:
            return gall_doc.to_dict()
        else:
            return None
    def get_gallery_details(self, gall_id):
        gall_ref = db.collection('gallery').document(gall_id)
        gall_data = gall_ref.get().to_dict()
        gall_name=gall_data.get('content')
        return gall_name