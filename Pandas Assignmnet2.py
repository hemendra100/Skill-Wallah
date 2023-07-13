#!/usr/bin/env python
# coding: utf-8

# Q1. List any five functions of the pandas library with execution.

# 1. read_csv():This is one of the most crucial pandas methods in Python. read_csv() function helps read a comma-separated values (csv) file into a Pandas DataFrame. 
# 2. head():head(n) is used to return the first n rows of a dataset
# 3. describe():used to generate descriptive statistics of the data in a Pandas DataFrame or Series.
# 4. astype():It can be a very helpful function in case your data is not stored in the correct format (data type). For instance, if floating point numbers have somehow been misinterpreted by Python as strings, you can convert them back to floating point numbers with astype(). Or if you want to convert an object datatype to category, you can use astype().
# data_1['Gender'] = data_1.Gender.astype('category')
# 5. loc[:]helps to access a group of rows and columns in a dataset, a slice of the dataset, as per our requirement.We can also access rows and columns based on labels instead of row and column number.
# 
# data_1.loc[0:4, ['Name', 'Age', 'State']] The command will give first for rows of three columns Name, Age & State
# 
# groupby()
# groupby() is used to group a Pandas DataFrame by 1 or more columns, and perform some mathematical operation on it. groupby() can be used to summarize data in a simple manner.
# 
# data_1.groupby(by='State').Salary.mean()
# 

# Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the
# DataFrame with a new index that starts from 1 and increments by 2 for each row.

# In[2]:


import pandas as pd


# In[3]:


data = {'A': ['ALice', 'Bob', 'Claire'], 'B': [25,30,27],'C':['Female','Male','Female']}
df = pd.DataFrame(data)


# In[7]:





# In[5]:


print(df)


# In[10]:


count_row = len(df)


# In[11]:


count_row


# In[15]:


index = [x for x in range(len(df))]


# In[16]:


df1=pd.DataFrame(data, index=index)


# In[17]:


df1


# In[19]:


df1.reindex([1,3,5])


# In[20]:


df1=pd.DataFrame(data, index=[1,3,5])


# In[21]:


df1


# You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
# iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
# function should print the sum to the console.

# In[28]:


import pandas as pd
data ={"Name":['ajay','vijay','raj','neha','asha'], 'Value':[20,40,80,100,150]}
df = pd.DataFrame(data)


# In[30]:



    sum_of_first_three = df['Value'].iloc[:3].sum()
    print("Sum of the first three values:", sum_of_first_three)


# Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column
# 'Word_Count' that contains the number of words in each row of the 'Text' column.

# In[20]:


import pandas as pd
data ={"Text":['ajaykumar','vijay','raj','neha','asha']}
df = pd.DataFrame(data)
df


# In[25]:



df['Word_count']= df["Text"].str.len()
print(df)


# How are DataFrame.size() and DataFrame.shape() different?

#  DataFrame.size(): Returns size of dataframe/series which is equivalent to total number of elements. That is rows x columns.
#  dataframe.shape: The shape property is used to get a tuple representing the dimensionality of the Pandas DataFrame.

# Which function of pandas do we use to read an excel file?

# read_excel()

# You have a Pandas DataFrame df that contains a column named 'Email' that contains email
# addresses in the format 'username@domain.com'. Write a Python function that creates a new column
# 'Username' in df that contains only the username part of each email address.

# In[29]:


import pandas as pd
data = {'Name': ['ALice', 'Bob', 'Claire'], 'Emailid':['Alice@yahoo.com','Bob@gmail.com','Claire@gmail.com']}
df = pd.DataFrame(data)

def extract_username(df):
    df['Username'] = df['Emailid'].apply(lambda email: email.split('@')[0])
    return df

extract_username(df)


# In[ ]:


def extract_username(df):
    df['Username'] = df['Email'].apply(lambda email: email.split('@')[0])
    return df


# You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects
# all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The
# function should return a new DataFrame that contains only the selected rows.

# In[2]:


import pandas as pd
data = {'A': [5,8,9,4,6,10], 'B':[4,12,10,5,7,8], 'C':[2,12,34,6,35,9]}
df=pd.DataFrame(data)
df


# In[4]:


df.loc[0,'A']


# In[7]:


df1 = df.loc[df['A']>5]


# In[8]:


df1


# In[10]:


df1 = df.loc[(df['A']>5) &  (df['B']<10)]


# In[11]:


df1


# Given Pandas data frame with column Value write python function to calculate mean median and SD of Values in Values column

# In[29]:


import pandas as pd
import numpy as np
data = {'Values': [5,8,9,4,6,10]}
df3=pd.DataFrame(data)
df3


# In[30]:


mean_value = np.mean(df3.values)
print(mean_value)

# Calculate standard deviation
std_value = np.std(df3.values)
print(std_value)

# Calculate median along the columns
median_values = np.median(df3.values, axis=0)
print(median_values)


# Given a Pandas DataFrame df with a column 'Sales' and a column 'Date', write a Python function to
# create a new column 'MovingAverage' that contains the moving average of the sales for the past 7 days
# for each row in the DataFrame. The moving average should be calculated using a window of size 7 and
# should include the current day.
# 

# In[22]:


import pandas as pd
import numpy as np
import os
import numpy as np

os.chdir('D:/FDP/Physicswallah')


# In[41]:


os.getcwd()


# In[23]:


df = pd.read_csv('Sales.csv')


# In[44]:


df.head()


# In[24]:


df['moving_average'] = df['Sales'].rolling(7).mean()


# In[50]:


df


# In[25]:


df.dropna(inplace=True)


# In[52]:


df


# You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new
# column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g.
# Monday, Tuesday) corresponding to each date in the 'Date' column.
# 

# In[7]:


from datetime import datetime


# In[26]:


def add_weekday_column(df, date_column):
    df['Weekday'] = df[date_column].apply(lambda x: datetime.strptime(x, '%d-%b-%y').strftime('%A'))
    return df

df = add_weekday_column(df, 'Date')
print(df)


# In[6]:


type(df['Date'])


# Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a Python
# function to select all rows where the date is between '2023-01-01' and '2023-01-31'.
# 

# In[20]:


mask = (df['Date'] > '01-06-2023') & (df['Date'] <= '10-06-2023')
print(df.loc[mask])


# In[29]:


df3 = df[(df['Date'] > '01-06-2023') & (df['Date'] <= '20-06-2023')]
df3


# To use the basic functions of pandas, what is the first and foremost necessary library that needs to
# be imported?

# Numpy, Pandas

# In[ ]:




