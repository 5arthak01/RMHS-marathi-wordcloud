Note: This is a markdown file, and for better understanding nust be opened with an appropriate viewer

# RMHS Assignment 2 submission

Sarthak Agrawal - 2019115003

### Abstract

I have scraped TOI articles relevant to the farmer's protest, stored in file articles.csv

### Methodology

I have used [Scrapy](https://scrapy.org/) because I have experience with it, and it is considered as fast.

- Instructions to run/reproduce:

  - Scrapy and python are necessary
  - There are two spiders, coded in the files [scrape_url](./tutorial/spiders/scrape_url.py) and [scrape_art](./tutorial/spiders/scrape_art.py). The former scrapes the URLs of the articles and stores them in a file 'urls.txt'. The second spider scrapes each article and stores in 'articles.csv'
  - Run (while in current directory)

    ```
    scrapy crawl urls_spi
    python filter_urls.py
    scrapy crawl each_article

    ```
Pranoy J - 2019115004

### Abstract
I have scrapes facebook posts relevant to the farmers' protest from 2 facebook pages and they are in the excel file titled Facebook_posts, I have also scraped the  links and titles of news articles relating to the protest from 4 online news sites and they have been stored in the file urls.txt.

### Methodology

To get the links and the facebook posts, I used a tool named scrapestorm in its free version. It is a downlodable scraping tool with an easy to use user interface.

To obtain the links from the online news platforms, I used [BeautifulSoup] because the coding required was minimal. A drawback of the code I used is that it can only process 1 webpage at a time and the required links had to be segregated manually as every link in the webpage would be displayed on the terminal screen.

- Instructions to run the code:

```
  python3 parse_links.py

```

### Issues faced

- The downloadable tool I employed was quite easy to use but had multiple restrictions because I was on the free version. As such, the range of its usability was fairly limited.
- Initially I tried using BeautifulSoup to scrape links from facebook but the links to individual posts could not be obtained and I was forced to switch to other tools. However, this worked for the online news sites.
