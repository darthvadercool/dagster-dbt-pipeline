
select * from {{ ref('dim_hospital_quality_cleansed')}}
where total_penalties < 0