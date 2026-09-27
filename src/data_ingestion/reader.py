# Read csv files
import os
import pandas as pd
from pathlib import Path

""" directory_path = "/Users/elora/Data Engineering/E_commerce Data Platform/data/sample"
file_count = len([f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))])
print(file_count)
 """
# Create 3 different df
def read_csv(file_path: str) -> pd.DataFrame:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".csv":
        raise ValueError(f"Expected a CSV file: {path}")
    return pd.read_csv(path)





