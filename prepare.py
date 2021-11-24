import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

def clean_telco_data(df):
    '''
    This function takes in the telco data and cleans it
    '''
    
    # change data type for total charges from string to float
    df.total_charges = pd.to_numeric(df.total_charges, errors='coerce')
    # drop rows where new customers have not yet had opportunity to churn
    df = df[df.total_charges.notnull()]
    # replace information included in another column to create binary values and simplify encoding
    df.replace('No internet service', 'No', inplace=True)
    
    # create df of dummy variables for columns with two values, dropping first
    dummy_df1 = pd.get_dummies(df[['gender', 'partner', 'dependents', 'online_security', 'online_backup',
                                   'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies',
                                   'paperless_billing', 'churn']], drop_first=True)
    # create df of dummy variables for columns with more than two values, keeping all columns for clarity
    dummy_df2 = pd.get_dummies(df[['multiple_lines','contract_type', 'internet_service_type', 'payment_type']])
    
    # identify and drop columns that are unnecessary or duplicated
    cols_to_drop = ['payment_type_id', 'internet_service_type_id', 'contract_type_id',
                    'customer_id', 'gender','partner', 'dependents', 'phone_service', 'online_security',
                    'online_backup', 'device_protection', 'tech_support', 'streaming_tv',
                    'streaming_movies', 'paperless_billing', 'churn']
    df = df.drop(columns=cols_to_drop)
    
    # concatenate dummy variable dfs onto original dataframe
    df = pd.concat([df, dummy_df1, dummy_df2], axis=1)

    # rename columns for clarity
    df.rename(columns={
                'gender_Male': 'is_male',
                'partner_Yes': 'has_partner',
                'dependents_Yes': 'has_dependents',
                'online_security_Yes': 'online_security',
                'online_backup_Yes': 'online_backup',
                'device_protection_Yes': 'device_protection',
                'tech_support_Yes': 'tech_support',
                'streaming_tv_Yes': 'streaming_tv',
                'streaming_movies_Yes': 'streaming_movies',
                'paperless_billing_Yes': 'paperless_billing',
                'churn_Yes': 'churn',
                'multiple_lines_No': 'one_line',
                'multiple_lines_No phone service': 'no_phone_service',
                'multiple_lines_Yes': 'has_multiple_lines',
                'contract_type_Month-to-month': 'month_to_month_contract',
                'contract_type_One year': 'one_year_contract',
                'contract_type_Two year': 'two_year_contract',
                'internet_service_type_DSL': 'dsl_internet',
                'internet_service_type_Fiber optic': 'fiber_optic_internet',
                'internet_service_type_None': 'no_internet_service',
                'payment_type_Bank transfer (automatic)': 'bank_transfer_payment_automatic',
                'payment_type_Credit card (automatic)': 'credit_card_payment_automatic',
                'payment_type_Electronic check': 'electronic_check_payment',
                'payment_type_Mailed check': 'mailed_check_payment'}, inplace=True)
    return df


def split_telco_data(df):
    '''
    This function takes in a dataframe and splits the data into train, validate and test samples. 
    Test, validate, and train are 20%, 24%, & 56% of the original dataset, respectively. 
    The function returns train, validate and test dataframes. 
    '''
    # split dataframe 80/20, stratify on churn to ensure equal proportions in both dataframes
    train_validate, test = train_test_split(df, test_size=.2, 
                                            random_state=369, 
                                            stratify=df.churn)
    # split larger dataframe from previous split 70/30, stratify on churn
    train, validate = train_test_split(train_validate, test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.churn)
    # results in 3 dataframes
    return train, validate, test


def prep_telco_data(df):
    '''
    This function takes in a dataframe and applies the previously defined functions to clean and split the data. It returns train, validate, and test dataframes.
    '''
    # cleans data
    df = clean_telco_data(df)
    # splits data
    train, validate, test = split_telco_data(df)
    return train, validate, test