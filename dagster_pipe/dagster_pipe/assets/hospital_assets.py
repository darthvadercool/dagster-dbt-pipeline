import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import os
import glob
import logging



from dagster_pipe.db_conn import get_postgres_conn
from dagster import asset




@asset(compute_kind='python')
def ProviderInfo():
	
    path = r'/home/kshitij/Downloads/dataset/ProviderInfo.csv'
    

   # all_files = glob.glob(path + "/*.csv")
    
 
    files =  path
    print (files)
    x = (os.path.basename(files))
    try:
        lgr = logging.getLogger('console_logger')
        df = pd.read_csv(files, sep=',', encoding='cp1252').replace(to_replace='null', value=np.NaN)
        
        lgr.error(df)
    except Exception as e:
        print("Data extract error: " + str(e))          	
    print ("kshitij1")
    try:
        
        engine = get_postgres_conn()
        lgr.info(df.head())
        print ("kshitij3")
        df.to_sql(x[:-4], engine, schema='public', index=False, if_exists='replace')
        print ("kshitij4")
        #print (x[:-4])
        #context.log.info(df.head())
        lgr.error(df.head())
        #context.log.info("Data ingestion successful")
    except Exception as e:    
        print("Data load error: " + str(e))
        lgr.error(str(e))
    
	  
	    
@asset(compute_kind='python')
def CovidVaxProvider():
    
    path = r'/home/kshitij/Downloads/dataset/CovidVaxProvider.csv'
 #   engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/dbt_data')
 #   all_files = glob.glob(path + "/*.csv")
    
 
    files =  path
    print (files)
    x = (os.path.basename(files))
    try:
        lgr = logging.getLogger('console_logger')
        df = pd.read_csv(files, sep=',', encoding='cp1252').replace(to_replace='null', value=np.NaN)
        lgr.error(df)
    except Exception as e:
        print("Data extract error: " + str(e))              
    
    try:
        engine = get_postgres_conn()
        df.to_sql(x[:-4], engine, schema='public',index=False,  if_exists='replace')
        print ("data ingestion")
        #print (x[:-4])
        #context.log.info(df.head())
        lgr.error(df.head())
        #context.log.info("Data ingestion successful")
    except Exception as e:    
        print("Data load error: " + str(e))
        lgr.error(str(e))
    
	
	

