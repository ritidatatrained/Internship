#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re


# In[5]:


#'Python Exercises, PHP exercises.'
#Expected Output: Python:Exercises::PHP:exercises:


text = "Python Exercises, PHP exercises."


text = text.replace(",", "").replace(".", "")


text = text.replace(" Exercises", ":Exercises::")

text = text.replace(" exercises", ":exercises:")

print(text)





# In[8]:


#Write a Python program to find all words starting with 'a' or 'e' in a given string.

string = 'Animal egg ant world decide event'
pattern =r'\b[aeAE]\w*\b'

matches = re.findall(pattern, string)
print(matches)





# In[18]:


#Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

import re

def find_4_words(text):
    pattern = re.compile(r'\b\w{4,}\b')
    matches = pattern.findall(text)
    return matches

string = "This is a simple example" 
result = find_4_words(string)
print(result)


# In[19]:


#Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

import re

def find_words(text):
    pattern = re.compile(r'\b\w{3,5}\b')
    matches = pattern.findall(text)
    return matches

string = "data science is a very good field for data analysis"

result = find_words(string)
print(result)




# In[ ]:


#Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
#Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
#Expected Output:
#example.com
#hr@fliprobo.com
#github.com
#Hello Data Science World
#Data Scientist




# In[ ]:


#Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
#Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
#Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
#Note- Store given sample text in the text file and then to remove the parenthesis area from the text.


# In[22]:


#Write a regular expression in Python to split a string into uppercase letters.
#Sample text: “ImportanceOfRegularExpressionsInPython”
#Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]


import re

text = "ImportanceOfRegularExpressionsInPython"
result = re.findall(r'[A-Z][a-z]*', text)

print(result)


# In[ ]:


#Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
#Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
#Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython


# In[ ]:


#Question 10- Write a python program to extract email address from the text stored in the text file using Regular Expression.
#Sample Text- Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com. 
#Please contact us at hr@fliprobo.com for further information. 
#Expected Output: 
['xyz@domain.com', 'xyz.abc@sdomain.domain.com']
['hr@fliprobo.com']


# In[23]:


#Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.


import re

strings_to_test = [
    "Valid_String_123",
    "anothervalidstring",
    "Invalid-String",
    "Not Valid",
    "Valid123",
    "A Valid String_",
]

pattern = r'^[A-Za-z0-9_]+$'

for s in strings_to_test:
    if re.match(pattern, s):
        print(f"'{s}' is a valid string.")
    else:
        print(f"'{s}' is not a valid string.")







# In[25]:


#Write a Python program where a string will start with a specific number. 

string = "82 is the answer."
number_to_check = "82"

if string.startswith(number_to_check):
    print(f"The string starts with {number_to_check}.")
else:
    print(f"The string does not start with {number_to_check}.")


# In[26]:


#Write a Python program to remove leading zeros from an IP address


ip_address = "192.168.001.001"
octets = ip_address.split('.')
cleaned_octets = [str(int(octet)) for octet in octets]
cleaned_ip_address = '.'.join(cleaned_octets)

print(cleaned_ip_address)






# In[6]:


#Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
#Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
#Expected Output- August 15th 1947
#Note- Store given sample text in the text file and then extract the date string asked format.




txt = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’."
x = re.search("August 15th 1947",txt)
print(x)


# In[1]:


#Write a Python program to search some literals strings in a string. 
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'



sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']

words_in_text = sample_text.split()
found_words = [word for word in searched_words if word in words_in_text]

print(f"Found words: {found_words}")


# In[2]:


sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = {'fox', 'dog', 'horse'}

found_words = searched_words.intersection(sample_text.split())

print(f"Found words: {found_words}")


# In[ ]:


#Write a Python program to search some literals strings in a string. 
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'


# In[7]:


#Write a Python program to find the substrings within a string.
#Sample text : 'Python exercises, PHP exercises, C# exercises'
#Pattern : 'exercises'.


text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print(match)


# In[11]:


#Write a Python program to find the occurrence and position of the substrings within a string.

import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print( s, e)


# In[7]:


#Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

input_date = input("Enter a date in yyyy-mm-dd format: ")

pattern = r"(\d{4})-(\d{2})-(\d{2})"
output_date = re.sub(pattern, r"\3-\2-\1", input_date)

print("Converted date:", output_date)


# In[ ]:


#Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.


# In[18]:


#Write a Python program to separate and print the numbers and their position of a given string.

text = "I have 23 boxes of oranges and 76 boxes of bananas"

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())
	


# In[8]:


#Write a regular expression in python program to extract maximum/largest numeric value from a string.
#Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
#Expected Output: 950


import re
#input
string='My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
#seperate number from string
number = re.findall('\d+', string)
#convert it into integer
number = map(int, number)
print("Max_value:",max(number))


# In[24]:


#Create a function in python to insert spaces between words starting with capital letters.
#Sample Text: “RegularExpressionIsAnImportantTopicInPython"
#Expected Output: Regular Expression Is An Important Topic In Python


   def capital_words_spaces(str1):
        return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)


print(capital_words_spaces("RegularExpressionIsAnImportantTopicInPython"))


# In[29]:


#Python regex to find sequences of one upper case letter followed by lower case letters

text = "This Is a Sample Text With Several Sequences Of Upper and Lowercase Letters "

pattern = r"[A-Z][a-z]+"

sequence = re.findall(pattern, text)
print(sequence)


# In[34]:


#Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
#Sample Text: "Hello hello world world"
#Expected Output: Hello hello world


sample_text = "Hello hello world world"

output_text = re.sub(r'\b(\w+)( \1\b)+', r'\1', sample_text)
print("Expected Output:", output_text)


# In[17]:


#Write a python program using RegEx to accept string ending with alphanumeric character.




input_string = input("Enter a string: ")

pattern = r".*[a-zA-Z0-9]$"

if re.match(pattern, input_string):
    print("The string ends with an alphanumeric character.")
else:
    print("The string does not end with an alphanumeric character.")


# In[16]:


#-Write a python program using RegEx to extract the hashtags.
#Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
#Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']



sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

hashtags = re.findall(r'#\w+', sample_text)

print("Hashtags extracted from the text:", hashtags)


# In[4]:


#Write a python program using RegEx to remove <U+..> like symbols
#Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
#Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
#Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders




sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"

cleaned_text = re.sub(r'<U\+[A-Z0-9]+>', '', sample_text)

print("Expected Output:", cleaned_text)


# In[5]:


#Write a python program to extract dates from the text stored in the text file.
#Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
#Note- Store this sample text in the file and then extract dates.

sample_text = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."

dates = re.findall(r'\d{2}-\d{2}-\d{4}', sample_text)
print(dates)



# In[6]:


sample_text = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."


with open("sample_text.txt", "w") as file:
    file.write(sample_text)


with open("sample_text.txt", "r") as file:
    text = file.read()


dates = re.findall(r'\d{2}-\d{2}-\d{4}', text)

# Print the extracted dates
print(dates)





# In[6]:


#Create a function in python to remove all words from a string of length between 2 and 4.
#The use of the re.compile() method is mandatory.
#Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.



def removewords_between_length(text):
    pattern = re.compile(r'\b\w{2,4}\b')
    return pattern.sub('', text)

sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
expected_output = " following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly."

result = removewords_between_length(sample_text)
print(result)


# In[ ]:




