Note: This is a markdown file, and for better understanding nust be opened with an appropriate viewer

# RMHS Assignment 2 submission

Sarthak Agrawal - 2019115003

### Methodology

Technology used is [Scrapy](https://scrapy.org/) because it is considered extremely fast, and allows both precision and accuracy since we can use CSS selectors to target elements.

### Articles archive

- Loksatta
  The `loksatta_articles.csv` file does not have a header and has `~` as delimiter. It has columns title, description, date, content (in this order). File `all_loksatta_articles.csv` has these headers as the first line and `|` as delimiter, with the addition of URLs for each article as the first column.
- Maharashtra times
  `maharashtra_times_articles.csv` does not have a header and has the columns title, author, date, highlights, content (in this order) and `|` as delimiter. File `all_mt_times_articles.csv` has these headers as the first line, with the addition of URLs for each article as the first column.

- Instructions to run/reproduce:

  - Scrapy and python are necessary
  - There are two spiders, coded in the files [scrape_url](./tutorial/spiders/scrape_url.py) and [scrape_art](./tutorial/spiders/scrape_art.py). The former scrapes the URLs of the articles and stores them in a file 'urls.txt'. The second spider scrapes each article and stores in 'articles.csv'
  - Run (while in current directory)

    ```
    scrapy crawl urls_spi
    python filter_urls.py
    scrapy crawl each_article

    ```
