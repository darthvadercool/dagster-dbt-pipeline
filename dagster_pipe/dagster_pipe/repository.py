from dagster import repository

from dagster_dbt import load_assets_from_dbt_project


from dagster_pipe.jobs.dbt_transform import dbt_job
from dagster_pipe.jobs.file_jobs import print_file_job
from dagster_pipe.ops.dbt import dbt_assets






"""
dbt_assets = load_assets_from_dbt_project(project_dir = "/home/kshitij/Workplace/pipeline_project/dbt_data_pipe/",
    profiles_dir="/home/kshitij/.dbt/"
    )
    """

@repository
def dagster_pipe():
    """
    The repository definition for this dagster_pipe Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [ print_file_job]
    # schedules = [my_hourly_schedule]
    # sensors = [my_sensor]
    
    

    return jobs 
