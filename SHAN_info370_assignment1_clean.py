
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# remove all measurement
def measureRemover(copy):
    copy.Ingredients = copy.Ingredients.str.replace(r'^\s*', '')
    copy.Ingredients = copy.Ingredients.str.replace(r'can\w*', '').str.replace(r'teaspoon\w*', '').str.replace(r'tablespoon\w*', '').str.replace(r'tbsp\D ', '').str.replace(r'tbsp', '').str.replace(r'tsp.', '').str.replace(r'cup\w*', '').str.replace(r'cup', '').str.replace(r'pint\w*', '')
    copy.Ingredients = copy.Ingredients.str.replace(r'pound\w*', '').str.replace(r'ounce\w*', '').str.replace(r'oz.', '').str.replace(r'clove\w*', '').str.replace(r'pinch\w*', '').str.replace(r'Pinch\w*', '').str.replace(r'jar\w*', '').str.replace(r'dash\w*', '')
    copy.Ingredients = copy.Ingredients.str.replace(r'large', '').str.replace(r'small', '').str.replace(r'whole', '').str.replace(r'plus', '').str.replace(r'slice\w*', '').str.replace(r'loaf\w* ', '').str.replace(r'handful\w*', '').str.replace(r'half', '')
    copy.Ingredients = copy.Ingredients.str.replace(r'^\s*', '')
    copy.Ingredients = copy.Ingredients.str.replace(r'^(of )', '').str.replace(r'^(to )', '').str.replace(r'(((?:[A-Z][a-z]+))) of', '')
    copy.Ingredients = copy.Ingredients.str.replace(r'^\s*', '')
    return copy


# In[3]:


#remove all prep method
def prepRemover(copy):
    copy.Ingredients = copy.Ingredients.str.replace(r'^\s*', '')                         
    copy.Ingredients = copy.Ingredients.str.replace(r'shred\w*', '').str.replace(r'Shred\w*', '').str.replace(r'sliced\w*', '').str.replace(r'Sliced\w*', '')
    copy.Ingredients = copy.Ingredients.str.replace(r'diced\w*', '').str.replace(r'Diced\w*', '').str.replace(r'minced\w*', '').str.replace(r'Minced\w*', '')
    copy.Ingredients = copy.Ingredients.str.replace(r'ground\w*', '').str.replace(r'Ground\w*', '').str.replace(r'uncooked\w*', '').str.replace(r'Uncooked\w*', '')
    copy.Ingredients = copy.Ingredients.str.replace(r'chopped\w*', '').str.replace(r'Chopped\w*', '').str.replace(r'cooked\w*', '').str.replace(r'Cooked\w*', '')
    copy.Ingredients = copy.Ingredients.str.replace(r'fresh\w*', '').str.replace(r'Fresh\w*', '').str.replace(r'fine\w*', '').str.replace(r'Fine\w*', '')
    copy.Ingredients = copy.Ingredients.str.replace(r'thinly\w*', '').str.replace(r'Thinly\w*', '').str.replace(r'fine\w*', '').str.replace(r'Fine\w*', '')    
    copy.Ingredients = copy.Ingredients.str.replace(r'^\s*', '')
    return copy


# In[4]:


def cleanerMain():
    rawData = pd.read_csv('SHAN_info370_assignment1_rawData.csv', index_col=0)
    rawCopy = rawData.copy()
    # remove all the numbers
    rawCopy.Ingredients = rawCopy.Ingredients.str.replace(r'\d', '').str.replace(r'one ', '').str.replace(r'several', '')
    # remove all special character like ½
    rawCopy.Ingredients = rawCopy.Ingredients.str.replace(r'½ ', '').str.replace(r'¼ ', '').str.replace(r'¾ ', '')
    # remove everything after a comma becuase the content only has the preping method
    rawCopy.Ingredients = rawCopy.Ingredients.str.replace(r'\,.*$', '')
    # remove all /, -, and +
    rawCopy.Ingredients = rawCopy.Ingredients.str.replace(r'\/', '').str.replace(r'\-', '').str.replace(r'\+', '')
    # remove all () and everything before
    rawCopy.Ingredients = rawCopy.Ingredients.str.replace(r'\(.*\)', '').str.replace(r'(((?:[a-z][a-z]+))) \(.*\) ', '')
    # remove all measurement
    rawCopy = measureRemover(rawCopy)
    # remove * and ()
    rawCopy.Ingredients = rawCopy.Ingredients.str.replace(r'\*', '')
    rawCopy.Ingredients = rawCopy.Ingredients.str.replace(r'\,.*$', '').str.replace(r'\(.*$', '')
    # remove spaces at the beginning of line
    rawCopy.Ingredients = rawCopy.Ingredients.str.replace(r'^\s*', '') 
    # remove all preping method
    rawCopy = prepRemover(rawCopy)
    # export to csv file
    rawCopy.to_csv('SHAN_info370_assignment1_clean.csv')

