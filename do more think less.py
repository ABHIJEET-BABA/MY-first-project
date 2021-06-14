#!/usr/bin/env python
# coding: utf-8

# # BIG BASKET ANALYSIS

# # project  price_of transport
# 

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


dataset=pd.read_csv("Data_Train.csv")


# In[9]:


dataset


# In[3]:


pd.set_option('display.max_columns',None)


# In[4]:


dataset.shape


# In[6]:


dataset.head()


# In[7]:


dataset.info()


# In[8]:


dataset["Duration"].value_counts()


# In[9]:


dataset.dropna(inplace=True)


# In[10]:


dataset.isnull().sum()


# In[11]:


dataset["Journey_day"] = pd.to_datetime(dataset.Date_of_Journey, format="%d/%m/%Y").dt.day


# In[12]:


dataset["Journey_month"] = pd.to_datetime(dataset["Date_of_Journey"], format = "%d/%m/%Y").dt.month


# In[13]:


dataset.head()


# In[14]:


dataset["Arrival_hour"] = pd.to_datetime(dataset.Arrival_Time).dt.hour

dataset["Arrival_min"] = pd.to_datetime(dataset.Arrival_Time).dt.minute

dataset.drop(["Arrival_Time"], axis = 1, inplace = True)


# In[15]:


dataset.head()


# In[16]:


duration = list(dataset["Duration"])

for i in range(len(duration)):
    if len(duration[i].split()) != 2:    
        if "h" in duration[i]:
            duration[i] = duration[i].strip() + " 0m"   
        else:
            duration[i] = "0h " + duration[i]           

duration_hours = []
duration_mins = []
for i in range(len(duration)):
    duration_hours.append(int(duration[i].split(sep = "h")[0]))   
    duration_mins.append(int(duration[i].split(sep = "m")[0].split()[-1])) 


# In[17]:


dataset["Duration_hours"]=duration_hours
dataset["Duration mins"]=duration_mins


# In[28]:


dataset.head()


# In[30]:


dataset.drop(["Duration"], axis = 1, inplace = True)


# In[31]:


dataset.head()


# In[18]:


dataset["Airline"].value_counts()


# In[19]:


sns.catplot(y="Price",x="Airline",data=dataset.sort_values("Price",ascending=False),kind="boxen",height=6,aspect=3)
plt.show()


# In[37]:


sns.catplot(y = "Price", x = "Airline", data = dataset.sort_values("Price", ascending = False), kind="boxen", height = 6, aspect = 3)
plt.show()


# In[22]:


Airline=dataset[["Airline"]]

Airline=pd.get_dummies(Airline,drop_first=True)

Airline.head()


# In[23]:


dataset["Source"].value_counts()


# In[29]:


sns.catplot(y = "Price", x = "Source", data = dataset.sort_values("Price", ascending = False), kind="boxen", height = 6, aspect = 3)
plt.show()


# In[27]:


Source=dataset[["Source"]]
Source=pd.get_dummies(Source,drop_first=True)
Source.head()


# In[30]:


dataset["Destination"].value_counts()


# In[31]:


Destination=dataset[["Destination"]]

Destination=pd.get_dummies(Destination,drop_first=True)


# In[32]:


Destination.head()


# In[33]:


dataset["Route"]


# In[ ]:




