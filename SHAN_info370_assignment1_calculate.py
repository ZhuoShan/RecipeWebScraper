
# coding: utf-8

# In[1]:


import pandas as pd


# In[15]:


# a calculator function that get the names, counts and proportions of top 10 most used ingredients
def calculatorMain():
    rawData = pd.read_csv('SHAN_info370_assignment1_cleanData.csv', index_col=0)
    rawCopy = rawData.copy()
    # get top 10 most used ingredients' names
    mostIngredients = rawCopy['Ingredients'].value_counts()[0:10].index.tolist()
    # get top 10 most used infredients counts
    mostCounts = rawCopy['Ingredients'].value_counts()[0:10].tolist()
    # calculate proportion
    proportion = []
    for value in mostCounts:
        proportion.append("{0:.3f}".format(float(value)/180))
    calculatedFrame = pd.DataFrame({'word': mostIngredients, 'count': mostCounts, 'proportion': proportion})
    # sort the order of columns
    calculatedFrame = calculatedFrame[['word', 'count', 'proportion']]
    # export to csv file
    calculatedFrame.to_csv('SHAN_info370_assignment1_calculate.csv', index = False)

