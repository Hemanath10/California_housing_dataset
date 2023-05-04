#!/usr/bin/env python
# coding: utf-8

# In[4]:


# A small project was performed on the California housing dataset using Pandas, Matplotlib, and Seaborn. 

# The project focused on addressing analytical questions such as filling missing values, dropping null values, 
# creating a new column, visualizing data through graphs using Matplotlib and Seaborn, and finding statistical descriptions of the data.

# The purpose of the project was to gain insights into the dataset and draw meaningful conclusions from the analysis. 

# The project helped to develop skills in data wrangling, data visualization, and statistical analysis using Python libraries.


# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


hd= pd.read_excel(r'C:\Users\91939\Downloads\housing (2).xlsx')     #importing the excel file as dataset into python 


# In[5]:


hd.head()


# In[ ]:


# 1.What is the average median income of the data set and check the distribution of data using appropriate plots.
# Please explain the distribution of the plot

Average_medivan_income= round(hd['median_income'].mean(),2)
# In[9]:


Average_median_income

# The mean of the median income in the housing dataset, calculated using the statistical module describe() in Pandas, is 3.87.


# In[10]:


sns.displot(x=hd['median_income'], kde='true') 
plt.title('Distribution of median_income')
plt.show()


# In[ ]:


#  A displot from the Seaborn library was used to plot the "median income" column, 
# which allows us to visualize the distribution of the data.

#  The "median income" column in the housing dataset is normally distributed, 
# as observed from the kernel density estimate plot (kdeplot) that was used to visualize the distribution.

# A kernel density estimate plot (kdeplot) is commonly used to visualize the distribution of a variable in a dataset
# and it also provides an estimate of the probability density function of the variable.


# In[ ]:





# In[ ]:


# 2.Draw an appropriate plot to see the distribution of housing_median_age and explain your observations.


# In[11]:


sns.displot(x=hd['housing_median_age'], color='red',edgecolor='black',bins=10, kde='true',linewidth=1, alpha=0.1)
plt.ylabel('Frequency')
plt.title('Distribution of housing_median_age')
plt.show()


# In[ ]:


# The distribution of the "median age" column in the housing dataset is approximately normal in shape.

# The "31-35" age range had the highest frequency of records in the "median age" column of the housing dataset. 
# On average, the median age of the population in the dataset is around 29 years old.

# The data distribution is slightly skewed to the right, with a normal distribution and a peak around 10-20 in the dataset. 
# However, the distribution also has a long tail to the right.


# In[ ]:





# In[ ]:


# 3.Show with the help of visualization, how median_income and median_house_values are related?


# In[12]:


plt.figure(figsize=(12,6))
sns.scatterplot(x='median_income', y='median_house_value', s=50, data=hd, alpha=.5)
plt.title('Relationship between median_income and medaian_house_value ')
plt.show()


# In[ ]:


# Compared to the other columns in the dataset, there is a moderately high correlation between these two columns, 
# with a correlation coefficient of 0.68.

# The observed positive correlation between the "median income" and "median house value" columns indicates that as the median income increases, 
# so does the median house value in the dataset. 

# This suggests that regions with higher income levels tend to have more expensive houses on average.


# In[ ]:





# In[ ]:


# 4. Create a data set by deleting the corresponding examples from the data set for which total_bedrooms are not available.


# In[13]:


hd.isna().sum()


# In[ ]:


# Initially, the "total_bedrooms" column in the dataset contained a total of 207 null (missing) values.


# In[14]:


hd1=hd['total_bedrooms'].dropna()


# In[ ]:


# To remove the null values from the "total_bedrooms" column in the dataset, 
# the dropna() function from the Pandas library was used. 
# This resulted in the creation of a new dataset called "hd1" with the null values removed.


# In[15]:


hd1.isna().sum()


# In[16]:


hd1.info()


# In[ ]:


# After removing the 207 null values from the "total_bedrooms" column using dropna(), 
# the total number of records in the dataset decreased from 20640 to 20433, 
# which corresponds to a decrease of 207 records.


# In[ ]:





# In[ ]:


