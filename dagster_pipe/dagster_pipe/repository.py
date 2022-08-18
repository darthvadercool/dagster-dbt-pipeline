from dagster import repository, with_resources, define_asset_job


from dagster_dbt import load_assets_from_dbt_project


from dagster_pipe.jobs.dbt_transform import dbt_job, dbt_cli_resource
from dagster_pipe.jobs.file_jobs import local_job





DBT_PROJECT_DIR = "/home/kshitij/Workplace/pipeline_project/dbt_data_pipe/"
DBT_PROFILES_DIR = "/home/kshitij/.dbt/"

dbt_assets = load_assets_from_dbt_project(
    DBT_PROJECT_DIR, 
    DBT_PROFILES_DIR,
    key_prefix=["dbt_data", "public"],
    source_key_prefix=["dbt_data"],
    )

everything_job = define_asset_job("every_dbt_asset_run", selection="*")



@repository
def dagster_pipe():

    return with_resources(
        dbt_assets,
        resource_defs={"dbt": dbt_cli_resource.configured(
                {"project_dir": DBT_PROJECT_DIR, "profiles_dir": DBT_PROFILES_DIR}
            )  
        },

        ) + [local_job] +[everything_job]