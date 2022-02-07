#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector as conn
import csv
import pandas as pd


# # # CREATING A DATABASE

# In[3]:


mydb = conn.connect(host='localhost' ,user='abhi739',passwd='1212')
mydb


# In[ ]:


cursor.execute("CREATE DATABASE ineurondb")


# In[4]:


cursor = mydb.cursor()

cursor.execute('use ineurondb')
cursor.execute('show tables')
cursor.fetchall()


# # Size of the car.data file

# In[6]:


empdata = pd.read_csv('C:\\Users\\Admin\\iNeuron\\car.data', header=None, delimiter = ',')
print(empdata.head())
print(empdata.shape)


# # CHECKING MISSING VALUES USING PANDA

# In[7]:


empdata.isnull().sum()


# # Create cardata table

# In[8]:


cursor.execute('create table ineurondb.cardata(buying varchar(20), maint varchar(20), doors varchar(20), person varchar(20), lug_boot varchar(20), safety varchar(20), class varchar(20))')
mydb.commit()


# # Reading each row of the car file and inserting its tuple equivalent into table by column names

# In[9]:


for row in empdata.iterrows():
    testseries=row[1].values
    cursor.execute('insert into ineurondb.cardata(buying,maint,doors,person,lug_boot,safety,class)' 
                  "VALUES('%s','%s','%s','%s','%s','%s','%s')" %tuple(testseries))
    


# In[10]:


cursor.execute('describe ineurondb.cardata')
cursor.fetchall()


# # Comparing size of cardata with car.data file

# In[11]:


#Checking the total rows
cursor.execute('select count(*) from ineurondb.cardata')
print(cursor.fetchall())


# In[12]:


#checking the total number of colums
cursor.execute(f"select count(*) as number_of_columns from information_schema.columns where table_schema='ineurondb' AND table_name='cardata'")
cursor.fetchall()


# Hence Size of car.data file and cardata table dump is the same

# #  Group all the data with COL1 AND count occurences of each and every record based on col1 value 

# In[13]:


cursor.execute('select * from ineurondb.cardata limit 6')
cursor.fetchall()


# In[27]:


cursor.execute("select buying,maint,doors,person,lug_boot,safety,class, count(*) from ineurondb.cardata group by buying")
cursor.fetchall()


# In[28]:


# 432 unique values of each column when grouped by first column 'buying'


# # Filter a record where col 3 value will be 4

# In[29]:


cursor.execute("select * from ineurondb.cardata where doors='4'")
cursor.fetchall()


# # Update a col 3 value with 8 whereever you have value equal to 2 

# In[33]:


cursor.execute("Update ineurondb.cardata set doors=8 where doors='2'")
cursor.fetchall()


# In[36]:


cursor.execute("select * from ineurondb.cardata where doors='8'")
cursor.fetchall()


# #  Delete table 

# In[37]:


cursor.execute('drop table ineurondb.cardata')
mydb.commit()


# In[38]:


cursor.execute('show tables')
cursor.fetchall()


# # Delete the Database

# In[39]:


cursor.execute('drop database ineurondb')


# In[40]:


#checking if database is deleted
cursor.execute('use ineurondb')

#the database has been deleted

