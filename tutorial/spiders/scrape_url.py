import scrapy


class UrlSpider(scrapy.Spider):
    name = "urls_spi"

    def start_requests(self):
        urls = ['https://timesofindia.indiatimes.com/topic/farmers-protest/news'
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = response.css("li.article div.content a::attr(href)").getall()
        filename = 'urls.txt'
        with open(filename, 'w') as f:
            for item in urls:
                f.write(f'https://timesofindia.indiatimes.com{item}\n')
