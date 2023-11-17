#!/usr/bin/env python
# coding: utf-8

# # zomato Preference Analysis
# 
# Dataset Link:https://www.kaggle.com/datasets/rrkcoder/zomato-data-40k-restaurants-of-indias-100-cities/download?datasetVersionNumber=1
# 

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


#- Read the Zomato dataset containing information about restaurants, ratings, cuisines, and related details to perform user preference analysis.
data=pd.read_csv(dataset_link,index_col=False)


# In[3]:


# Converting Data to Pandas DataFrame and Displaying Information

## Objective:
#- Convert the loaded Zomato dataset into a pandas DataFrame for efficient data manipulation and analysis.
#- Display essential information about the DataFrame.

df=pd.DataFrame(data)
print(df.info())


# In[4]:


#Checking for Missing Values in the Zomato DataFrame

## Objective:
#- Examine the dataset for missing values to assess data integrity and plan for data cleaning if necessary.

print(df.isnull().sum())


# In[5]:


# Displaying the Initial Rows of the Zomato DataFrame

## Objective:
#- Provide a preview of the dataset by displaying the first few rows of the Zomato DataFrame.

print(df.head())


# In[6]:


# Displaying Column Names of the Zomato DataFrame

## Objective:
#- Obtain a list of column names in the Zomato DataFrame for reference and further analysis.

df.columns


# In[7]:


# Filtering Zomato DataFrame based on Rating Values

## Objective:
#- Remove rows from the Zomato DataFrame where the 'Rating' column contains specific values from the given list.

list=[" ","_","New","-"]
df=df[df.Rating.isin(list)==False]
print(df)


# In[8]:


# Filtering Zomato DataFrame to Exclude Rows with Null Cuisine Values

## Objective:
#- Remove rows from the Zomato DataFrame where the 'Cuisine' column contains null (missing) values.

df=df[df["Cuisine"].isnull()==False]


# In[9]:


# Displaying Rows with Null Values in the 'Location' Column

## Objective:
#- Print the rows in the Zomato DataFrame where the 'Location' column contains null (missing) values.

print(df[df["Location"].isnull()==True])


# In[10]:


print(df)


# In[11]:


# Extracting Numerical Values from 'Average Price' Column

## Objective:
#- Extract numerical values from the 'Average Price' column, assuming values are prefixed with the Indian Rupee symbol (₹).

df["Average Price"]=df["Average Price"].str.extract(r'\₹(\d+)', expand=False)
print(df)


# In[12]:


# Filtering Zomato DataFrame Based on 'Average Delivery Time'

## Objective:
#- Remove rows from the Zomato DataFrame where the 'Average Delivery Time' column starts with specific values from the given list.

list=["Currently not accepting orders","Opens"]
df=df[df["Average Delivery Time"].str.startswith("Opens")==False]


# In[13]:


print(df)


# In[14]:


# Further Filtering Zomato DataFrame Based on 'Average Delivery Time'

## Objective:
#- Continue refining the Zomato DataFrame by removing rows where the 'Average Delivery Time' column starts with specific phrases.


df=df[df["Average Delivery Time"].str.startswith("Currently")==False]
df=df[df["Average Delivery Time"].str.startswith("Temporarily")==False]
df=df[df["Average Delivery Time"].str.startswith("Opening")==False]


# In[15]:


df=df[df["Average Delivery Time"].str.startswith("Closes")==False]


# In[18]:


# Extracting and Filtering 'Average Delivery Time' Values

## Objective:
#- Extract numerical values from the 'Average Delivery Time' column and filter the DataFrame to include only rows where the delivery time is equal to "10".

df["Average Delivery Time"]=df["Average Delivery Time"].str.extract(r'(\d+)\s?\w*', expand=False)
print(df[df["Average Delivery Time"]=="10"])


# In[19]:


# Counting Null Values in the 'Safety Measure' Column

## Objective:
#- Determine and print the number of null (missing) values in the 'Safety Measure' column.

print(df["Safety Measure"].isnull().sum())


# In[20]:


# Categorizing 'Safety Measure' Values

## Objective:
#- Categorize values in the 'Safety Measure' column based on whether they start with "Follows" or not.

def rep(x):
    if(x.startswith("Follows")==True):
        return "safety"
    else:
        return "WHO"
            
df["Safety Measure"]=df["Safety Measure"].apply(lambda x:rep(x))
print(df)


# In[21]:


# Counting Null Values in the 'Location' Column

## Objective:
#- Determine and print the number of null (missing) values in the 'Location' column.

print(df["Location"].isnull().sum())


# In[23]:


print(df.dtypes)


# In[24]:


df=df[df['Average Price'].isnull()==False]


# In[25]:


# Counting Null Values in the 'Average Delivery Time' Column

## Objective:
# Determine and print the number of null (missing) values in the 'Average Delivery Time' column.

print(df['Average Delivery Time'].isnull().values.sum())


# In[26]:


df=df[df['Average Delivery Time'].isnull()==False]


# In[27]:


