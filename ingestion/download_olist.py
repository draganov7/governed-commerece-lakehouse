from pathlib import Path

import requests

OLIST_FILES = {
    "customers": "https://huggingface.co/datasets/miminmoons/olist-ecommerce-for-delivery-and-review-prediction/resolve/main/data/olist_customers_dataset.csv",
    "orders": "https://huggingface.co/datasets/miminmoons/olist-ecommerce-for-delivery-and-review-prediction/resolve/main/data/olist_orders_dataset.csv",
    "order_items": "https://huggingface.co/datasets/miminmoons/olist-ecommerce-for-delivery-and-review-prediction/resolve/main/data/olist_order_items_dataset.csv",
    "order_payments": "https://huggingface.co/datasets/miminmoons/olist-ecommerce-for-delivery-and-review-prediction/resolve/main/data/olist_order_payments_dataset.csv",
    "order_reviews": "https://huggingface.co/datasets/miminmoons/olist-ecommerce-for-delivery-and-review-prediction/resolve/main/data/olist_order_reviews_dataset.csv",
    "products": "https://huggingface.co/datasets/miminmoons/olist-ecommerce-for-delivery-and-review-prediction/resolve/main/data/olist_products_dataset.csv",
    "sellers": "https://huggingface.co/datasets/miminmoons/olist-ecommerce-for-delivery-and-review-prediction/resolve/main/data/olist_sellers_dataset.csv",
    "category_translation": "https://huggingface.co/datasets/miminmoons/olist-ecommerce-for-delivery-and-review-prediction/resolve/main/data/product_category_name_translation.csv",
}


def download_file(name: str, url: str, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{name}.csv"

    response = requests.get(url, timeout=180)
    response.raise_for_status()

    output_path.write_bytes(response.content)
    return output_path


def main() -> None:
    output_dir = Path("data/raw")

    for name, url in OLIST_FILES.items():
        path = download_file(name, url, output_dir)
        print(f"Downloaded {name}: {path}")


if __name__ == "__main__":
    main() 