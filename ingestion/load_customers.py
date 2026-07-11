import os
import pandas as pd

from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime, timezone
from sqlalchemy import create_engine, text

load_dotenv()

def get_database_url() -> str:
    return(
        f"postgresql+psycopg2://"
        f"{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}"
        f"@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}"
        f"/{os.environ['POSTGRES_DB']}"
        f"?sslmode={os.environ['POSTGRES_SSLMODE']}"
    )

def main() -> None:
    file_path = Path("data/raw/customers.csv")

    if not file_path.exists():
        raise FileNotFoundError(f"File: {file_path} not found!!!")

    df = pd.read_csv(
        file_path
        ,dtype={
            "customer_id": "string",
            "customer_unique_id": "string",
            "customer_zip_code_prefix": "string",
            "customer_city": "string",
            "customer_state": "string",
        }
    )

    print(df.head())

    df["ingestion_file_name"] = file_path.name
    df["ingestion_timestamp"] = datetime.now(timezone.utc)

    engine = create_engine(get_database_url())

    with engine.connect() as conn:
        conn.execute(text("truncate table raw.customers_raw"))
    
    df.to_sql(
        name="customers_raw",
        con=engine,
        schema="raw",
        if_exists="append",
        index=False,
        chunksize=5000,
        method="multi",
    )

    print(f"Loaded {len(df)} rows to raw.customers_raw.")

if __name__ == "__main__":
    main()