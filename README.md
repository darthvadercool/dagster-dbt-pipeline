# Dagster-dbt pipeline project

The project tries to utilise dagster for data orchestration techniques. It uses a locally run postgres as data warehouse connecting it to dbt and dagster. The data is ingested to postgres warehouse  using dagster ops. The dbt is used for staging, cleaning and modelling on data warehouse and storing the tranformed model in warehouse itself. Dagster is being utilised to oversee the whole process in a more systematic way.

## Installation

Clone the repository and change directory to pipeline-project/

#### create virtual environment

```bash
python3.9 -m venv env
pip install requirements.txt
```

#### postgres
make a database in local postgres with credentials as follow:
```bash
db-name - dbt_data
schema - public
user - postgres
pass - postgres
port - 5432
```

#### dbt 
change directory to /dbt_data_pipe and run the commands
```bash
export DBT_PROFILES_DIR=path/to/directory
```
by default dbt searches for profiles in /home/<user_name>/.dbt/profiles.yml
there is also a profiles.yml in dbt_data_pipe/ folder. The path to that profiles can also be set using above command.



#### dagster 
In the dagster projects, in /jobs/file_jobs.py | repository.py, change DBT_PROJECT_DIR and DBT_PROFILES_DIR to path as per the system location on your laptop. 

Also keep the csvs in dataset/ folder with names ProviderInfo.csv and CovidVaxProvider.csv. Though dagster will read and make tables accordingly but the dbt project models are wired to tables with specific names. Specify the path of csvs in ops/file_operations.py accordingly. There is a bit of hardcoding that will be updated.



## License
[MIT](https://choosealicense.com/licenses/mit/)
