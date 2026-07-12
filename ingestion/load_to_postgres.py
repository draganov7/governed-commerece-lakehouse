import os
import pandas as pd

from urllib.parse import quote_plus
from dotenv import load_dotenv
from sqlalchemy import create_engine, Engine, text
from datetime import datetime, timezone
from pathlib import Path

load_dotenv()

TABLE_MAP = {
    "customers": "customers_raw",
    "orders": "orders_raw",
    "order_items": "order_items_raw",
    "order_payments": "order_payments_raw",
    "order_reviews": "order_reviews_raw",
    "products": "products_raw",
    "sellers": "sellers_raw",
    "category_translation": "category_translation_raw",
}

DATE_COLUMNS = {
    "orders": [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ],
    "order_items": [
        "shipping_limit_date",
    ],
    "order_reviews": [
        "review_creation_date",
        "review_answer_timestamp",
    ],
}

INTEGER_COLUMNS = {
    "order_items": [
        "order_item_id",
    ],
    "order_payments": [
        "payment_sequential",
        "payment_installments",
    ],
    "order_reviews": [
        "review_score",
    ],
    "products": [
        "product_name_lenght",
        "product_description_lenght",
        "product_photos_qty",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm",
    ],
}


NUMERIC_COLUMNS = {
    "order_items": [
        "price",
        "freight_value",
    ],
    "order_payments": [
        "payment_value",
    ],
}

def get_engine():
    required_variables = [
        "POSTGRES_USER",
        "POSTGRES_PASSWORD",
        "POSTGRES_HOST",
        "POSTGRES_PORT",
        "POSTGRES_DB",
        "POSTGRES_SSLMODE",
    ]

    missing_variables = [
        variable
        for variable in required_variables
        if not os.getenv(variable)
    ]

    if missing_variables:
        raise RuntimeError(f"Missing Variables: {missing_variables}")

    user     = quote_plus(os.environ["POSTGRES_USER"])
    password = quote_plus(os.environ["POSTGRES_PASSWORD"])

    url = (
        f"postgresql+psycopg2://{user}:{password}"
        f"@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}"
        f"/{os.environ['POSTGRES_DB']}"
        f"?sslmode={os.environ['POSTGRES_SSLMODE']}"
    )

    engine = create_engine(url)
    

    return engine

def clean_dataframe(
    dataset_name: str,
    dataframe: pd.DataFrame,
    file_name: str,
) -> pd.DataFrame:
    dataframe = dataframe.copy()

    for column in DATE_COLUMNS.get(dataset_name, []):
        dataframe[column] = pd.to_datetime(
            dataframe[column],
            errors="coerce",
        )

    for column in INTEGER_COLUMNS.get(dataset_name, []):
        dataframe[column] = pd.to_numeric(
            dataframe[column],
            errors="coerce",
        ).astype("Int64")

    for column in NUMERIC_COLUMNS.get(dataset_name, []):
        dataframe[column] = pd.to_numeric(
            dataframe[column],
            errors="coerce",
        )

    dataframe["ingestion_file_name"] = file_name
    dataframe["ingestion_timestamp"] = datetime.now(timezone.utc)

    return dataframe


def load_file(
    engine: Engine,
    dataset_name: str,
    file_path: Path,
) -> None:
    table_name = TABLE_MAP[dataset_name]

    print(f"Loading {file_path} into raw.{table_name}")

    dataframe = pd.read_csv(file_path)
    dataframe = clean_dataframe(
        dataset_name,
        dataframe,
        file_path.name,
    )

    with engine.begin() as connection:
        connection.execute(
            text(f"truncate table raw.{table_name}")
        )

    dataframe.to_sql(
        name=table_name,
        con=engine,
        schema="raw",
        if_exists="append",
        index=False,
        chunksize=5000,
        method="multi",
    )

    print(
        f"Loaded {len(dataframe):,} rows into raw.{table_name}"
    )


def main() -> None:
    data_directory = Path("data/raw")
    engine = get_engine()

    for dataset_name in TABLE_MAP:
        file_path = data_directory / f"{dataset_name}.csv"

        if not file_path.exists():
            raise FileNotFoundError(
                f"Missing file: {file_path}. "
                "Run download_olist.py first."
            )

        load_file(
            engine,
            dataset_name,
            file_path,
        )


if __name__ == "__main__":
    main()