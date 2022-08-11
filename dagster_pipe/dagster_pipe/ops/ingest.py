import numpy as np
import pandas as pd
from pandas import DataFrame
from dagster import op, Out, Output, In
import logging
from dagster_pipe.db_conn import get_postgres_conn



@op(ins={"filepath": In(str)}, out={"df": Out(is_required=True)})
def fetch_data(context, filepath):
    try:
        lgr = logging.getLogger('console_logger')

        df = pd.read_csv(filepath, sep=',', encoding='cp1252').replace(to_replace='null', value=np.NaN)
        context.log.info(df.head())
        lgr.error(df)
        return df

    except Exception as e:
        print("Data extract error: " + str(e))


# load data to postgres

@op(ins={"df": In(DataFrame), "tablename": In(str)})
def ingest_data_to_postgres(context, df: DataFrame, tablename):
    try:
        lgr = logging.getLogger("console_logger")
        context.log.info(tablename)
        context.log.info(df.head())
        lgr.error(df.head())

        engine = get_postgres_conn()
        context.log.info(engine)

        df.to_sql(tablename, engine, if_exists='replace', index=False, schema="public")
        context.log.info("Data ingestion successful")
    except Exception as e:
        print("Data load error: " + str(e))
        lgr.error(str(e))