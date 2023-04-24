#!/usr/bin/env python3

import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys
import math

arg_list = sys.argv
df_length = 50 if len(arg_list) == 1 else int(arg_list[1])
pd.options.display.max_rows = df_length

titles = []
unf_scores = []
dict = {'Title': [], 'Score': []}

# loops through the mal top anime pages
for i in range(1, math.ceil(df_length/50) + 1):
    if i == 1:
        source = requests.get('https://myanimelist.net/topanime.php').text
    else:
        source = requests.get(f'https://myanimelist.net/topanime.php?limit={50*i}').text

    # lxml is a parser that needs to be installed first
    soup = BeautifulSoup(source, 'lxml')

    # finds all titles and scores from the top anime mal page
    titles += soup.find_all('h3', class_='hoverinfo_trigger')
    unf_scores += soup.find_all('span', class_='score-label')

# loops through the titles and scores and appends them to the dictionary
scores = list(filter(lambda x: 'N/A' not in x, unf_scores))

for title in titles[:df_length]:
    dict['Title'].append(title.text)

for score in scores[:df_length]:
    dict['Score'].append(score.text)
# turns the dictionary into a dataframe
df = pd.DataFrame(dict, index=[x for x in range(1, df_length + 1)])

print(df)
