import os
import boto3
from dotenv import load_dotenv

load_dotenv()

# Create a client using access keys
def get_s3_client():
    return boto3.client(
        "s3",
        region_name="eu-west-1"
    )

""" response = s3.list_buckets()
print(response)

for bucket in response["Buckets"]:
    print(bucket["Name"]) """
#s3 = session.resource('s3')
#for bucket in s3.buckets.all():
 #   print(bucket.name)