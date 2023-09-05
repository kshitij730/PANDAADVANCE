#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""List any five functions of the pandas library with execution."""


# In[2]:


import pandas as pd


# In[5]:


df = pd.read_csv("https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/organizations/organizations-100.csv")


# In[6]:


df.to_csv("org.csv")


# In[7]:


df = pd.read_csv("org.csv")


# In[8]:


df.head()


# In[9]:


df.tail()


# In[10]:


df.columns


# In[11]:


df.dtypes


# In[12]:


df.describe()


# In[13]:


"""Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the
DataFrame with a new index that starts from 1 and increments by 2 for each row."""


# In[32]:


import pandas as pd

def reindex_dataframe(df):
    # Reset the index to default integer index
    df_reset = df.reset_index(drop=True)
    
    # Create a new index starting from 1 and incrementing by 2
    new_index = pd.Series(range(1, len(df_reset) * 2, 2))
    
    # Assign the new index to the DataFrame
    df_reset.index = new_index
    
    return df_reset


# In[33]:


# Example usage:
import pandas as pd

data = {'A': [10, 20, 30], 'B': [40, 50, 60], 'C': [70, 80, 90]}
df = pd.DataFrame(data)

new_df = reindex_dataframe(df)
print(new_df)


# In[34]:


""""You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
function should print the sum to the console."""


# In[35]:


import pandas as pd

def calculate_sum_of_first_three_values(df):
    # Check if the 'Values' column exists in the DataFrame
    if 'Values' not in df.columns:
        print("DataFrame does not contain a 'Values' column.")
        return
    
    # Extract the 'Values' column
    values_column = df['Values']
    
    # Calculate the sum of the first three values
    sum_of_first_three = values_column.head(3).sum()
    
    # Print the sum to the console
    print("Sum of the first three values in the 'Values' column:", sum_of_first_three)

# Example usage:
data = {'Values': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

calculate_sum_of_first_three_values(df)


# In[1]:


"""Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column
'Word_Count' that contains the number of words in each row of the 'Text' column."""


# In[25]:


import pandas as pd


# In[26]:


data = {'Text' : ["Kshitij", "Sharma"]}


# In[27]:


df = pd.DataFrame(data)


# In[28]:


df


# In[36]:


df['Word_Count'] = df['Text'].count


# In[37]:


df


# In[1]:


"""To use the basic functions of pandas, what is the first and foremost necessary library that needs to
be imported?"""


# In[2]:


"""we have to import (import pandas as pd)"""


# In[3]:


"""Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a Python
function to select all rows where the date is between '2023-01-01' and '2023-01-31'."""


# In[4]:


import pandas as pd


# In[11]:


date = {'Date' : ["2023-01-01","2023-01-01","2023-01-02","2023-01-03","2023-01-04","2023-01-05","2023-01-06","2023-01-07","2023-01-08","2023-01-09","2023-01-10","2023-01-11","2023-01-12","2023-01-13","2023-01-14","2023-01-15","2023-01-16","2023-01-17","2023-01-18","2023-01-19","2023-01-20","2023-01-21","2023-01-22","2023-01-23","2023-01-24","2023-01-25","2023-01-26","2023-01-27","2023-01-28","2023-01-29","2023-01-30","2023-01-31"]}


# In[12]:


df = pd.DataFrame(date)


# In[13]:


df


# In[14]:


df[(df['Date'] > '2023-01-01') & (df['Date'] < '2023-01-31')]


# In[15]:


"""You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new
column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g.
Monday, Tuesday) corresponding to each date in the 'Date' column."""


# In[21]:


week = {'Date' : ["2023-01-01","2023-01-02","2023-01-03","2023-01-04", "2023-01-05"],
       'Weekdays' : ["Monday","Tuesday","Wednesday","Thursday","Friday"]}
df = pd.DataFrame(week)


# In[22]:


df


# In[23]:


"""Given a Pandas DataFrame df with a column 'Values', write a Python function to calculate the mean,
median, and standard deviation of the values in the 'Values' column."""


# In[24]:


val = {'Values' : [1,2,3,4,5,6,7,10,23,45,6,45,7,9,10,2,3]}


# In[25]:


df = pd.DataFrame(val)


# In[26]:


df


# In[27]:


df.describe()

