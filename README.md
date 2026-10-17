# E-commerce Data Pipeline

## Overview

A Python-based data pipeline that ingests e-commerce CSV datasets, stores raw data in Amazon S3, transforms the data, and saves the processed datasets in Parquet format.

This project demonstrates basic data engineering practices, including modular pipeline stages, data validation, duplicate removal, cloud storage, and Git-based development.

## Architecture

```text
Local CSV files
      |
      v
Data ingestion
      |
      v
Raw CSV files in Amazon S3
      |
      v
Data transformation
      |
      +--> Validate required columns
      +--> Check for empty datasets
      +--> Remove duplicate rows
      +--> Convert CSV to Parquet
      |
      v
Processed Parquet files in Amazon S3
```

## Datasets

The pipeline processes three datasets:

- `customers.csv`
- `products.csv`
- `orders.csv`

## Technologies

- Python
- pandas
- boto3
- Amazon S3
- s3fs
- PyArrow / Parquet
- python-dotenv
- Git and GitHub

## Project Structure

```text
.
├── main.py
├── data/
│   └── sample/
├── src/
│   ├── data_ingestion/
│   ├── raw_storage/
│   └── data_transformation/
├── requirements.txt
└── .gitignore
```

## Prerequisites

- Python 3
- An AWS account with access to an S3 bucket
- AWS credentials configured locally
- The sample CSV files in `data/sample/`

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure AWS credentials locally. The pipeline uses the S3 bucket `ecommercepipeline2026` in the `eu-west-1` region. Ensure your AWS identity has the required permissions to read and write the relevant objects.

Do not commit AWS credentials or your `.env` file to GitHub.

## Run the Pipeline

From the project root, run:

```bash
python main.py
```

The pipeline runs the following stages in order:

1. Read the local CSV datasets and print their row counts.
2. Upload the raw CSV files to S3.
3. Validate and transform each dataset.
4. Save the transformed datasets as Parquet files in S3.
5. Verify that each processed object exists.

## S3 Output Locations

Raw datasets:

- `source/customers.csv`
- `source/products.csv`
- `source/orders.csv`

Processed datasets:

- `processed/customers/customers.parquet`
- `processed/products/products.parquet`
- `processed/orders/orders.parquet`

## Validation

The transformation stage checks for empty datasets and missing required columns, removes duplicate rows, writes Parquet outputs, and verifies that the output objects exist in S3.

## Future Improvements

- Add automated unit tests.
- Improve handling of unchanged or previously processed data.
- Add structured logging and clearer error handling.
- Improve configuration and remove machine-specific file paths.
- Document the pipeline with additional examples.
