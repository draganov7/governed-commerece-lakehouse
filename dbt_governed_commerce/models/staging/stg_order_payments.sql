select 
order_id
,payment_sequential
,lower(payment_type) payment_type
,payment_installments
,payment_value
,ingestion_file_name
,ingestion_timestamp
from {{ source('raw', 'order_payments_raw') }}