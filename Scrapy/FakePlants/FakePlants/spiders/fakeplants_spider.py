import scrapy
from ..items import FakeplantsItem


class FakeplantsSpider(scrapy.Spider):
    name = 'plants'    
    start_urls = [
        'https://www.fake-plants.co.uk/'
    ]

    def parse(self, response):
        links = response.css("li.product-category a::attr(href)")
        for link in links:
            yield response.follow(link.get(), callback=self.parse_categories)

    
    def parse_categories(self, response):
        items = FakeplantsItem()

        products = response.css("div.astra-shop-summary-wrap")

        for product in products:
            items['name'] = product.css("h2.woocommerce-loop-product__title::text").get()
            items['category'] = product.css("span.ast-woo-product-category::text").get().strip("\t").strip("\r\n\t\t\t\t")

            yield items
