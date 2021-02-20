import scrapy
import csv


class ScrapeArticleSpider(scrapy.Spider):
    name = "each_article"

    def start_requests(self):
        urls = []
        with open("filtered_urls.txt", "r") as f:
            urls = f.readlines()
        start_urls = [url[:-1] for url in urls]

        # start_urls = [
        #     "https://maharashtratimes.com/india-news/the-way-farmers-are-being-treated-is-shameful-says-harsimrat-kaur-badal/articleshow/80665137.cms"
        # ]

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.css("div.news_card h1::text").get()
        author = response.css(
            "div.news_card_source div.source span[itemprop='author']::text"
        ).get()
        date = response.css(
            "div.news_card_source div.source span.time *::text"
        ).getall()
        highlights = response.css(
            "div.undefined.top-article.tophighlight *::text"
        ).getall()
        content = response.css("article.story-content *::text").getall()
        junk_articles = response.css(".embedarticle *::text").getall()

        for junk in junk_articles + highlights:
            content.remove(junk)

        def clean(content):
            return content.strip("\n \t")

        title = clean(title)
        author = clean(author)
        date = " ".join([clean(x) for x in date])
        highlights = " ".join([clean(x) for x in highlights])
        content = " ".join([clean(x) for x in content])

        with open("maharashtra_times_articles.csv", "a") as f:
            article_writer = csv.writer(f, delimiter="|")
            article_writer.writerow([title, author, date, highlights, content])