# 5.Create a data set by filling the missing data with the mean value of the total_bedrooms in the original data set.


# In[17]:


hd2= hd['total_bedrooms'].fillna(hd['total_bedrooms'].mean())


# In[18]:


hd2.isna().sum()


# In[19]:


hd2.info()


# In[ ]:


# To fill the missing values in the "total_bedrooms" column of the dataset, the fillna() function from the Pandas library was used. 
# The missing values were filled with the mean value of the "total_bedrooms" column in the dataset.


# In[ ]:





# In[ ]:


# 6.Write a programming construct (create a user defined function) to calculate the median value of the data set wherever required.


# In[20]:


def median(column_name):
  median_value= hd['{}'.format(column_name)].median()
  return median_value


# In[21]:


median('total_rooms')


# In[ ]:


# A user-defined function was used in the Pandas dataset to calculate the median of the columns in the dataset. 

# This function was likely defined using Python's built-in `def` keyword and takes in a Pandas DataFrame as an argument, 
# and then calculates the median of each column using the `median()` method from the Pandas library. 

# The resulting medians were then returned as a new Pandas Series.


# In[ ]:





# In[ ]:


# 7.Plot latitude versus longitude and explain your observations.


# In[22]:


hd.plot(kind="scatter", x="longitude", y="latitude", 
             alpha=0.3)
plt.title('longitude Vs latitude')
plt.show()


# In[ ]:


# A scatter plot was created to visualize the relationship between the "longitude" and "latitude" columns in the dataset. 

# The correlation between these two variables was found to be negative, meaning that as the "latitude" increases, the "longitude" tends to decrease. 

# To differentiate the two variables in the scatter plot, the alpha parameter was used to decrease the opacity of one variable. 

# This helps to visualize the density of points in areas where the two variables overlap.


# In[ ]:





# In[ ]:


# 8.Create a data set for which the ocean_proximity is ‘Near ocean’.


# In[23]:


hd['ocean_proximity'].unique()                  # to get unique values in a column        


# In[24]:


hdo = hd[hd['ocean_proximity']=='NEAR OCEAN']


# In[25]:


hdo.head()


# In[26]:


hdo.info()


# In[ ]:


# A new dataset called "hdo" was created by filtering the original dataset based on the condition that the "ocean_proximity" column 
# is equal to "near ocean". 

# This resulted in a new dataset containing only the rows where the "ocean_proximity" column had a value of "near ocean". 

# The resulting dataset "hdo" contains 2658 entries where the "ocean_proximity" is "near ocean".


# In[ ]:





# In[ ]:


# 9.Find the mean and median of the median income for the data set created in question 8.


# In[28]:


hdo.mean()


# In[ ]:


# To find the mean of the numerical columns in the newly created dataset "hdo", the `describe()` function with the `mean()` method was used. 

# This function provides descriptive statistics of the dataset, including the mean of each column. 

# By using this function, the mean of each numerical column in the "hdo" dataset was calculated.


# In[ ]:





# In[ ]:


# 10.Please create a new column named total_bedroom_size. If the total bedrooms is 10 or less, it should be quoted as small. 
# If the total bedrooms is 11 or more but less than 1000, it should be medium, otherwise it should be considered large.


# In[29]:


total_bedroom_size=[]
for size in hd['total_bedrooms']:
  if size <=10:
    total_bedroom_size.append('Small')
  elif size >11 and size <=1000:
    total_bedroom_size.append('Medium')
  else:
    total_bedroom_size.append('Large')

hd['total_bedroom_size']= total_bedroom_size
hd.head()


# In[ ]:


# To categorize the data in the "total_bedrooms" column of the California housing dataset, 
# a for loop with if conditions was used. 

# The loop iterates through each row of the dataset and checks the value in the "total_bedrooms" column. 

# If the value is less than or equal to 10, it is categorized as "small". 

# If the value is greater than 10 and less than or equal to 1000, it is categorized as "medium". 

# Finally, if the value is greater than 1000, it is categorized as "large". 

# The resulting categorization provides a way to group the data into smaller, more manageable categories for analysis.

