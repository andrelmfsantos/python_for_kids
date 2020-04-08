#!/usr/bin/env python
# coding: utf-8

# # First Calc

# In[1]:


def addition():
    first = float(input('I will add two numbers. Please, put the first number and press ENTER '))
    second = float(input('Now put the second number and press ENTER '))
    print(first + second)
    
def subtraction():
    first = float(input('I will subtract two numbers. Please, put on the first number and press ENTER '))
    second = float(input('Now put the second number and press ENTER '))
    print(first - second)
    
def division():
    first = float(input('I will divide two numbers. Please, put on the first number (dividend) and press ENTER '))
    second = float(input('Now put the second number (divider) and press ENTER '))
    print(first / second)

def multiplication():
    first = float(input('I will  multiply two numbers. Please, put on the first number and press ENTER '))
    second = float(input('Now put the second number and press ENTER '))
    print(first * second)


# ## Conditional Statements

# In[2]:


def calc_run():
    op = input('Choose just one signal for operation (+  -  *  / ) and press ENTER ')
    if op == '+':
        addition()
    elif op == '-':
        subtraction()
    elif op == '*':
        multiplication()
    elif op == '/':
        division()
    else:
        print('Just use the signals: (+ - * /), try again!')


# In[4]:


calc_run()


# In[ ]:




