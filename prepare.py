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

#Import visualizations
import matplotlib.pyplot as plt
import seaborn as sns

# Import custom library 
import acquire
# Import the 'os' library for operating system-related tasks
import os


#datetime utilities
from datetime import timedelta, datetime


# +
################################### Prep Store Function #################################

def prep_store_data():
    '''
    This function takes in a df and changes date dtypes, resets date as index,
    creates new columns for month, weekday, and total sales
    and returns that as a new pandas dataframe
    '''

    #assign variable df from the acquire function
    df= acquire.get_store_data()

    #change data type on sale_date
    df.sale_date = df.sale_date.astype('datetime64[ns]')
    #set the index to sale_date
    df = df.set_index('sale_date').sort_index()

    #create new colum for month
    df['month'] = df.index.month_name()
    #create new colum for weekday
    df['day_of_week'] = df.index.day_name()
    #create new colum for sale total
    df['sales_total'] = df.sale_amount * df.item_price

    return df



# +
########################## Prep Germany Function ##########################

def prep_germany_data():
    '''
    This function takes in a df and changes date dtypes, resets date as index,
    creates new columns for month, weekday, and total sales
    and returns that as a new pandas dataframe
    '''

    #assign variable df from the acquire function
    df= acquire.get_germany_data()

    #change data type on Date
    df.Date = df.Date.astype('datetime64[ns]')
    #set the index to Date
    df = df.set_index('Date').sort_index()
    #rename columns
    df = df.rename(columns={'Consumption':'consumption', 'Wind':'wind', 'Solar':'solar','Wind+Solar':'wind_solar'})

    #create new colum for month
    df['month'] = df.index.month_name()
    #create new colum for weekday
    df['day_of_week'] = df.index.day_name()
    #create new column for year
    df['year'] = df.index.year
    #fill nulls with 0
    df = df.fillna(0)

    return df


# +
########################## Prep Saas Data Function ##########################

def prep_saas_data():
    '''
    This function takes in a df and changes date dtypes, resets date as index,
    creates new columns for month, weekday, and total sales
    and returns that as a new pandas dataframe
    '''

    #assign variable df from the acquire function
    df= pd.read_csv('saas.csv')

    #rename columns by lowercasing them all
    df.columns = [col.lower() for col in df]

    #change data type on Date
    df.month_invoiced = df.month_invoiced.astype('datetime64[ns]')
    #set the index to Date
    df = df.set_index('month_invoiced').sort_index()
    #change amount from float to int
    df.amount = df.amount.astype(int)
    #change sub type from float to int
    df.subscription_type = df.subscription_type.astype(int)

    #create new colum for month
    df['month'] = df.index.month_name()
    #create new colum for weekday
    df['day_of_week'] = df.index.day_name()
    #create new column for year
    df['year'] = df.index.year

    return df


# +
########################### Convert to Datetime Function #######################

def convert_to_datetime(df):
    '''
    This function takes in a dataframe
    and converts the sales_date column to a datetime
    '''
    df.sale_date = pd.to_datetime(df.sale_date, infer_datetime_format=True)
    return df



# +
########################### Plot Distributions Function #########################

def plot_distributions(df):
    for col in list(df.columns.drop('Date')):
        plt.figure()
        sns.histplot(df[col])
        plt.title('Distribution of {}'.format(col))
# -





# +
#def prepare_store(df):
#    """
#    Prepares a sales DataFrame for analysis by:
#    1. Converting sale dates to datetime format.
#    2. Setting the datetime as the index.
#    3. Extracting the month and day of the week.
#    4. Calculating the total sales for each transaction.

#    Args:
#        df (DataFrame): The input sales DataFrame.

#    Returns:
#        DataFrame: The prepared DataFrame.
#    """
#    # Convert the sale date into a datetime
#    df.sale_date = pd.to_datetime(df.sale_date, format='%Y-%m-%d')
#    #df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y')
#    # Set the index as the new datetime value
#    df = df.set_index('sale_date')
#    # Extract the month value (name of month)
#    df['month'] = df.index.strftime('%B')
#    # Extract the day of the week from the date
#    df['day of the week'] = df.index.day_name()
#    # Calculate the total sales
#    df['sales_total'] = df.sale_amount * df.item_price
#    return df

# +
#def prep_germany_data(df):
#    '''
#    Takes in a dataframe, coverts Date to DateTime format and makes it the index, produces histograms 
#    of all variables, renames "Wind+Solar" to the more python-friendly "WindSolar", fills the abundant 
#    nulls/NaNs with 0, and adds the columns 'month' and 'year'. We take a look at the amended dataframe
#    and the dataframe is returned.
#    '''
#    # Convert date to datetime for time series analysis
#    df.Date = pd.to_datetime(df.Date)
    
#    # Histogram of Consumption
#    df.Consumption.hist()
#    plt.title('Consumption')
#    plt.show()
    
    # Histogram of Wind
#    df.Wind.hist()
#    plt.title('Wind')
#    plt.show()
    
    # Histogram of Solar
#    df.Solar.hist()
#    plt.title('Solar')
#    plt.show()
    
    # Histogram of Solar
#    df['Wind+Solar'].hist()
#    plt.title('WindSolar')
#    plt.show()
    
    # Rename column to python ok type
#    df = df.rename(columns={'Wind+Solar': 'WindSolar'})
    
    # Fill null values with 0
#    df = df.fillna(0)
    
    # Set date as index for time series analysis
#    df = df.set_index('Date').sort_index()
    
    # add columns to df
#    df['month'] = df.index.month
#    df['year'] = df.index.year
    
#    print(df.head())
    
#    return df
# -

def display_numeric_column_histograms(data_frame):
    """
    Display histograms for numeric columns in a DataFrame with three colors.

    Args:
    data_frame (DataFrame): The DataFrame to visualize.

    Returns:
    None(prints to console)
    """
    numeric_columns = data_frame.select_dtypes(exclude=["object", "category"]).columns.to_list()
    # Define any number of colors for the histogram bars
    colors = ["#FFBF00"]
    for i, column in enumerate(numeric_columns):
        # Create a histogram for each numeric column with two colors
        figure, axis = plt.subplots(figsize=(10, 3))
        sns.histplot(data_frame, x=column, ax=axis, color=colors[i % len(colors)])
        axis.set_title(f"Histogram of {column}")
        plt.show()


def prepare_ops(df):
    """
    Prepare the operations DataFrame for analysis by performing the following steps:
    
    1. Convert column names to lowercase.
    2. Convert the 'date' column to datetime format.
    3. Set the 'date' column as the DataFrame index.
    4. Extract and add 'month' and 'year' columns.
    5. Fill missing values with zeros.

    Args:
        df (DataFrame): The input operations DataFrame.

    Returns:
        DataFrame: The prepared DataFrame.
    """
    df.columns = df.columns.str.lower()
    df.date = pd.to_datetime(df.date)
    df = df.set_index('date')
    df['month'] = df.index.month
    df['year'] = df.index.year
    df = df.fillna(0)
    return df
