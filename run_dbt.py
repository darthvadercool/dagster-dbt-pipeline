from dagster_dbt import dbt_cli_resource, dbt_run_op,  load_assets_from_dbt_manifest, DbtCliOutput


from dagster import job
import json



my_dbt_resource = dbt_cli_resource.configured(
    {"project_dir": "/home/kshitij/Workplace/pipeline_project/dbt_data_pipe/",
     "profiles_dir": "/home/kshitij/.dbt/"}
)





@job(resource_defs={"dbt": my_dbt_resource})
def my_dbt_job():
    dbt_run_op()
    
