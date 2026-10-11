from pathlib import Path
from src.raw_storage.s3_client import get_s3_client

def upload_file(file_path: str, bucket_name: str, s3_key: str) -> None:
    path = Path(file_path)

    if not path.exists():
       raise FileNotFoundError(f"file not found: {file_path}")

    s3_client = get_s3_client()

    s3_client.upload_file(path, bucket_name, s3_key)

    print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_key}")
     