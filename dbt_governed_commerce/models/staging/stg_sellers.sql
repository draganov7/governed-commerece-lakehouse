select 
seller_id
,
from {{ source('raw', 'sellers_raw') }}