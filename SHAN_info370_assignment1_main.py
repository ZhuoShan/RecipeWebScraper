
# coding: utf-8

# In[1]:


from SHAN_info370_assignment1_scrape import *
from SHAN_info370_assignment1_clean import *
from SHAN_info370_assignment1_calculate import *


# In[2]:


# two urls that needs to be scraped
# I use two urls because one does not have enough recipes to scrape. Two URLs combined have 180 recipes
mainURL = "https://www.spoonfulofflavor.com/category/main-dish"
secondURL = "https://www.spoonfulofflavor.com/category/breakfast/"


# In[3]:


# main function from scrape file that scrapes and export all the raw data
# param: two strings of URL
scraperMain(mainURL, secondURL)


# In[4]:


# main function from clean file that clean all the raw data and export to another clean csv
cleanerMain()


# In[5]:


# main function from calculate file that calculate the top 10 most used ingredients' names, counts, and proportions
# calculated data will be exported to another calculate csv
calculatorMain()

