select
    p.product_id,
    p.product_category_name,
    coalesce(
        t.product_category_name_english,
        p.product_category_name
    ) as product_category_name_english,
    p.product_name_lenght as product_name_length,
    p.product_description_lenght as product_description_length,
    p.product_photos_qty,
    p.product_weight_g,
    p.product_length_cm,
    p.product_height_cm,
    p.product_width_cm,
    p.ingestion_file_name,
    p.ingestion_timestamp
from {{ source('raw', 'products_raw') }} as p
left join {{ source('raw', 'category_translation_raw') }} as t
    on p.product_category_name = t.product_category_name