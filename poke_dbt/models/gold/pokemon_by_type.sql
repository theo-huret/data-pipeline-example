with stg as (
    select id, name, string_to_array(nullif(types_csv,''), ',') as types
    from {{ ref('stg_raw_pokemon') }}
),
     exploded as (
         select id, name, unnest(types) as type
         from stg
     )
select
    type,
    count(*) as pokemon_count,
    min(id) as min_id,
    max(id) as max_id
from exploded
group by type
order by pokemon_count desc