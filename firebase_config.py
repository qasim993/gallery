from google.cloud import datastore, firestore, storage

# Initialize Datastore client
#db = datastore.Client()
db = firestore.Client()

bucket_name = "gallery-bucket-99"
bucket = storage.Client()

