Note: This is a markdown file, and for better understanding nust be opened with an appropriate viewer. One way to do so is [here](https://github.com/joeyespo/grip)

# RMHS Assignment 2 submission

Sarthak Agrawal - 2019115003

## Articles archive

**Methodology**

Technology used is [Scrapy](https://scrapy.org/) because it is considered extremely fast, and allows both precision and accuracy since we can use CSS selectors to target elements.

- **Loksatta**

  The `loksatta_articles.csv` file does not have a header and has `~` as delimiter. It has columns title, description, date, content (in this order). File `all_loksatta_articles.csv` has these headers as the first line and `|` as delimiter, with the addition of URLs for each article as the first column.

- **Maharashtra times**

  `maharashtra_times_articles.csv` does not have a header and has the columns title, author, date, highlights, content (in this order) and `|` as delimiter. File `all_mt_times_articles.csv` has these headers as the first line, with the addition of URLs for each article as the first column.

Instructions to run/reproduce:

- Scrapy and python are necessary
- There are two spiders, coded in the files [scrape_url](./tutorial/spiders/scrape_url.py) and [scrape_art](./tutorial/spiders/scrape_art.py). The former scrapes the URLs of the articles and stores them in a file 'urls.txt'. The second spider scrapes each article and stores in 'articles.csv'
- Run (while in current directory)

  ```
  scrapy crawl urls_spi
  python filter_urls.py
  scrapy crawl each_article
  ```

## Wordcloud

- Stopwords obtained from [Kaggle](https://www.kaggle.com/rtatman/stopword-lists-for-19-languages?select=marathiST.txt) and [CLTK](https://github.com/cltk/cltk/blob/master/cltk/stop/marathi/stops.py), the latter needed editing. Also added from [this repo](https://github.com/stopwords-iso/stopwords-mr) and manually as well. Was excited on seeing [LTRC](https://ltrc.iiit.ac.in/showfile.php?filename=ltrc/internal/nlp/corpus/index.html) recommended on first page result, but the file contains only garbage :(
- Font obtained from [lipikaar](http://www.lipikaar.com/support/download-unicode-fonts-for-hindi-marathi-sanskrit-nepali), [another](https://www.freefontspro.com/otf/13585/marathi-saras.font) didn't work.
- Issues referred:
  - https://github.com/amueller/word_cloud/issues/70
  - https://github.com/amueller/word_cloud/issues/367
  - https://github.com/amueller/word_cloud/issues/272
  - https://github.com/amueller/word_cloud/issues/562 (finally solved here!)

## Topic Modelling

Tried (Contextualized Topic Modelling)[https://github.com/MilaNLProc/contextualized-topic-models]. Zero-shot modelling gave garbage (that too all english) output for data, and CombinedTM gave relevant output, but all english again, which is stored in [CTMtopics.txt](./CTMtopics.txt). Both were employed only on 20 articles, which are stored in `temp_files` directory.
