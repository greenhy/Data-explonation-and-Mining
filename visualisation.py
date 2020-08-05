#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

# read the veteran dataset
df = pd.read_csv('veteran.csv')

# show all columes information
print(df.info())


# # Setting correct data type to variables

# In[4]:


# change DemCLuster from interval/integer to nominal/str
df['DemCluster'] = df['DemCluster'].astype(str)


# In[5]:


df['DemHomeOwner'].value_counts()


# In[6]:


# change DemHomeOwner into binary 0/1 variable
dem_home_owner_map = {'U':0, 'H': 1}
df['DemHomeOwner'] = df['DemHomeOwner'].map(dem_home_owner_map)


# # Explore column data

# Function pandas.Series.describe() prints key statistics of a series, including count
# (number of non-missing values), mean (average), std (standard deviation), min, max, and
# quantiles (typically at 25%, 50% (i.e. median), 75%).

# Function pandas.Series.unique() prints unique values in a Series. Typically used for
# categorical variables.

# Function pandas.Series.value_counts() prints unique values and corresponding count in
# a Series. Also commonly used for categorical variables.

# In[7]:


# describe key statistics from DemAge column
print(df['DemAge'].describe())


# In[8]:


# unique values in DemAge
print(df['DemAge'].unique())


# In[9]:


# print number of occurences for each unique value in DemAge
print(df['DemAge'].value_counts())


# In[10]:


# similar as above, but the values are binned into a 10 range bins for easier interpretatio
print(df['DemAge'].value_counts(bins=10))


# # Data dispersion

# In[11]:


import numpy as np
df2 = df.select_dtypes(include=[np.number]) # This code selects the columns of numeric data


# In[12]:


df2.mean()


# In[13]:


df2.median()


# In[14]:


df2.mode()[0:1]


# In[15]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[16]:


ax = sns.boxplot(df['DemMedIncome'])
plt.show()


# In[17]:


# To ignore any future warnings
import warnings
warnings.filterwarnings("ignore")
dg = sns.distplot(df['DemMedIncome'])
plt.show()


# In[18]:


#to explore the distribution of DemAge
# distplot is sensitive towards missing values

df3 = df['DemAge'].dropna()
dg = sns.distplot(df3)
plt.show()


# In[19]:


dg = sns.countplot(data=df, x='DemGender')
plt.show()


# # Grouping and correlation of columns

# In[20]:


# get the average age of donors, grouped by their lapsing information
print(df.groupby(['TargetB'])['DemAge'].mean())


# In[21]:


# get the value count of each gender
print("Raw count of genders of lapsing and non-lapsing donors")
print(df.groupby(['TargetB'])['DemGender'].value_counts())
print("------------------")
# add normalisation to get the relative frequency
print("Normalised count (percentage) of genders of lapsing and non-lapsing donors")
print(df.groupby(['TargetB'])['DemGender'].value_counts(normalize=True))


# In[22]:


import matplotlib.pyplot as plt2
plt2.scatter(df['GiftAvg36'], df['GiftAvgCard36'])
plt2.title('Correlation')
plt2.xlabel('GiftAvg36')
plt2.ylabel('GiftAvgCard36')
plt2.show()


# In[23]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
corr = df2.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(df2.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(df2.columns)
ax.set_yticklabels(df2.columns)
plt.show()


# In[ ]:




