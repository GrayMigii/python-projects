#!/usr/bin/env python3

import pandas as pd
import requests
from bs4 import BeautifulSoup

dict = {'Title': [], 'Score': []}

source = requests.get('https://myanimelist.net/topanime.php').text

soup = BeautifulSoup(source, 'lxml')
# lxml is a parser that needs to be installed first

# finds all titles and scores from the top anime mal page
titles = soup.find_all('h3', class_='hoverinfo_trigger')
scores = soup.find_all('span', class_='score-label')

# loops through the titles and scores and appends them to the dictionary
for title in titles:
    dict['Title'].append(title.text)

for score in scores:
    dict['Score'].append(score.text) if score.text != 'N/A' else None

# turns the dictionary into a dataframe
df = pd.DataFrame(dict, index=[x for x in range(1, 51)])

print(df)
