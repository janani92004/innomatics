# -*- coding: utf-8 -*-
"""innomatics2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pM665HQ7YEz7GaQa89uRgYfTsIdYyDRZ
"""

import chardet
file_path = '/content/HSR_Layout.csv'

with open(file_path, 'rb') as file:
    raw_data = file.read(10000)
result = chardet.detect(raw_data)

print(f"Detected encoding: {result['encoding']}")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/content/merged_file_2.csv')

def categorize_property_age(age):
    if age <= 1:
        return 'New'
    elif 1 < age <= 5:
        return 'Less than 5 years'
    elif 5 < age <= 10:
        return '5 to 10 years'
    elif 10 < age <= 20:
        return '10 to 20 years'
    else:
        return 'More than 20 years'


df['property_age_category'] = df['property_age'].apply(categorize_property_age)


print(df[['property_age', 'property_age_category']].head())
category_counts = df['property_age_category'].value_counts()


print(category_counts)

type_counts = df['type'].value_counts()


print(type_counts)

import pandas as pd


df = pd.read_csv('merged_file_2.csv', low_memory=False)


df['activation_date'] = pd.to_datetime(df['activation_date'], dayfirst=True)
df['request_date'] = pd.to_datetime(df['request_date'], dayfirst=True)


df['days_since_activation'] = (df['request_date'] - df['activation_date']).dt.days


df_within_7_days = df[df['days_since_activation'] <= 7]


interaction_counts = df_within_7_days.groupby('property_id').size()

total_interactions_majority = interaction_counts.sum()


print(f'Total number of interactions for the majority of properties within 7 days of activation: {total_interactions_majority}')

import pandas as pd


df = pd.read_csv('merged_file_2.csv')


df['request_date'] = pd.to_datetime(df['request_date'], dayfirst=True)


interactions_by_apartment = df.groupby('type')['request_date'].count()


apartment_with_max_interactions = interactions_by_apartment.idxmax()
max_interactions = interactions_by_apartment.max()


print(f"The apartment type with the highest number of interactions is '{apartment_with_max_interactions}' with {max_interactions} interactions.")

import pandas as pd

df = pd.read_csv('merged_file_2.csv')


df['request_date'] = pd.to_datetime(df['request_date'], dayfirst=True)


top_localities = ['Bellandur', 'Kasavanahalli', 'HBR Layout', 'Brookefield']
filtered_df = df[df['locality'].isin(top_localities)]


interaction_counts = filtered_df.groupby('locality')['request_date'].count()

max_interactions_locality = interaction_counts.idxmax()
max_interactions_count = interaction_counts.max()


print(f"The locality with the highest interaction counts is '{max_interactions_locality}' with {max_interactions_count} interactions.")
