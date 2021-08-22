# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class TcaeQuestion(Item):
    title = Field(type=str)
    answer_1 = Field(type=str)
    answer_2 = Field(type=str)
    answer_3 = Field(type=str)
    correct_answer = Field(type=int)
