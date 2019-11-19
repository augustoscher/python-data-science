# -*- coding: utf-8 -*-
import scrapy

from books_project.items import BooksItem

class BooksToscrapeComSpider(scrapy.Spider):
    name = 'books.toscrape.com'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def get_name(self, name):
      res = name[70:-18]
      res = res.replace('lt=', '').replace('"', '').strip()
      return res

    def get_stars_count(self, param):
      idx = param.find('star-rating') + 12
      res = param[idx:idx + 5]
      res = res.replace('"', '').replace('>', '').strip().lower()
      choices = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
      return choices.get(res)

    def parse(self, response):
      for book in response.css('.col-xs-6'):
        name = book.css('.thumbnail').get()
        price_str = book.css('.price_color::text').get()[1:]
        stars_str = book.css('p.star-rating').get()

        yield BooksItem (
          name= self.get_name(name),
          price = float(price_str),
          avaiable = True,
          qtd = 'qtd',
          stars = self.get_stars_count(stars_str),
          category = 'Category',
          upc = 'Upc',
        )
      
      url = response.css('.pager .next a::attr(href)').get()
      if url is not None:
        yield response.follow(url)

