import os

PORT = os.environ.get("PORT", 8080)

BUCKET_NAME = os.environ.get("BUCKET_NAME", "latihan-cloud-bucket")

BUCKET_FOLDER = os.environ.get("BUCKET_FOLDER", "ml_model/")
