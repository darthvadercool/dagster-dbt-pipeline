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
The profiles.yml has been provided in the dbt_data_pipe/config folder. If some issues occur, change directory to /dbt_data_pipe and run the commands, specifying the profiles.yml on your local machine.
```bash
export DBT_PROFILES_DIR=path/to/directory
```
by default dbt searches for profiles in /home/<user_name>/.dbt/profiles.yml




#### dagster 
DBT_PROJECT_DIR and DBT_PROFILES_DIR are required to load dbt_assets, change values of the given constants in dagster_pipe/utils/constants.py to ypur local repository loaction on laptop. 

Also keep the csvs in dataset/ folder with names ProviderInfo.csv and CovidVaxProvider.csv. Though dagster will read and make tables accordingly but the dbt project models are wired to tables with specific names. Specify the path of csvs in ops/file_operations.py accordingly. There is a bit of hardcoding that will be updated.The datasets are also given in the repo.



## License
[MIT](https://choosealicense.com/licenses/mit/)
