import scrapy

from scrapy.selector import Selector
from tcae.items import TcaeQuestion

class TcaeSpider(scrapy.Spider):
    name = "tcae"

    custom_settings = {
        'CONCURRENT_REQUESTS': 1,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'DOWNLOAD_DELAY': 5,
        'COOKIES_ENABLED': False,
        'HTTPCACHE_ENABLED': False,
        'FEED_FORMAT': 'json',
        'TOR_PROXY_ENABLED': True
    }

    def start_requests(self):
        urls = [
            'http://www.auxiliar-enfermeria.com/test/test_4108.htm',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_test)

    def parse_test(self, response):
        questions = response.xpath("//form").getall()
        for q in questions:
            yield self.parse_question(Selector(text=q))

    def parse_question(self, selector):
        item = TcaeQuestion()
        item['title'] = self.__parse_title(selector)
        answers = self.__parse_responses(selector)
        item['answer_1'] = answers[0]
        item['answer_2'] = answers[1]
        item['answer_3'] = answers[2]
        #item[] = self.__parse_solution(selector)
        return item

    def __parse_title(self, selector):
        return selector.xpath("/html/body/form/p/font/text()").get()

    def __parse_responses(self, selector):
        answers_list = selector.xpath("/html/body/form/blockquote/p/font/text()").getall() #['27ºC', '\r\n      ', '37ºC', '\r\n      ', '47ºC', '\r\n      Resultado: ']
        
        del answers_list[1]
        del answers_list[2]
        del answers_list[3]
        return answers_list

    def __parse_solution(self, selector, anwser_list):
        pass 
    