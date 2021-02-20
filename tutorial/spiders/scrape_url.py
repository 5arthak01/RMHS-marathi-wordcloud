import scrapy


class UrlSpider(scrapy.Spider):
    name = "urls_spi"

    def start_requests(self):
        urls = [
            f"https://www.loksatta.com/page/{x}/?s=farmers+protest" for x in range(1, 3)
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = response.css("div.newslistbx h2 a::attr(href)").getall()
        filename = "urls.txt"
        with open(filename, "a") as f:
            for item in urls:
                f.write(f"{item}\n")
