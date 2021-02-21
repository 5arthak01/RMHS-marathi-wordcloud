# RMHS Assignment 2 submission

**Note**: This is a markdown file, and for better understanding nust be opened with an appropriate viewer. One way to do so is [here](https://stackedit.io/), but if you are on linux, [VS Code preview](https://code.visualstudio.com/docs/languages/markdown) or [grip](https://github.com/joeyespo/grip) is recommended.

Sarthak Agrawal - Marathi media,
Pranoy J - Malayalam media

# Marathi media

## Tools

Technology used is [Scrapy](https://scrapy.org/), primarily because it is extremely fast, and allows both precision and accuracy since we can use CSS selectors to target DOM elements, which was especially helpful in the case of Maharastra times, since their articles had multiple sub-elements, such as `<strong>` for bold. Using python allows for very easy data parsing, cleaning and storing - I could store each article in the csv file as soon as it was scraped. The articles in Maharastra times have other links to other articles embedded as well, cleaning this would be a hassle otherwise (such as in `wget`), but python makes it a breeze.

There are alternatives such as wget (which doesn't allow the same flexibility in handling the scraped data, cleaning and storing can be a pain) or BeautifulSoup or Spyder in python, but these are not as fast as Scrapy. Scrapy also has great documentation and a quick, easy setup.

## Archive

- **Loksatta**

  The file [all_loksatta_articles.csv](./loksatta/all_loksatta_articles.csv) has columns `URL, title, description, date, content` (in this order) and has these headers as the first line. It has `|` as the delimiter. It has 195 articles.

- **Maharashtra times**

  The file [all_mt_times_articles.csv](./mt_times/all_mt_times_articles.csv) has the columns `URL, title, author, date, highlights, content` (in this order) and has has these headers as the first line. It has `|` as the delimiter. It has 242 articles.

## Analysis

### Topic Modelling

Attempted Contextualized Topic Modelling, but did not have much success. [Zero-shot modelling](https://arxiv.org/pdf/2004.07737v2.pdf) gave all-english garbage, unrelated output for data. CombinedTM gave relevant output, but all english again, which is stored in [CTMtopics.txt](./mt_times/CTMtopics.txt). Both were employed only on 20 articles, as a test first, and were discontinued due to such unsatisfactory results.

### Wordcloud

The Wordcloud library doesn't work for non-English content by default, so there were some challenges here. The two main issues are rendering the font, and stopwords (else the wordcloud will be filled with articles, pronouns, verbs, etc). The issuse of tokenising the words could not be solved.

- Font was initially downloaded from [here](https://www.freefontspro.com/otf/13585/marathi-saras.font), but it it did not render. After some searching, [lipikaar](http://www.lipikaar.com/support/download-unicode-fonts-for-hindi-marathi-sanskrit-nepali) was found to be working. However, there were still complications - Marathi, like Hindi, has `मात्रा(matraa)`, essential to the word, but were not being rendered initially.

- Stopwords were obtained from

  - [This repo](https://github.com/stopwords-iso/stopwords-mr)
  - [Kaggle](https://www.kaggle.com/rtatman/stopword-lists-for-19-languages?select=marathiST.txt)
  - [CLTK](https://github.com/cltk/cltk/blob/master/cltk/stop/marathi/stops.py)
  - Was excited on seeing [LTRC](https://ltrc.iiit.ac.in/showfile.php?filename=ltrc/internal/nlp/corpus/index.html) but the file contains only garbage :(

Some sources needed minor editing. However, these were not sufficient either, and some words were added to the list manually.

#### Results

The wordclouds are stored in [loksatta_wordcloud.png](./loksatta/loksatta_wordcloud.png) and [mt_wordcloud.png](./mt_times/mt_wordcloud.png). As expected, both have the words "farmer" and "protest" as main discourses. However there are many difference between the two paper otherwise. Loksatta has more emphasis on "modi", "rahul gandhi" and "tweet" (they often had tweets embedded in their articles as well). Maharashtra times, on the other hand, has focus on "farm laws", "delhi", "police" and "rakesh taikit". It also has far more emphasis on "farmers" and "discussion".
