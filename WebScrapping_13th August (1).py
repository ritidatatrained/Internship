#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install requests
pip install beautifulsoup4
pip install pandas


# In[4]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# Send a GET request to fetch the HTML content of the page
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all header tags (h1, h2, h3, h4, h5, h6)
header_tags = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

# Extract the text content from header tags and store in a list
header_texts = [tag.get_text() for tag in header_tags]

# Create a DataFrame from the extracted header texts
data = {"Header": header_texts}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# In[9]:


import pandas as pd

# Sample HTML data for demonstration (replace with actual URL)
url = "https://presidentofindia.nic.in/former-presidents.htm"

# Create a BeautifulSoup object
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_data, "html.parser")

# Initialize lists to store data
names = []
terms = []

# Extract data from the table
table = soup.find("table", {"class": "tablepress"})
for row in table.find_all("tr")[1:]:
    columns = row.find_all("td")
    names.append(columns[0].get_text())
    terms.append(columns[1].get_text())

# Create a DataFrame
data = {"Name": names, "Term of Office": terms}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# In[13]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for the CNBC world news page
url = "https://www.cnbc.com/world/?region=world"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Initialize lists to store the news details
headlines = []
times = []
news_links = []

# Find the news articles
articles = soup.find_all("div", class_="Card-titleContainer")
for article in articles:
    headline = article.find("a", class_="Card-titleLink")
    time = article.find("time", class_="Card-time")
    
    if headline and time:
        headlines.append(headline.text.strip())
        times.append(time.text.strip())
        news_links.append("https://www.cnbc.com" + headline['href'])

# Create a DataFrame
data = {
    "Headline": headlines,
    "Time": times,
    "News Link": news_links
}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# In[14]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for most downloaded articles in the last 90 days
url = "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Initialize lists to store the article details
titles = []
authors = []
published_dates = []
paper_urls = []

# Find the article items
articles = soup.find_all("li", class_="pod-listing")
for article in articles:
    title = article.find("h3", class_="pod-listing-header").text.strip()
    author = article.find("ul", class_="author-list").text.strip()
    date = article.find("span", class_="pod-listing-secondary-text").text.strip()
    paper_url = article.find("a", class_="pod-listing-title")['href']
    
    titles.append(title)
    authors.append(author)
    published_dates.append(date)
    paper_urls.append(paper_url)

# Create a DataFrame
data = {
    "Paper Title": titles,
    "Authors": authors,
    "Published Date": published_dates,
    "Paper URL": paper_urls
}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# In[ ]:




