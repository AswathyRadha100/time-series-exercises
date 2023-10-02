# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
# Import the Pandas library for data manipulation
import pandas as pd

# Import the NumPy library for numerical operations
import numpy as np

# Import the 'requests' library to make HTTP requests
import requests

# Import the 'os' library for operating system-related tasks
import os

# Import credentials from an 'env.py' file 
from env import host, user, password

# -

def get_db_url(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# +



####################### grocery_df function  #########################


def get_store_data():
    '''
    Returns a dataframe of all store data in the tsa_item_demand database and saves a local copy as a csv file.
    '''
    url = get_db_url('tsa_item_demand')

    query = '''
            SELECT *
            FROM items
            JOIN sales USING(item_id)
            JOIN stores USING(store_id)
            '''

    df = pd.read_sql(query, url)
    df.to_csv('tsa_store_data.csv', index=False)
    return df


# -
def get_swapi_data(endpoint):
    """
    This function will:  
    - creates a csv of `endpoint` data if one does not exist
        - if one already exists, it uses the existing csv 
    - outputs data as a dataframe.
    
    endpoint formatting: "planets"
    
    """
    
    base_url = "https://swapi.dev/api/"
    
    if os.path.isfile(f"{endpoint}.csv"):
        df = pd.read_csv(f"{endpoint}.csv", index_col=0)
        
    else:
        response = requests.get(base_url + endpoint + "/")
        data = response.json()
        df = pd.DataFrame(data['results'])
        
        while data['next'] != None:
            print(data['next'])
            response = requests.get(data['next'])
            data = response.json()
            df = pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
        df.to_csv(f"{endpoint}.csv")
        
    return df


# +
############################## german energy function  #############################

def opsd_germany_daily():
    """
    This function uses or creates the 
    opsd_germany_daily csv and returns a df.
    """
    if os.path.isfile('opsd_germany_daily.csv'):
        df = pd.read_csv('opsd_germany_daily.csv', index_col=0)
    else:
        url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'
        df = pd.read_csv(url)
        df.to_csv('opsd_germany_daily.csv')
    return df
# -

