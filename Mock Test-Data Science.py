#!/usr/bin/env python
# coding: utf-8

# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers from the input list. Use list comprehension to solve this problem.

# In[1]:


list =[1,2,3,4,5,6,7,8,9,10]


# In[2]:


newlist =[]


# In[3]:


newlist = [x for x in list if x%2==0]


# In[4]:


newlist


# Implement a decorator function called ‘timer’ that measures the execution time of a function. The ‘timer’ decorator should print the time taken by the decorated function to execute. Use the ‘time’ module in Python to calculate the execution time.

# In[6]:


import time


# import time
# 
# def timer(func):
#     def wrapper():
#         begin = time.time()
#         func()  
#         end = time.time()
#         print("Total time taken in", func.__name__, ":", end - begin)
#     return wrapper
# 
# @timer
# def my_function():
#     
#     time.sleep(2)
# 
# my_function()

# In[ ]:





# Write a function called ‘calculate_mean’ that takes a list of numbers as input and returns the mean (average) of the numbers. The function should calculate the mean using the sum of the numbers divided by the total count.

# In[18]:


def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

data = [10, 15, 20, 25, 30]

lst = []

n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input())
    lst.append(ele) 
 
print(lst)

mean_value = calculate_mean(lst)
print("Mean:", mean_value)


# Write a function called ‘perform_hypothesis_test’ that takes two lists of numbers as input, representing two samples. The function should perform a two-sample t-test and return the p-value. Use the ‘scipy.stats’ module in Python to calculate the t-test and p-value.

# In[21]:


from scipy import stats

def perform_hypothesis_test(lst1, lst2):
    t_statistic, p_value = stats.ttest_ind(lst1, lst2)
    return p_value

sample1 = [5, 10, 15, 20, 25]
sample2 = [10, 20, 30, 40, 50]

lst1 = []

n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input("Sample 1"))
    lst1.append(ele) 
 
print(lst1)

lst2 = []

for i in range(0, n):
    ele = int(input("Sample 2"))
    lst2.append(ele) 
 
print(lst2)


p_value = perform_hypothesis_test(lst1, lst2)
print("P-value:", p_value)


# In[ ]:




