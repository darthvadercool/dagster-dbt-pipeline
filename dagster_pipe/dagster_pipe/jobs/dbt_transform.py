from dagster_dbt import dbt_cli_resource, dbt_run_op, DbtCliOutput
from dagster import job,op,In,Out, Nothing

from dagster_pipe.ops.dbt import dbt_run






@op(
    ins={"source1": In(Nothing), "source2": In(Nothing)},
    required_resource_keys={"dbt"},
    out=Out(dagster_type=DbtCliOutput),
    tags={"kind": "dbt"},
)
def dbt_job():
    dbt_run_op()
