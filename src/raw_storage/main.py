import os
from src.raw_storage.uploader import upload_file

local_folder_path = '/Users/elora/Data Engineering/E_commerce Data Platform/data/sample/'
bucket_name = 'ecommercepipeline2026'
s3_key = 'source/customers.csv'

def main() -> None:
    files_to_upload = ['customers.csv', 'orders.csv', 'products.csv']

    for file_name in files_to_upload:
        file_path = os.path.join(local_folder_path, file_name)

        upload_file(
            file_path=file_path,
            bucket_name=bucket_name,
            s3_key=f'source/{file_name}'
        )

if __name__ == "__main__":
    main()