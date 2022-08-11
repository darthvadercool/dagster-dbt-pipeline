from dagster_dbt import dbt_cli_resource, dbt_run_op, DbtCliOutput
from dagster import job,op,In,Out, Nothing

from dagster_pipe.ops.dbt import dbt_run




my_dbt_resource = dbt_cli_resource.configured(
    {"project_dir": "/home/kshitij/Workplace/pipeline_project/dbt_data_pipe/",
     "profiles_dir": "/home/kshitij/.dbt/"}
)

@op(
    ins={"source1": In(Nothing), "source2": In(Nothing)},
    required_resource_keys={"dbt"},
    out=Out(dagster_type=DbtCliOutput),
    tags={"kind": "dbt"},
)
def dbt_job():
    dbt_run_op()
