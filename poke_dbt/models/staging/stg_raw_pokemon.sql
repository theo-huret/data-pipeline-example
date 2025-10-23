with raw as (
    select *
    from poke_bronze.pokemon
)

select
    id,
    name,
    height,
    weight,
    base_experience,
    types_csv,
    abilities_csv
from raw
