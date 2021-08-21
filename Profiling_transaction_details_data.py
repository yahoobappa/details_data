#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


import pandas as pd


# In[3]:


t_details = pd.read_csv("/Users/bappadas/Documents/IITG_Projects/Raw_data_IITG Projects/1028_industry_grade project/transaction_details_data.csv")


# In[4]:


t_details.describe()


# In[5]:


get_ipython().system('pip install pandas-profiling')
from pandas_profiling import ProfileReport


# In[6]:


profile = ProfileReport(t_details)


# In[ ]:


profile.to_file(output_file = "transaction_details_data.html")


# In[ ]:




