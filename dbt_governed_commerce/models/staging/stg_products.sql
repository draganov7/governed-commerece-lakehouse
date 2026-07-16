select 
product_id
,product_category_name
,product_name_lenght product_name_length
,product_description_lenght product_description_length
,product_photos_qty product_photos_qty
,product_weight_g
,product_length_cm
,product_height_cm
,product_width_cm
,ingestion_file_name
,ingestion_timestamp
from {{ source('raw', 'products_raw') }}