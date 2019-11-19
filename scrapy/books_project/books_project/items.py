# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    avaiable = scrapy.Field()
    qtd = scrapy.Field()
    stars = scrapy.Field()
    category = scrapy.Field()
    upc = scrapy.Field()
