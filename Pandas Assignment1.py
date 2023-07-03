#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[9]:


import pandas as pd
list =[4,8,15,16,23,42]
ser= pd.Series(list)
print(ser)


# In[10]:


import pandas as pd
list1 =[1,2,3,4,5,6,7,8,9,10]
ser1 =pd.Series(list1)
print(ser1)


# In[17]:


import pandas as pd
data = {'Name': ['ALice', 'Bob', 'Claire'], 'Age': [25,30,27],'Gender':['Female','Male','Female']}
df = pd.DataFrame(data)
print(df)


# What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.
# 

# Series (a one-dimensional labelled array) and DataFrame (a two-dimensional labelled data structure with columns of possibly diverse types).

# In[18]:


import pandas as pd
# Example of series
list1 =[1,2,3,4,5,6,7,8,9,10]
ser1 =pd.Series(list1)
print(ser1)
#example of dataframe
data = {'Name': ['ALice', 'Bob', 'Claire'], 'Age': [25,30,27],'Gender':['Female','Male','Female']}
df = pd.DataFrame(data)
print(df)


# What are some common functions you can use to manipulate data in a Pandas DataFrame? Can you give an example of when you might use one of these functions?
# 

# Dropping columns in the data
# df_dropped = data.drop('Survived', axis=1)
# 
# Dropping rows in the data
# df_row_dropped = data.drop(2, axis=0)
# 
# Renaming a column in the dataset
# df_renamed = data.rename(columns={'PassengerId': 'Id'})
# 
# Select columns with specific data types
# integer_data = data.select_dtypes('int')
# 
# 
# This article was published as a part of the Data Science Blogathon
# 
# Pandas
# Pandas is an open-source data analysis and data manipulation library written in python. Pandas provide you with data structures and functions to work on structured data seamlessly. The name Pandas refer to “Panel Data”, which means a structured dataset. Pandas have two main classes to work on, DataFrame and Series. Let us explore more on this later in this article.
# 
# Key Features of Pandas
# Perform Group by operation seamlessly
# Datasets are mutable using pandas which means we can add new rows and columns to them.
# Easy to handle missing data
# Merge and join datasets
# Indexing and subsetting data
# Installation
# Install via pip using the following command,
# 
# pip install pandas
# Install via anaconda using the following command,
# 
# conda install pandas
# DataFrame in Pandas
# A DataFrame is a two-dimensional table in pandas. Each column can have different data types like int, float, or string. Each column is of class Series in pandas, we’ll discuss this later in this article.
# 
# datset | Data Manipulation
# dataframe
# Image Source
#  
# 
# 
# Become a Full Stack Data Scientist
# Transform into an expert and significantly impact the world of data science.
# Creating a DataFrame in Pandas
# 
# # import the library as pd
# import pandas as pd
# df = pd.DataFrame(
#     {
#         'Name': ['Srivignesh', 'Hari'],
#         'Age': [22, 11],
#         'Country': ['India', 'India']
#     }
# ) 
# print(df)
# # output
# #         Name  Age Country
# # 0  Srivignesh   22   India
# # 1        Hari   11   India
# pd.DataFrame is a class available in pandas. Here we provide a dictionary whose keys are the column names (‘Name’, ‘Age’, ‘Country’) and the values are the values in those columns. Here each column is of class pandas.Series. Series is a one-dimensional data used in pandas.
# 
# # accessing the column 'Name' in df
# print(df['Name'])
# # Output
# # 0    Srivignesh
# # 1          Hari
# # Name: Name, dtype: object
# print(type(df['Name']))
# # Output
# # <class 'pandas.core.series.Series'>
# Let’s get started with Data Manipulation using Pandas!
# For this purpose, we are going to use Titanic Dataset which is available on Kaggle.
# 
# import pandas as pd
# path_to_data = 'path/to/titanic_dataset'
# # read the csv data using pd.read_csv function
# data = pd.read_csv(path_to_data)
# data.head()
# data.head | Data manipulation
# Dropping columns in the data
# df_dropped = data.drop('Survived', axis=1)
# df_dropped.head()
# dropping columns
# The ‘Survived’ column is dropped in the data. The axis=1 denotes that it ‘Survived’ is a column, so it searches ‘Survived’ column-wise to drop.
# 
# Drop multiple columns using the following code,
# 
# df_dropped_multiple = data.drop(['Survived', 'Name'], axis=1)
# df_dropped_multiple.head()
# 
# The columns ‘Survived’ and ‘Name’ are dropped in the data.
# 
# Dropping rows in the data
# df_row_dropped = data.drop(2, axis=0)
# df_row_dropped.head()
# dropping rows
# The row with index 2 is dropped in the data. The axis=0 denotes that index 2 is a row, so it searches the index 2 column-wise.
# 
# Drop multiple rows using the following code,
# 
# df_row_dropped_multiple = data.drop([2, 3], axis=0)
# df_row_dropped_multiple.head()
# drop multiple rows | Data manipulation
# The rows with indexes 2 and 3 are dropped in the data.
# 
# Renaming a column in the dataset
# data.columns
# # Output
# # Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
# #        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
# #       dtype='object')
# df_renamed = data.rename(columns={'PassengerId': 'Id'})
# df_renamed.head()
# rename column | Data manipulation
# The column ‘PassengerId’ is renamed to ‘Id’ in the data. Do not forget to mention the dictionary inside the columns parameter.
# 
# Rename multiple columns using the following code,
# 
# df_renamed_multiple = data.rename(
#     columns={
#         'PassengerId': 'Id', 
#         'Sex': 'Gender',
#     }
# )
# df_renamed_multiple.head()
# rename multiple columns
# The columns ‘PassengerId’ and ‘Sex’ are renamed to ‘Id’ and ‘Gender’ respectively.
# 
# Select columns with specific data types
# integer_data = data.select_dtypes('int')
# integer_data.head()
# selct columns
# The above code selects all columns with integer data types.
# 
# float_data = data.select_dtypes('float')
# float_data.head()
# select by value
# The above code selects all columns with float data types.
# 
# Slicing the dataset
# data.iloc[:5, 0]
# The above code returns the first five rows of the first column. The ‘:5’ in the iloc denotes the first five rows and the number 0 after the comma denotes the first column, iloc is used to locate the data using numbers or integers.
# 
# Group by in DataFrame
# data.groupby('Sex').agg({'PassengerId': 'count'})
# The above code groups the values of the column ‘Sex’ and aggregates the column ‘PassengerId’ by the count of that column.

# Which of the following is mutable in nature Series, DataFrame, Panel?
# 

# All pandas data structures are value-mutable (the values they contain can be altered) but not always size-mutable. The length of a Series cannot be changed, but, for example, columns can be inserted into a DataFrame.

# Create a DataFrame using multiple Series. Explain with an example.

# In[22]:


import pandas as pd
# Example of series
list1=[1,2,3,4,5,6,7,8,9,10]
list2 =[10,12,14,16,18,20,22,24,26,28]
list3 =[100,200,200,400,500,600,700,800,900,1000]
ser1= pd.Series(list1)
ser2=pd.Series(list2)
ser3=pd.Series(list3)
df = pd.concat([ser1,ser2,ser3], axis=1)
print(df)


# In[ ]:




