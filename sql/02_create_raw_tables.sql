create table if not exists raw.customers_raw (
    customer_id text,
    customer_unique_id text,
    customer_zip_code_prefix text,
    customer_city text,
    customer_state text,
    ingestion_file_name text,
    ingestion_timestamp timestamp
);

create table if not exists raw.orders_raw (
    order_id text,
    customer_id text,
    order_status text,
    order_purchase_timestamp timestamp,
    order_approved_at timestamp,
    order_delivered_carrier_date timestamp,
    order_delivered_customer_date timestamp,
    order_estimated_delivery_date timestamp,
    ingestion_file_name text,
    ingestion_timestamp timestamp
);

create table if not exists raw.order_items_raw (
    order_id text,
    order_item_id int,
    product_id text,
    seller_id text,
    shipping_limit_date timestamp,
    price numeric(12,2),
    freight_value numeric(12,2),
    ingestion_file_name text,
    ingestion_timestamp timestamp
);

create table if not exists raw.order_payments_raw (
    order_id text,
    payment_sequential int,
    payment_type text,
    payment_installments int,
    payment_value numeric(12,2),
    ingestion_file_name text,
    ingestion_timestamp timestamp
);

create table if not exists raw.order_reviews_raw (
    review_id text,
    order_id text,
    review_score int,
    review_comment_title text,
    review_comment_message text,
    review_creation_date timestamp,
    review_answer_timestamp timestamp,
    ingestion_file_name text,
    ingestion_timestamp timestamp
);

create table if not exists raw.products_raw (
    product_id text,
    product_category_name text,
    product_name_lenght int,
    product_description_lenght int,
    product_photos_qty int,
    product_weight_g int,
    product_length_cm int,
    product_height_cm int,
    product_width_cm int,
    ingestion_file_name text,
    ingestion_timestamp timestamp
);

create table if not exists raw.sellers_raw (
    seller_id text,
    seller_zip_code_prefix text,
    seller_city text,
    seller_state text,
    ingestion_file_name text,
    ingestion_timestamp timestamp
);

create table if not exists raw.category_translation_raw (
    product_category_name text,
    product_category_name_english text,
    ingestion_file_name text,
    ingestion_timestamp timestamp
);