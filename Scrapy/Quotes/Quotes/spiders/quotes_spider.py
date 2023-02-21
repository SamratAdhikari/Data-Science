import scrapy
from ..items import QuotesItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class QuoteSpider(scrapy.Spider):
    name = 'Quotes'
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):

        token = response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'test',
            'password': 'test'
        }, callback=self.start_scraping)


    def start_scraping(self, response):
        open_in_browser(response)
        items = QuotesItem()
        div_quotes = response.css("div.quote")

        print('\n\n\n')
        for quotes in div_quotes:
            quote = [string.lstrip('“').rstrip('”').replace(',', '') for string in quotes.css("span.text::text").extract()]
            author = quotes.css("small.author::text").extract()
            tags = quotes.css(".tag::text").extract()
        
            items['quote'] = quote
            items['author'] = author
            items['tags'] = tags

            yield items