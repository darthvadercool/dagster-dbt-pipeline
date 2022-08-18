from dagster import job, graph

from dagster_dbt import dbt_run_op, dbt_cli_resource


from dagster_pipe.ops.file_operations import get_csv_path, get_tablename
from dagster_pipe.ops.ingest import fetch_data, ingest_data_to_postgres
from dagster_pipe.jobs.dbt_transform import dbt_job
from dagster_pipe.ops.dbt import dbt_run



my_dbt_resource = dbt_cli_resource.configured(
    {"project_dir": "/home/kshitij/Workplace/pipeline_project/dbt_data_pipe/",
     "profiles_dir": "/home/kshitij/.dbt/"}
)



@graph
def print_file_job():
	path1, path2 = get_csv_path()
	tablename1, tablename2 = get_tablename()
	df1 = fetch_data.alias("csv1_data")(path1)
	df2 = fetch_data.alias("csv2_data")(path2)
	loaded1 = ingest_data_to_postgres.alias("ingest_file_1")(df1, tablename1)
	loaded2 = ingest_data_to_postgres.alias("ingest_file_2")(df2, tablename2)
	dbt_run(source1=loaded1, source2=loaded2)


local_job = print_file_job.to_job(resource_defs={"dbt": my_dbt_resource})


# @job(resource_defs={"dbt": my_dbt_resource})
# def trial_dbt():
# 	dbt_run()
