# -*- coding: utf-8 -*-
from datetime import datetime

import scrapy

from books_project.items import BooksItem

class BooksToscrapeComSpider(scrapy.Spider):
    name = 'books.toscrape.com'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
      for book in response.css('.col-xs-6'):
        name = book.css('.thumbnail').get()
        yield BooksItem (
          name=name[70:-18],
          price = '',
          avaiable = '',
          qtd = '',
          stars = '',
          category = '',
          upc = '',
          scrape_date=datetime.now().isoformat(),
        )
      

