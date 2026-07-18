select
order_date
,count(*) as total_orders
,sum(case
        when order_status = 'delivered' then 1
        else 0
    end) as delivered_orders
,sum(case
        when is_late_delivery then 1
        else 0
    end) as late_orders
,avg(delivery_days) as average_delivery_days
,sum(case
        when is_late_delivery then 1
        else 0
    end)::numeric / nullif(count(*), 0) as late_delivery_rate
from {{ ref('fct_orders') }}
group by order_date