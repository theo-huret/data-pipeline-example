with stg as (
    select * from {{ ref('stg_raw_pokemon') }}
)
select
    id,
    name,
    height,
    weight,
    base_experience,
    string_to_array(nullif(types_csv,''), ',') as types,
    string_to_array(nullif(abilities_csv,''), ',') as abilities
from stg
order by id