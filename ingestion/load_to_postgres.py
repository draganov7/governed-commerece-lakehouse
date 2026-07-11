from dotenv import load_dotenv

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

