

select * from {{ ref('analytics_quality_versus_personnel')}}
where zip_code < 0


