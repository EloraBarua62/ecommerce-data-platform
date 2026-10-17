from src.data_transformation.transformations import transform_data


BUCKET_NAME = "ecommercepipeline2026"

DATASETS = [
    {
        "name": "customers",
        "input_key": "source/customers.csv",
        "output_key": "processed/customers/customers.parquet",
    },
    {
        "name": "products",
        "input_key": "source/products.csv",
        "output_key": "processed/products/products.parquet",
    },
    {
        "name": "orders",
        "input_key": "source/orders.csv",
        "output_key": "processed/orders/orders.parquet",
    },
]


def main() -> None:
    for dataset in DATASETS:
        transform_data(
            bucket_name=BUCKET_NAME,
            input_key=dataset["input_key"],
            output_key=dataset["output_key"],
            dataset_name=dataset["name"],
        )


if __name__ == "__main__":
    main()
