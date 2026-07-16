select 
lower(product_category_name) product_category_name
,lower(product_category_name_english) product_category_name_english
,ingestion_file_name
,ingestion_timestamp
from {{ source('raw', 'category_translation_raw') }}