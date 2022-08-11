with personnel as (

    select * from {{ ref('dim_personnel_data_cleansed') }}

),

hospitalquality as (

    select * from {{ ref('dim_hospital_quality_cleansed') }}

),

final as (

    select
        
        hospitalquality.provider_number,
        hospitalquality.provider_name,
        hospitalquality.provider_address,
        hospitalquality.provider_city,
        hospitalquality.provider_state,
        hospitalquality.zip_code,
        hospitalquality.contact_number,
        hospitalquality.county_code,
        hospitalquality.county_name,
        hospitalquality.ownership_type,
        hospitalquality.overall_rating,
        hospitalquality.rc1_health_score,
        hospitalquality.rc2_health_score,
        hospitalquality.rc3_health_score,
        hospitalquality.total_health_score,
        hospitalquality.total_penalties,
        hospitalquality.location,
        personnel.percent_vax_res,
        personnel.percent_vax_h_res,
        personnel.percent_res_with_booster,
        personnel.percent_h_res_with_booster

        from hospitalquality
    left join personnel 
        on hospitalquality.provider_number = personnel.provider_id
)

select * from final