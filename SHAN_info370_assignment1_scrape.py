
# coding: utf-8

# In[1]:


import pandas as pd;
import requests;
import re
from bs4 import BeautifulSoup


# In[2]:


# A function that scrapes url of individual individual page from the main page
# @param: a string of URL of the main page
# @return a list of names of recipes, a list of url of recipes
def nameURLScraper(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = []
    names = []
    for each in soup.find_all('div', attrs={'class': 'archive-post'}):
        for i in each.find_all('h4', attrs={'class':'title'}):
            names.append(i.get_text())
        for j in each.find_all('a', attrs={'href':re.compile("^https://")}):
            links.append(j.get('href'))
    return names, links


# In[3]:


# A function that scrapes ingredients from individual recipe page
# @param: a string of URL of individual recipe page
# @return: a list of uncleaned ingredients
def ingredientScraper(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser') 
    ingredient = soup.find_all('li', attrs={'class':'ingredient'})
    ingredients = []
    for each in ingredient:
        ingredients.append(each.get_text())
    return ingredients


# In[4]:


# A function that scrapes URLs of all pages
# @param: a URL of the main page
# @return: a list of URLs of pages(main page included)
def pageURLScraper(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    pages = [url]
    for each in soup.find_all('div', attrs={'class': 'nav-links'}):
        for i in each.find_all('a', attrs={'href':re.compile("^https://")}):
            if i.get('href') not in pages:
                pages.append(i.get('href'))
    return pages


# In[5]:


# The main function that scrapes all the recipes from the given URLs
# @param: two string of URLs that need to be scraped
# @return: a dataframe of all ingredients, corresponding url and name, a list of all name, a list of all URL
# @return: the function will produce a .csv file from the dataframe returned
def scraperMain(mainURL, secondURL):
    mainList = pageURLScraper(mainURL)
    secondList = pageURLScraper(secondURL)
    pageList = mainList + secondList
    ingredientsFrame = pd.DataFrame()
    allNames = pd.DataFrame()
    allURL = pd.DataFrame()
    for each in pageList:
        curNames, curLists = nameURLScraper(each)
        allNames = allNames.append(curNames)
        allURL = allURL.append(curLists)
        for i in range(0, len(curLists)-1):
            curIngredients = ingredientScraper(curLists[i])
            ingredientsFrame = ingredientsFrame.append(
                pd.DataFrame({'Name': curNames[i], 'Ingredients': curIngredients, 'URL': curLists[i]}))
    # remove redundant indexing
    ingredientsFrame = ingredientsFrame.reset_index(drop=True)
    #sort columns into right order
    ingredientsFrame = ingredientsFrame[['URL', 'Name', 'Ingredients']]
    ingredientsFrame.to_csv("SHAN_info370_assignment1_rawData.csv", encoding='utf-8')

