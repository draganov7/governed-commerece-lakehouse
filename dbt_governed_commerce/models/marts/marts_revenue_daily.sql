select
order_date
,count(distinct order_id) as total_orders
,count(distinct customer_id) as unique_customers
,sum(gross_revenue) as gross_revenue
,sum(freight_revenue) as freight_revenue
,sum(total_payment_value) as total_payment_value
,avg(total_payment_value) as average_order_value
from {{ ref('fct_orders') }}
group by order_date