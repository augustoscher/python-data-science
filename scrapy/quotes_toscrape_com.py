# Para executar: scrapy runspider quotes_toscrape_com.py
import scrapy


class QuotesToscrapeComSpider(scrapy.Spider):
    name = 'quotes.toscrape.com'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('.quote'):
            text = quote.css('span.text::text').get()
            yield {'text': text}
