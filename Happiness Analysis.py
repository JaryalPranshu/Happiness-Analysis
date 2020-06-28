#!/usr/bin/env python
# coding: utf-8

# In[125]:


##Importing Python Libraries for the analysis
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import matplotlib
import plotly.graph_objs as go


# In[114]:


##Importing Datasets for different years
d2015 = pd.read_csv(r"C:\Users\pxj190011\Desktop\Projects\Happiness\2015.csv")
d2016 = pd.read_csv(r"C:\Users\pxj190011\Desktop\Projects\Happiness\2016.csv")
d2017 = pd.read_csv(r"C:\Users\pxj190011\Desktop\Projects\Happiness\2017.csv")
d2018 = pd.read_csv(r"C:\Users\pxj190011\Desktop\Projects\Happiness\2018.csv")
d2019 = pd.read_csv(r"C:\Users\pxj190011\Desktop\Projects\Happiness\2019.csv")


# In[115]:


##Assigning a new Column "YEAR"
d2015["year"] = 2015
d2016["year"] = 2016
d2017["year"] = 2017
d2018["year"] = 2018
d2019["year"] = 2019


# In[135]:


##Joining all the datasets of different years into one
df = d2015.append([d2016,d2017,d2018,d2019])
d2019.head()


# In[117]:


##Renaming Column Names
df = df.rename(columns={'Happiness.score': 'score','Economy (GDP per Capita)': 'Economy',"Trust (Government Corruption)": 'Trust' , 'Health (Life Expectancy)': 'Health'})
df.head()


# In[84]:


#Heatmap to check the corelation for Year 2015
plt.rcParams['figure.figsize'] = (20, 15)
sns.heatmap(d2015.corr(), cmap = 'copper', annot = True)

plt.show()


# In[86]:


#Heatmap to check the corelation for Year 2016
plt.rcParams['figure.figsize'] = (20, 15)
sns.heatmap(d2016.corr(), cmap = 'copper', annot = True)

plt.show()


# In[128]:


#Heatmap to check the corelation for Year 2017
plt.rcParams['figure.figsize'] = (30, 15)
sns.heatmap(d2017.corr(), cmap = 'copper', annot = True)

plt.show()


# In[88]:


#Heatmap to check the corelation for Year 2018
plt.rcParams['figure.figsize'] = (20, 15)
sns.heatmap(d2018.corr(), cmap = 'copper', annot = True)

plt.show()


# In[134]:


#Heatmap to check the corelation for Year 2019
plt.rcParams['figure.figsize'] = (30, 15)
sns.heatmap(d2019.corr(), cmap = 'copper', annot = True)

plt.show()


# In[121]:


## COuntry with the highest rate of genrosity
df[['Country', 'Generosity']].sort_values(by = 'Generosity',
                                                ascending = False).head(10)


# In[139]:


## Country with the highest rate of Health (Life Expectancy)
d2019[['Country', 'Health (Life Expectancy)']].sort_values(by = 'Health (Life Expectancy)', ascending = False).head(10)


# In[140]:


## Country with the highest rate of Family
d2019[['Country', 'Family']].sort_values(by = 'Family', ascending = False).head(5)


# In[141]:


## Country with the highest rate of Economy (GDP per Capita)
d2017[['Country', 'Economy (GDP per Capita)']].sort_values(by = 'Economy (GDP per Capita)',
            ascending = False).head(10)

