with source as (

    select * from {{ ref('stg_covidvaxprovider__PersonnelVaxData') }}

),

final as (

    select
        
        source.provider_id,
        cast(source.percent_vax_res as double precision),
        cast(source.percent_vax_h_res as double precision),
        cast(source.percent_res_with_booster as double precision),
        cast(source.percent_h_res_with_booster as double precision),
        source.last_updated
        from source
)

select * from final
