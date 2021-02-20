import scrapy
import csv


class ScrapeArticleSpider(scrapy.Spider):
    name = "each_article"

    def start_requests(self):
        urls = []
        with open("filtered_urls.txt", "r") as f:
            urls = f.readlines()
        start_urls = [url[:-1] for url in urls]

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.css("h1#headline *::text").get()
        description = response.css("h2.synopsis *::text").get()
        date = response.css("div.date p span *::text").get()
        content = response.css("div.rightsec p::text").getall()

        def clean(content):
            return content.strip("\n \t")

        title = clean(title)
        description = clean(description)
        date = clean(date)
        content = " ".join([clean(x) for x in content])

        with open("all_loksatta_articles.csv", "a") as f:
            article_writer = csv.writer(f, delimiter="|")
            article_writer.writerow(
                [response.request.url, title, description, date, content]
            )
