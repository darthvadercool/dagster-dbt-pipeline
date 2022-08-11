

 with source as (

    select * from {{ ref('stg_providerinfo__HospitalQuality') }}

),

final as (

    select
        
        source.provider_number,
        source.provider_name,
        source.provider_address,
        source.provider_city,
        source.provider_state,
        source.zip_code,
        source.contact_number,
        source.county_code,
        source.county_name,
        source.ownership_type,
        source.overall_rating,
        source.rc1_health_score,
        source.rc2_health_score,
        source.rc3_health_score,
        source.total_health_score,
        source.total_penalties,
        source.location,
        source.processing_date
        from source


)

select * from final