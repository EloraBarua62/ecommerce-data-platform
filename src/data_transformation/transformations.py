import pandas as pd
import boto3
from dotenv import load_dotenv

load_dotenv()

REQUIRED_COLUMNS = {
    "customers": ["customer_id", "name", "country", "signup_date"],
    "products": ["product_id", "product_name", "category", "price"],
    "orders": ["order_id", "customer_id", "product_id", "quantity", "order_date"],
}


def transform_data(
    bucket_name: str,
    input_key: str,
    output_key: str,
    dataset_name: str,
) -> None:
    """Validate, deduplicate, and save a dataset as Parquet in S3."""

    input_path = f"s3://{bucket_name}/{input_key}"
    output_path = f"s3://{bucket_name}/{output_key}"

    if dataset_name not in REQUIRED_COLUMNS:
        raise ValueError(f"Unknown dataset: {dataset_name}")

    data = pd.read_csv(input_path)

    # Validate that the dataset contains records
    if data.empty:
        raise ValueError(f"{dataset_name} dataset is empty")

    # Validate required columns
    missing_columns = set(REQUIRED_COLUMNS[dataset_name]) - set(data.columns)

    if missing_columns:
        raise ValueError(
            f"{dataset_name} is missing required columns: "
            f"{sorted(missing_columns)}"
        )

    rows_before = len(data)
    data = data.drop_duplicates()
    rows_removed = rows_before - len(data)
    print(f"Dataset: {dataset_name}")
    print(f"Rows read: {rows_before}")
    print(f"Duplicate rows removed: {rows_removed}")


    # Store parquet data
    data.to_parquet(output_path, index=False)
    print(f"Saved to: {output_path}")

    s3  = boto3.client("s3", region_name="eu-west-1")
    s3.head_object(Bucket=bucket_name, Key=output_key)
    print(f"Validation passed: s3://{bucket_name}/{output_key} exists")
    

    