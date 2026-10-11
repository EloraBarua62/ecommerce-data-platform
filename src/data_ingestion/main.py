from src.data_ingestion.reader import read_csv

directory_path = "/Users/elora/Data Engineering/E_commerce Data Platform/data/sample"

def main() -> None:
    customers = read_csv(f"{directory_path}/customers.csv")
    orders = read_csv(f"{directory_path}/orders.csv")
    products = read_csv(f"{directory_path}/products.csv")

    print(f"Customers: {len(customers)}")
    print(f"Products: {len(products)}")
    print(f"Orders: {len(orders)}")

if __name__ == "__main__":
    main()
