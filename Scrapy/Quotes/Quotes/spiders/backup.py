import scrapy
from ..items import QuotesItem

class QuoteSpider(scrapy.Spider):
    name = 'Quotes'
    start_urls = ['http://quotes.toscrape.com/page/1/']
    page_num = 2

    def parse(self, response):
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

        

        next_page = f"http://quotes.toscrape.com/page/{QuoteSpider.page_num}/"

        if QuoteSpider.page_num < 11:
            QuoteSpider.page_num += 1
            yield response.follow(next_page, callback=self.parse)
