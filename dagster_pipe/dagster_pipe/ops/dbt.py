from dagster import  Output, op, AssetMaterialization, repository, AssetKey, Nothing, Out

from dagster_dbt import load_assets_from_dbt_project, dbt_run_op
from dagster_dbt.utils import generate_materializations
import json



dbt_assets = load_assets_from_dbt_project(project_dir = "/home/kshitij/Workplace/pipeline_project/dbt_data_pipe/",
    profiles_dir="/home/kshitij/.dbt/"
    )


@op(out=Out(Nothing),required_resource_keys={"dbt"})
def dbt_run(context):
    dbt_output = context.resources.dbt.run()
    


    x = dbt_output.result['results']
    a= x[1]

    print (a['unique_id'])

    print (len(x))
    print (x[1])



    #iterate over results_json
    # print (dbt_output.result['results'])
    # for keys in dbt_output.result['results']:
    #     print (keys)
    i=0
    for keys in x:
        print (keys)
        # yield AssetMaterialization(
        # asset_key=AssetKey('x[i].['unique_id']')
        
        # )
        # i = i+1
        
   
    return Nothing

    


    # print (dbt_assets)
    # [<dagster.core.definitions.assets.AssetsDefinition object at 0x7fef1cacd310>]
    
    # returning class object of above used for using dbt models reference in python, most likely



    #print (dbt_output.logs)
    # with open("dbt_output_logs.json", "w") as outfile:
    #     json.dump(dbt_output.logs, outfile)

    



    # print (dbt_output.result)
    # with open("dbt_output_result.json", "w") as outfile:
    #     json.dump(dbt_output.result, outfile)
	




@op(required_resource_keys={"dbt"})
def dag_dbt_test(context, _dbt_output):
    context.resources.dbt.test()

