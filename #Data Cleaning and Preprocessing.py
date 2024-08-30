#Data Cleaning and Preprocessing

#Task: Write a Python program to clean and preprocess a dataset. 
#This includes handling missing values, removing duplicates, and encoding categorical variables.

import pandas as pd
import sklearn

print(sklearn.__version__)

from sklearn.preprocessing import LabelEncoder

# Load the Titanic dataset
df = pd.read_csv('C:/Users/santh/Desktop/DATASET')

# Handle missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Encode categorical variables
label_encoder = LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])
df['Embarked'] = label_encoder.fit_transform(df['Embarked'])

print(df.head())

