# Para executar:     scrapy runspider spiders/quotes_toscrape_com.py
# Salvar em arquivo: scrapy runspider spiders/quotes_toscrape_com.py -o quotes.csv
# Salvar em arquivo: scrapy runspider spiders/quotes_toscrape_com.py -o quotes.json
import scrapy

from quotes_project.items import QuotesItem

class QuotesToscrapeComSpider(scrapy.Spider):
  name = 'quotes.toscrape.com'
  allowed_domains = ['quotes.toscrape.com']
  start_urls = ['http://quotes.toscrape.com/']

  def parse(self, response):
    for quote in response.css('.quote'):
      text = quote.css('span.text::text').get()
      autor = quote.css('.author::text').get()
      yield QuotesItem (
        text=text,
        author=autor,
        url=response.url,
        rank=1
      )
        
    # Paginação
    url = response.css('.pager .next a::attr(href)').get()
    if url is not None:
      yield response.follow(url)
