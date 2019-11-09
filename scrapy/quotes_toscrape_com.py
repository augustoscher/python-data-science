# Para executar:     scrapy runspider quotes_toscrape_com.py
# Salvar em arquivo: scrapy runspider quotes_toscrape_com.py -o quotes.csv
# Salvar em arquivo: scrapy runspider quotes_toscrape_com.py -o quotes.json
import scrapy


class QuotesToscrapeComSpider(scrapy.Spider):
  name = 'quotes.toscrape.com'
  allowed_domains = ['quotes.toscrape.com']
  start_urls = ['http://quotes.toscrape.com/']

  def parse(self, response):
    for quote in response.css('.quote'):
      text = quote.css('span.text::text').get()
      autor = quote.css('.author::text').get()
      yield {
        'text': text,
        'author': autor
      }
    
    url = response.css('.pager .next a::attr(href)').get()
    yield response.follow(url)
