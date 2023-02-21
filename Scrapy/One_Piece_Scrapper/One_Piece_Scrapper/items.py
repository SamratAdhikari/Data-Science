# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OnePieceScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    affiliations = scrapy.Field()
    occupations = scrapy.Field()
    status = scrapy.Field()
    birthday = scrapy.Field()
    origin = scrapy.Field()
    age = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    blood_type = scrapy.Field()
    devil_fruit_name = scrapy.Field()
    devil_fruit_type = scrapy.Field()
    bounty = scrapy.Field()
