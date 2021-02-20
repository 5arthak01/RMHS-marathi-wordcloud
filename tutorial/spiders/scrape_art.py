import scrapy
import csv


class ScrapeArticleSpider(scrapy.Spider):
    name = "each_article"

    def start_requests(self):
        urls = []
        with open('urls.txt', 'r') as f:
            urls = f.readlines()
        start_urls = [url[:-1] for url in urls]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.css("h1._23498::text").getall()
        content = response.css("div.ga-headlines::text").getall()
        counter = 0
        l = len(title)
        with open('articles.csv', 'a') as f:
            article_writer = csv.writer(
                f, delimiter='~', escapechar='|', quoting=csv.QUOTE_NONE)
            while(counter < l):
                article_writer.writerow([title[counter], content[counter]])
