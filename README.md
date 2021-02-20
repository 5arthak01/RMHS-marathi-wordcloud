Note: This is a markdown file, and for better understanding nust be opened with an appropriate viewer

# RMHS Assignment 2 submission

Sarthak Agrawal - 2019115003

### Methodology

I have used [Scrapy](https://scrapy.org/) because I have experience with it, and it is considered as fast.

###### Loksatta articles

The `loksatta_articles.csv` file does not have a header and has `~` as delimiter. It has columns in the following order:

1. title
2. description
3. date
4. content

`all_loksatta_articles.csv` has headers and `|` as delimiter.

- Instructions to run/reproduce:

  - Scrapy and python are necessary
  - There are two spiders, coded in the files [scrape_url](./tutorial/spiders/scrape_url.py) and [scrape_art](./tutorial/spiders/scrape_art.py). The former scrapes the URLs of the articles and stores them in a file 'urls.txt'. The second spider scrapes each article and stores in 'articles.csv'
  - Run (while in current directory)

    ```
    scrapy crawl urls_spi
    python filter_urls.py
    scrapy crawl each_article

    ```
