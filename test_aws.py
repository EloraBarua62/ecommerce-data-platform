import os
from dotenv import load_dotenv

load_dotenv()

access_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_DEFAULT_REGION")

print("Access key loaded:", bool(access_key))
print("Secret key loaded:", bool(secret_key))
print("Region:", region)