select
c.customer_unique_id
,min(c.customer_state) as customer_state
,min(c.customer_city) as customer_city
,count(distinct f.order_id) as total_orders
,coalesce(sum(f.total_payment_value), 0) as lifetime_value
,avg(f.average_review_score) as average_review_score
,max(f.order_date) as last_order_date
,case
    when count(distinct f.order_id) > 1 then true
    else false
end as is_repeat_customer
from {{ ref('dim_customers') }} c
left join {{ ref('fct_orders') }} f on c.customer_id = f.customer_id
group by c.customer_unique_id