print(df['Average Delivery Time'].isnull().values.sum())


# In[28]:


print(df.isnull().values.any())


# In[29]:


print(df[df["Average Delivery Time"]=="10"])


# In[30]:


# Displaying the Dimensions of the DataFrame

## Objective:
#- Print the number of rows and columns in the DataFrame.
print(df.shape)


# In[31]:


# Converting Data Types of DataFrame Columns

## Objective:
#- Modify the data types of specific columns in the DataFrame according to a predefined dictionary.

typ={"Restaurant Name":str,"Rating":float,"Cuisine":str,"Average Price":float,"Average Delivery Time":int,"Safety Measure":str,"Location":str}
df=df.astype(typ)
print(df.dtypes)


# In[32]:


# Displaying Rows with 'Average Delivery Time' Equal to 1

## Objective:
#- Print rows from the DataFrame where the 'Average Delivery Time' column has a value equal to 1.

print(df[df["Average Delivery Time"]==1])


# In[33]:


print(df['Restaurant Name'].isnull().values.sum())


# In[34]:


# Calculating and Displaying Correlation Matrix

## Objective:
#- Calculate and print the correlation matrix for numeric columns in the DataFrame.

print(df.corr())


# In[35]:


#df.plot.bar(x="Average Price",y="Average Delivery Time")


# In[36]:


#df.to_csv("zomato_dataset_analysis.csv",index=False)
df['Index'] = range(1, len(df) + 1)


# In[37]:


#df.to_csv("zomato_dataset_cusine.csv",index=False,columns=["Index","Restaurant Name","Cuisine"])
#df.to_csv("zomato_FULLDATA.csv",index=False)


# In[38]:


df.shape


# In[39]:


df.iloc[0,2]


# In[40]:


# Extracting Unique Words from 'Cuisine' Column

## Objective:
#- Define a function to extract unique words from the 'Cuisine' column in the DataFrame.

import re
def word_search():
    y=[]
    for i in range(0,34855):
        words=df.iloc[i,2].split(',')
        for w in words:
            if re.search(w.strip(),str(y)):
                pass
            else:
                y.append(w.strip())
    print(y)
    return y
z=word_search()


# In[41]:


len(z)


# In[42]:


#cuisine=pd.DataFrame(index=df["Restaurant Name"],columns=z)
#cuisine.to_csv("cusine.csv")
#34855


# In[43]:


import re
#def word_search():
 #   for i in range(0,122):
  #      for j in range(0,34928):
   #         words=df.iloc[j,2].split(',')
    #        for w in words:
     #           if re.search(z[i],w.strip()):
      #              cuisine.iloc[j,i]=1
       #             break
        #        else:
         #           cuisine.iloc[j,i]=0
                    
        
#word_search()
#cuisine.to_csv("cusine.csv")


# In[44]:


print(df.iloc[1,7])


# In[45]:


cuisine_1=pd.DataFrame(columns=["Restaurant_Names","Cusine","Index"])
cuisine.to_csv("cusine.csv")
#34855


# In[55]:


# Reading Cuisine Images from CSV and Printing Pizza Images

## Objective:
#-- Read cuisine images from a CSV file and print URLs associated with the "Pizza" cuisine.

images_cusine=pd.read_csv("cusine_images.csv")
print(images_cusine)   
for img in images_cusine.index:
    if(images_cusine.iloc[img,1]=="Pizza"):
        print(images_cusine.iloc[img,2])


# In[58]:


# Searching for Cuisines in 'Cuisine' Column and Creating a New DataFrame

## Objective:
#- Search for specific cuisines in the 'Cuisine' column of the main DataFrame and create a new DataFrame with additional information.

import re
cus=[]
res=[]
ind=[]
imgs=[]
def word_search():
    for i in range(0,122):
        for j in range(0,34855):
            words=df.iloc[j,2].split(',')
            for w in words:
                if re.search(z[i],w.strip()):
                    res.append(df.iloc[j,0])
                    cus.append(w.strip())
                    for img in images_cusine.index:
                        if(images_cusine.iloc[img,1]==w.strip()):
                            imgs.append(images_cusine.iloc[img,2])
                            break
                    ind.append(df.iloc[j,7])
                    break
                    
        
word_search()
cuis=pd.DataFrame({"Restaurant_Names":res,"Cusine":cus,"Index":ind,"Images":imgs})
print(cuis)
cuis.to_csv("cusine_FULLDATA_new.csv")


# In[59]:


cuis.to_csv("cusine_fulldataset_new.csv")


# In[ ]:


cusine_iamges=pd.DataFrame({"Cusine":z})
#cusine_iamges.to_csv("cusine_images.csv")


# In[ ]:


import requests
image=[]
for i in range(0,70):
    word=z[i].replace(" ", "_")
    link="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_288,h_360/v1674029859/PC_Creative%20refresh/3D_bau/banners_new/"+word+".png"
    response = requests.head(link)
    print(i)
    if response.status_code != 404:
        image.append(link)
    else:
        image.append(" ")
print(image)        

