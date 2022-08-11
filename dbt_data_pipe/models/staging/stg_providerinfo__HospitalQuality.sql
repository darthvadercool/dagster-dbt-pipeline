

with source as (
    select *
    from {{ source('public', 'ProviderInfo') }}
),

renamed as (
    
    select
        "Federal Provider Number" as provider_number,
        "Provider Name" as provider_name,
        "Provider Address" as provider_address,
        "Provider City" as provider_city,
        "Provider State" as provider_state,
        "Provider Zip Code" as zip_code,
        "Provider Phone Number" as contact_number,
        "Provider SSA County Code" as county_code,
        "Provider County Name" as county_name,
        "Ownership Type" as ownership_type,
        "Overall Rating" as overall_rating, 
        "Rating Cycle 1 Total Health Score" as rc1_health_score,
        "Rating Cycle 2 Total Health Score" as rc2_health_score,
        "Rating Cycle 3 Total Health Score" as rc3_health_score,
        "Total Weighted Health Survey Score" as total_health_score,
        "Total Number of Penalties" as total_penalties,
        "Location" as location,
        "Processing Date" as processing_date
        
        from source

)

select * from renamed


