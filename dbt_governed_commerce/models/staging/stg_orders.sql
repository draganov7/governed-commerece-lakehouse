select
    order_id,
    customer_id,
    lower(order_status) as order_status,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date,
    case
        when order_delivered_customer_date is not null
         and order_estimated_delivery_date is not null
         and order_delivered_customer_date > order_estimated_delivery_date
        then true
        else false
    end as is_late_delivery,
    extract(
        day from (
            order_delivered_customer_date
            - order_purchase_timestamp
        )
    )::int as delivery_days,
    ingestion_file_name,
    ingestion_timestamp
from {{ source('raw', 'orders_raw') }}