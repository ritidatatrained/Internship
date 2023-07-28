#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re

#Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).


# In[12]:


string = 'abcdefgJKLY56789'
pattern= r'^[a-zA-Z0-9]+$'
result =re.findall(pattern,string)
print(result)


# In[6]:


#Create a function in python that matches a string that has an a followed by zero or more b's

import re

def match_ab(input_string):
    pattern = r'ab*'  # Regular expression pattern for 'a' followed by zero or more 'b's
    if re.match(pattern, input_string):
        return True
    else:
        return False

# Test the function
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    if match_ab(input_string):
        print("The string matches the pattern 'a' followed by zero or more 'b's.")
    else:
        print("The string does not match the pattern.")


# In[7]:


#Create a function in python that matches a string that has an a followed by zero or more b's


string = 'abbbcbbb'
pattern = 'ab+'
result =re.findall(pattern,string)
print(result)


# In[19]:


#Write a RegEx pattern that matches a string that has an a followed by zero or one 'b'.

string = 'hello big world'
pattern = 'b+?'
result =re.findall(pattern,string)
print(result)


# In[28]:


#Write a RegEx pattern in python program that matches a string that has an a followed by three 'b'.

string = 'big box has bbbunch of bananas'
pattern = 'b{3}'
result =re.findall(pattern,string)
print(result)


# In[29]:


#Write a RegEx pattern in python program that matches a string that has an a followed by two to three 'b'

string = 'bbig bbox has bbbunch of bananas'
pattern = 'b{2,3}'

result =re.findall(pattern,string)
print(result)


# In[44]:


#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
string =  'acccbbdb'
pattern = '^a.*b$'
result =re.findall(pattern,string)
print(result)


# In[27]:


#Write a RegEx pattern in python program that matches a word at the beginning of a string.

target_string = 'hello world'
result = re.match(r"\w{5}",target_string)
print(result)


# In[7]:


Write a RegEx pattern in python program that matches a word at the end of a string

import re
s = 'datacience is a great platform to enhance your skills'
result = re.search(r'\w+$', s)
print(result.group())


# In[11]:


#Write a RegEx pattern in python program to find all words that are 4 digits long in a string.

#Sample text- '01 0132 231875 1458 301 2725.'

#Expected output- ['0132', '1458', '2725']

string = '01 0132 231875 1458 301 2725'
pattern = r'\b\d{4}\b'
result = re.findall(pattern,string)
print(result)


# In[ ]:




