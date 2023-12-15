# import pandas as pd
# import requests
# from bs4 import BeautifulSoup

# URL = "https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav"


# headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

# webpage = requests.get(url = URL, headers=headers).text

# soup = BeautifulSoup(webpage , 'lxml')


# print(soup.prettify())


import seaborn as sns


sns.load_dataset("flights").head()


