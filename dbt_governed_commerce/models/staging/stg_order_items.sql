select 
order_id
,order_item_id
,product_id
,seller_id
,shipping_limit_date
,price
,freight_value
,price + freight_value as item_total_value
,ingestion_file_name
,ingestion_timestamp
from {{ source('raw', 'order_items_raw') }}