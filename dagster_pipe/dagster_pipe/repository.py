from dagster import repository, with_resources, define_asset_job, load_assets_from_package_module


from dagster_dbt import load_assets_from_dbt_project


from .jobs.dbt_transform import dbt_job, dbt_cli_resource
from .jobs.file_jobs import local_job
from . import assets
from .utils.constants import DBT_CONFIG, DBT_PROJECT_DIR, DBT_PROFILES_DIR





dbt_assets = load_assets_from_dbt_project(
    DBT_PROJECT_DIR, 
    DBT_PROFILES_DIR,
    key_prefix=["dbt_data", "public"],
    source_key_prefix=["dbt_data"],
    )

raw_data_assets = load_assets_from_package_module(
    assets,
    group_name="raw_data",
    key_prefix=["dbt_data", "public"],
  
)

everything_job = define_asset_job("every_dbt_asset_run", selection="*")



@repository
def dagster_pipe():

    return with_resources(
        dbt_assets + raw_data_assets,
        resource_defs={"dbt": dbt_cli_resource.configured(DBT_CONFIG)  
        },

        ) + [local_job] +[everything_job]