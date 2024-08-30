# Pandas_Hands_on_File 

import pandas as pd

data_path = ('C:/Users/santh/Desktop/DATASET/USA_REAL_ESTATE_DATA.csv')
data = pd.read_csv(data_path)
print(data)

print(data.columns)

print(f" total Number of Columns are :{len(data.columns)}")
print(f"Columns are {data.columns}")
print(f"Columns are {data.columns.tolist()}")

# To check Top 5 Rows 
print(data.head())

# To check Bottom 5 Rows 
print(data.tail())

#to get The dimension Of Data : No of rows x numbers of columns 
print(data.shape)

num_rows, num_columns = data.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")

print(f"Type of data in shape: {type(data.shape)}")


# data.info() returns the information of the entire dataset
print(data.info())

print(data.isnull().sum().index.tolist)

print(data.isna().sum().values.tolist)








