


with source as (
    select *
    from {{ source('public', 'CovidVaxProvider') }}
),

renamed as (
    
    select
        "Federal Provider Number" as provider_id,
        case 
          when "Percent Vaccinated Residents" = 'Not Available' then  '0'
          else "Percent Vaccinated Residents" 
        end as percent_vax_res,
        case 
          when "Percent Vaccinated Healthcare Personnel" = 'Not Available' then  '0'
          else "Percent Vaccinated Healthcare Personnel" 
        end as percent_vax_h_res,
        case 
          when "Percent of Fully Vaccinated Residents who Received a Booster Dose" = 'Not Available' then  '0'
          else "Percent of Fully Vaccinated Residents who Received a Booster Dose" 
        end as percent_res_with_booster,
        
        
        case 
          when "Percent of Fully Vaccinated Staff who Received a Booster Dose" = 'Not Available' then  '0'
          else "Percent of Fully Vaccinated Staff who Received a Booster Dose" 
        end as percent_h_res_with_booster,
        
        "Date vaccination data last updated" as last_updated 
        from source

)

select * from renamed




