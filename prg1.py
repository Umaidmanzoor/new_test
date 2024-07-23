#!/usr/bin/env python
# coding: utf-8

# In[7]:


def add(a,d):
    return a+b
def sub(c,d):
    return c-d
def mul(e,f):
    return e*f
def div(g,h):
    return g/h
print("=================")
print("1. TO PERFORM ADDITITON")
print("2. TO PERFORM SUBTRACTION")
print("3. TO PERFORM MULTIPICATION")
print("4. TO PERFORM DIVISION")
print("=================")
choice = int(input("Enter Your choice"))
if choice ==1:
    a=int(input("Enter the 1st value"))
    b=int(input("Enter the 2nd value"))
    print(add(a,b))
elif choice ==2:
    c=int(input("Enter the 1st value"))
    d=int(input("Enter the 2nd value"))
    print(sub(c,d))
elif choice ==3:
    e=int(input("Enter the 1st value"))
    f=int(input("Enter the 2nd value"))
    print(mul(e,f))
elif choice ==4:
    g=int(input("Enter the 1st value"))
    h=int(input("Enter the 2nd value"))
    print(div(g,h))
else:
    print("wrong choice")


# In[10]:


# Program to check if a string is palindrome or not

#my_str = 'Malayalam'

my_str=input("Enter the string")

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


# In[12]:


# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[15]:


list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
if(list1==list2):
    print("True")
else:
    print("False")
    


# In[ ]:
