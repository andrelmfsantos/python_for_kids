#!/usr/bin/env python
# coding: utf-8

# In[1]:


# three lists:
fruit = ['apple', 'banana', 'kiwi', 'dragondfruit']
years = [2012, 2013, 2014, 2015]
students_in_class = [30, 22, 28, 33]
computer_class = ['Cynthia', 78, 42, 'Raj', 98, 24, 35, 'Kadeem', 'Rachel']


# In[2]:


print(type(fruit),type(years),type(students_in_class),type(computer_class))


# In[3]:


print('fruit:            ',type(fruit))
print('years:            ',type(years))
print('students_in_class:',type(students_in_class))
print('computer_class:   ',type(computer_class))


# In[4]:


# Index:
#               ['apple', 'banana', 'kiwi', 'dragondfruit']
# Left to right    0          1       2            3
# Right to left   -4         -3      -2           -1
#--------------------------------------------
len(fruit) # lenght


# In[5]:


# List's Elements
fruit[1:len(fruit)]


# In[6]:


# Adding itemns to the list
fruit.append('orange')
print(fruit)


# In[7]:


# Removing items from the list
fruit.remove('dragondfruit') # or fruit.remove(fruit[3])
print(fruit)


# In[8]:


# Lists and loops
colors = ['green', 'yellow', 'red']


# In[9]:


for color in colors:
    print('I see ' + color + '.')


# ## Dictionaries

# In[10]:


numbers = {'one': 1, 'two': 2, 'three': 3}


# In[13]:


numbers['one']


# In[14]:


items = {'arrows': 200, 'rocks': 25, 'food': 15, 'lives': 2}


# In[17]:


type(items)


# In[22]:


items['fireball'] = 10


# In[23]:


print(items)


# In[24]:


# Changing the value of an existing item
items.update({'rocks': 10})
print(items)


# In[25]:


# Removing items from the dictionary
del items['lives']
print(items)

