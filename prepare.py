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
    df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y')
    # Set the index as the new datetime value
    df = df.set_index('sale_date')
    # Extract the month value (name of month)
    df['month'] = df.index.strftime('%B')
    # Extract the day of the week from the date
    df['day of the week'] = df.index.day_name()
    # Calculate the total sales
    df['sales_total'] = df.sale_amount * df.item_price
    return df


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



