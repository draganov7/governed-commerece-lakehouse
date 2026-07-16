select
    seller_id,
    seller_zip_code_prefix,
    lower(seller_city) as seller_city,
    upper(seller_state) as seller_state,
    ingestion_file_name,
    ingestion_timestamp
from {{ source('raw', 'sellers_raw') }}