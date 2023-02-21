import scrapy
from ..items import AmazonscraperItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'    
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1676794739&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0'
        ]
    page_num = 2

    def parse(self, response):
        items = AmazonscraperItem()

        title = response.css('.a-size-medium::text').extract()
        author = response.css('.a-color-secondary .a-row .a-size-base:nth-child(2)').css('::text').extract()
        price = response.css('#nav-logo-sprites , .s-price-instructions-style .a-price-fraction , .s-price-instructions-style .a-price-whole').css('::text').extract()
        image = response.css('.s-image::attr(src)').extract()

        items['title'] = title
        items['author'] = author
        items['price'] = price[5:-1]
        items['image'] = image

        yield items

    
        next_page = f'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page={AmazonSpider.page_num}&qid=1676794746&rnid=1250225011&ref=sr_pg_2'
        # if AmazonSpider.page_num is not None:
        if AmazonSpider.page_num < 10:
            AmazonSpider.page_num += 1
            yield response.follow(next_page, callback=self.parse)