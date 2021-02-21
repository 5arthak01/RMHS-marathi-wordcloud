import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.twentyfournews.com/page/2?s=farmers+protest')
bSoup = BeautifulSoup(page.content, 'html.parser')
links_list = bSoup.find_all('a')

for link in links_list:
    if 'href' in link.attrs:
        print(str(link.attrs['href']) + "\n")

# Please note that this code will print  every link in the page given as argument and the relevant urls must be sorted manually.
# Also, since this is a very elementary version, most sites will not display relevant information when this code is used.
