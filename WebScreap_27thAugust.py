#!/usr/bin/env python
# coding: utf-8

# In[2]:


# q1

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open the website
driver.get("https://www.shine.com/")

# Find and fill in the search fields
job_title_input = driver.find_element(By.NAME, "search")
job_location_input = driver.find_element(By.ID, "id_q_2")

job_title_input.send_keys("Data Analyst")
job_location_input.send_keys("Bangalore")

# Click the search button
search_button = driver.find_element(By.ID, "btn-search-home")
search_button.click()

# Wait for the results to load
driver.implicitly_wait(10)

# Extract job details
job_elements = driver.find_elements(By.CLASS_NAME, "result-display__profile")
job_data = []

for job_element in job_elements[:10]:
    job_title = job_element.find_element(By.CLASS_NAME, "result-display__profile__job-title").text
    job_location = job_element.find_element(By.CLASS_NAME, "result-display__profile__location").text
    company_name = job_element.find_element(By.CLASS_NAME, "result-display__profile__company-name").text
    experience_required = job_element.find_element(By.CLASS_NAME, "result-display__profile__experience").text

    job_data.append({
        "Job Title": job_title,
        "Job Location": job_location,
        "Company Name": company_name,
        "Experience Required": experience_required
    })

# Create a DataFrame
df = pd.DataFrame(job_data)

# Print the DataFrame
print(df)

# Close the browser window
driver.quit()


# In[ ]:


#q2

import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open the website
driver.get("https://www.shine.com/")

# Find and fill in the search fields
job_title_input = driver.find_element_by_name("search")
job_location_input = driver.find_element_by_id("id_q_2")

job_title_input.send_keys("Data Scientist")
job_location_input.send_keys("Bangalore")

# Click the search button
search_button = driver.find_element_by_id("btn-search-home")
search_button.click()

# Wait for the results to load
driver.implicitly_wait(10)

# Extract job details
job_elements = driver.find_elements_by_class_name("result-display__profile")
job_data = []

for job_element in job_elements[:10]:
    job_title = job_element.find_element_by_class_name("result-display__profile__job-title").text
    job_location = job_element.find_element_by_class_name("result-display__profile__location").text
    company_name = job_element.find_element_by_class_name("result-display__profile__company-name").text

    job_data.append({
        "Job Title": job_title,
        "Job Location": job_location,
        "Company Name": company_name
    })

# Create a DataFrame
df = pd.DataFrame(job_data)

# Print the DataFrame
print(df)

# Close the browser window
driver.quit()


# In[ ]:


#q4

import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open the website
driver.get("https://www.flipkart.com/")

# Close the login popup if it appears
try:
    close_button = driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']")
    close_button.click()
except:
    pass

# Search for sunglasses
search_box = driver.find_element_by_name("q")
search_box.send_keys("sunglasses")
search_box.submit()

# Wait for the results to load
driver.implicitly_wait(10)

# Scroll to load more results
for _ in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(5)

# Extract sunglasses details
sunglasses_listings = driver.find_elements_by_css_selector("div._2kHMtA")

sunglasses_data = []

for listing in sunglasses_listings[:100]:
    brand = listing.find_element_by_css_selector("div._2WkVRV").text
    description = listing.find_element_by_css_selector("a.IRpwTa").text
    price = listing.find_element_by_css_selector("div._30jeq3").text

    sunglasses_data.append({
        "Brand": brand,
        "Product Description": description,
        "Price": price
    })

# Create a DataFrame
df = pd.DataFrame(sunglasses_data)

# Print the DataFrame
print(df)

# Close the browser window
driver.quit()


# In[4]:


#q6


import requests
from bs4 import BeautifulSoup

# URL to the search results page
url = "https://www.flipkart.com/search?q=sneakers"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find sneaker listings
sneaker_listings = soup.find_all("div", class_="_1AtVbE")

sneaker_data = []

for listing in sneaker_listings[:100]:
    brand = listing.find("div", class_="_2WkVRV").text
    description = listing.find("a", class_="IRpwTa").text
    price = listing.find("div", class_="_30jeq3").text

    sneaker_data.append({
        "Brand": brand,
        "Product Description": description,
        "Price": price
    })

# Print or process the scraped data
for sneaker in sneaker_data:
    print(sneaker)


# In[ ]:




