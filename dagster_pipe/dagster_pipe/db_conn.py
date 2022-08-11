from sqlalchemy import create_engine


def get_postgres_conn():
    pwd = 'postgres'
    uid = 'postgres'
    server = 'localhost'
    db = 'dbt_data'
    port = 5432
    cs = create_engine(f'postgresql://{uid}:{pwd}@{server}:{port}/{db}')
    try:
        return cs
    except:
        print("Error loading the config file.")
