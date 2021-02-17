#%%
# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import re


#%%
html = requests.get(
    'https://vgsales.fandom.com/wiki/List_of_highest-grossing_video_games')
soup = BeautifulSoup(html.text, 'html5lib')
soup.text


# %%
# find <tr><td><a class=extiw" GameTitle></td></tr>
table = soup('table')


#%%
rows = []
titles = []

for row in soup.find_all('tr'):
    rows.append(row)
    for column in row.find_all('td'):
        titles.append(column('a', {'class': 'extiw'}))
        rows.append(column)
    # for item in row.find_all

#%%
rows[1]


# %%
columns = ['title', 'Gross(w/o inflation), Release Year',
           'Gross(as of year)', 'Gross(w/ inflation)', 'Genre']
