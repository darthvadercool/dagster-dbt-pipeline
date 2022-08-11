
select * from {{ ref('dim_personnel_data_cleansed')}}
where percent_vax_res < 0