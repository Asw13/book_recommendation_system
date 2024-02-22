#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df1=pd.read_csv("Dataset (1)/Books.csv",low_memory=False)
df2=pd.read_csv("Dataset (1)/Ratings.csv",low_memory=False)
df3=pd.read_csv("Dataset (1)/Users.csv",low_memory=False)
df1
#df2
#df3


# In[3]:


df1['Year-Of-Publication'].unique()


# In[4]:


df1.loc[df1['Year-Of-Publication'] == 'DK Publishing Inc',:]

### replacing the pubisher with the year

# In[5]:


df1.loc[df1['ISBN']== '0789466953','Year-Of-Publication']=2000
df1.loc[df1["ISBN"]=='0789466953','Book-Author']="James Buckley"  
df1.loc[df1["ISBN"]=='0789466953','Publisher']='DK Publishing Inc'
df1.loc[df1["ISBN"]=="0789466953","Book-Title"]='DK Readers: Creating the X-Men, How Comic Book'


# In[6]:


df1.loc[df1['ISBN']== '0789466953','Year-Of-Publication']=2000
df1.loc[df1["ISBN"]=='0789466953','Book-Author']="michael Teiteibaum"
df1.loc[df1["ISBN"]=='0789466953','Publisher']='DK Publishing Inc'
df1.loc[df1["ISBN"]=="0789466953","Book-Title"]='DK Readers: Creating the X-Men, How It All Beg'


# In[7]:


df1.loc[df1['Year-Of-Publication'] == 'Gallimard',:]


# In[8]:


df1.loc[df1['ISBN']== '078946697X','Year-Of-Publication']=2000
df1.loc[df1["ISBN"]=='078946697X','Book-Author']="Jean-Marie Gustave Le ClÃƒ?Ã‚Â©zio"
df1.loc[df1["ISBN"]=='078946697X','Publisher']='Gallimard'
df1.loc[df1["ISBN"]=="078946697X","Book-Title"]="Peuple du ciel, suivi de 'Les Bergers"


# In[9]:


df1["Year-Of-Publication"]=pd.to_numeric(df1['Year-Of-Publication'],errors='coerce')
print(sorted(df1["Year-Of-Publication"].unique()))


# In[10]:


df1["Year-Of-Publication"].unique()


# In[11]:


df1["Year-Of-Publication"].fillna(round(df1["Year-Of-Publication"].mean()),inplace=True)
df1["Year-Of-Publication"].unique()


# In[12]:


df2


# In[13]:


df3


# In[14]:


df2_new=df2.merge(df3,on="User-ID")
df2_new


# In[15]:


df2_new.shape


# In[16]:


df3.shape


# In[17]:


df2["User-ID"].duplicated()## finding duplicate values in the df2 data set


# In[18]:


df3["User-ID"].duplicated()


# In[19]:


df2.duplicated()


# In[20]:


df=df2_new.merge(df1,on="ISBN")
df


# In[21]:


df.shape


# In[22]:


len(df) ## totsl no of user ids


# In[23]:


len(df["User-ID"].unique()) ### unique user id s


# In[24]:


df["User-ID"].duplicated()


# In[25]:


df_sort=df.sort_values("User-ID")## sorting the user ids
df_sort


# In[26]:


df_sort["Age"].describe()


# In[27]:


df_sort["Age"].mode()  ## checking mode 


# In[28]:


df_sort["Age"].median()  ## checking median


# In[29]:


df_sort.isnull().values.any() ## checking is their any null values


# In[30]:


df.isnull().sum() ## counting how many null valies in the each column


# In[31]:


df_sort["Age"].fillna(value=int(df_sort["Age"].mean()),inplace=True) ## filling ag null values with mode 


# In[32]:


df_sort


# In[33]:


df_sort[df_sort['Publisher'].isnull()] ##extracting only which row have null vallues at particular column


# In[34]:


df_sort[df_sort["Book-Author"].isnull()]


# In[35]:


df_sort[df_sort["Image-URL-L"].isnull()]


# In[36]:


df_sort["Book-Author"].mode() 


# In[37]:


df_sort["Publisher"].mode()


# In[38]:


df_sort["Book-Author"].fillna(value=str(df_sort["Book-Author"].mode()),inplace=True) ## filling ag null values with mode 


# In[39]:


df_sort["Publisher"].fillna(value=str(df_sort["Publisher"].mode()),inplace=True) ## filling ag null values with mode 


# In[40]:


df_cleaned=df_sort.drop(["Image-URL-S",'Image-URL-M',"Image-URL-L"], axis=1)  ## droping the unwanted columns
df_cleaned


# In[41]:


df_cleaned["Book-Rating"].value_counts() ### rating given by the users


# In[42]:


df_cleaned.isnull().sum()


# In[43]:


df_cleaned.info()


# In[44]:


df_cleaned.describe()


# In[45]:


df_cleaned["Book-Title"].value_counts()


# In[46]:


#EDA


# In[ ]:





# In[47]:


df_cleaned.hist(None)


# In[ ]:


top=df_cleaned[df_cleaned["Book-Rating"]>0]
plt.style.use("seaborn-whitegrid")
plt.figure(figsize=(15,15))
sns.barplot(x="Book-Rating",y="Book-Title",data=df_cleaned,palette="inferno")


# In[ ]:


df_cleaned.groupby(['Book-Title']).sum().plot(kind='pie',y='y' )


# In[ ]:


sns.countplot(data=df_cleaned,x="Book-Rating")
plt.show()


# In[ ]:









