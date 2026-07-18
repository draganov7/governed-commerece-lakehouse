with orders as (

select 
*
from {{ ref('stg_orders') }}

),

items as (
    
select
order_id
,count(*) as item_count
,sum(price) as gross_revenue
,sum(freight_value) as freight_revenue
,sum(item_total_value) as order_total_value
from {{ ref('stg_order_items') }}
group by order_id

),

payments as (

select
order_id
,sum(payment_value) as total_payment_value
,count(*) as payment_event_count
from {{ ref('stg_order_payments') }}
group by order_id

),

reviews as (

select
order_id
,avg(review_score)::numeric(10, 2) as average_review_score
,count(*) as review_count
from {{ ref('stg_order_reviews') }}
group by order_id

)

select
o.order_id
,o.customer_id
,o.order_status
,o.order_purchase_timestamp::date as order_date
,o.order_purchase_timestamp
,o.order_delivered_customer_date
,o.order_estimated_delivery_date
,o.is_late_delivery
,o.delivery_days
,coalesce(i.item_count, 0) as item_count
,coalesce(i.gross_revenue, 0) as gross_revenue
,coalesce(i.freight_revenue, 0) as freight_revenue
,coalesce(i.order_total_value, 0) as order_total_value
,coalesce(p.total_payment_value, 0) as total_payment_value
,coalesce(p.payment_event_count, 0) as payment_event_count
,r.average_review_score
,coalesce(r.review_count, 0) as review_count
from orders o 
left join items i on o.order_id = i.order_id
left join payments p on o.order_id = p.order_id
left join reviews r on o.order_id = r.order_id