import scrapy


class TcaeSpider(scrapy.Spider):
    name = "tcae"

    def start_requests(self):
        urls = [
            'http://google.es',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass