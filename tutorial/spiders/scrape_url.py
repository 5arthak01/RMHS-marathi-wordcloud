import scrapy


class UrlSpider(scrapy.Spider):
    name = "urls_spi"

    def start_requests(self):
        urls = [
            f"https://maharashtratimes.com/topics/%E0%A4%B6%E0%A5%87%E0%A4%A4%E0%A4%95%E0%A4%B0%E0%A5%80-%E0%A4%86%E0%A4%82%E0%A4%A6%E0%A5%8B%E0%A4%B2%E0%A4%A8/{x}"
            for x in range(1, 3)
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = response.css("div.newslistbx h2 a::attr(href)").getall()
        filename = "urls.txt"
        with open(filename, "a") as f:
            for item in urls:
                f.write(f"{item}\n")
