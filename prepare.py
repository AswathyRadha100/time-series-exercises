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

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def prepare_store(df):
    """
    Prepares a sales DataFrame for analysis by:
    1. Converting sale dates to datetime format.
    2. Setting the datetime as the index.
    3. Extracting the month and day of the week.
    4. Calculating the total sales for each transaction.

    Args:
        df (DataFrame): The input sales DataFrame.

    Returns:
        DataFrame: The prepared DataFrame.
    """
    # Convert the sale date into a datetime
    df.sale_date = pd.to_datetime(df.sale_date, format='%Y-%m-%d')
    #df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y')
    # Set the index as the new datetime value
    df = df.set_index('sale_date')
    # Extract the month value (name of month)
    df['month'] = df.index.strftime('%B')
    # Extract the day of the week from the date
    df['day of the week'] = df.index.day_name()
    # Calculate the total sales
    df['sales_total'] = df.sale_amount * df.item_price
    return df


def prep_germany_data(df):
    '''
    Takes in a dataframe, coverts Date to DateTime format and makes it the index, produces histograms 
    of all variables, renames "Wind+Solar" to the more python-friendly "WindSolar", fills the abundant 
    nulls/NaNs with 0, and adds the columns 'month' and 'year'. We take a look at the amended dataframe
    and the dataframe is returned.
    '''
    # Convert date to datetime for time series analysis
    df.Date = pd.to_datetime(df.Date)
    
    # Histogram of Consumption
    df.Consumption.hist()
    plt.title('Consumption')
    plt.show()
    
    # Histogram of Wind
    df.Wind.hist()
    plt.title('Wind')
    plt.show()
    
    # Histogram of Solar
    df.Solar.hist()
    plt.title('Solar')
    plt.show()
    
    # Histogram of Solar
    df['Wind+Solar'].hist()
    plt.title('WindSolar')
    plt.show()
    
    # Rename column to python ok type
    df = df.rename(columns={'Wind+Solar': 'WindSolar'})
    
    # Fill null values with 0
    df = df.fillna(0)
    
    # Set date as index for time series analysis
    df = df.set_index('Date').sort_index()
    
    # add columns to df
    df['month'] = df.index.month
    df['year'] = df.index.year
    
    print(df.head())
    
    return df


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
