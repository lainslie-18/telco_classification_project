import pandas as pd
import numpy as np
import os
import env


def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''
    This function takes in user credentials from an env.py file and a database name and creates a connection to the Codeup database through a connection string 
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


telco_sql_query = '''
                select * from customers
                join contract_types using(contract_type_id)
                join internet_service_types using(internet_service_type_id)
                join payment_types using(payment_type_id)
                '''

def query_telco_data():
    '''
    This function uses the get_connection function to connect to the telco_churn database and returns the telco_sql_query read into a pandas dataframe
    '''
    return pd.read_sql(telco_sql_query,get_connection('telco_churn'))


def get_telco_data():
    '''
    This function checks for a local telco.csv file and reads it into a pandas dataframe, if it exists. If not, it uses the get_connection & query_telco_data functions to query the data and write it locally to a csv file
    '''
    # If csv file exists locallyread in data from csv file.
    if os.path.isfile('telco.csv'):
        df = pd.read_csv('telco.csv', index_col=0)
        
    else:
        
        # Query and read data from telco_churn database
        df = query_telco_data()
        
        # Cache data
        df.to_csv('telco.csv')
        
    return df