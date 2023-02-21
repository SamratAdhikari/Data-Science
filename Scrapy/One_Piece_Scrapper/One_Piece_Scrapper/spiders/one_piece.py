import scrapy
from ..items import OnePieceScrapperItem


class OnePieceSpider(scrapy.Spider):
    name = 'one_piece'
    start_urls = ['https://onepiece.fandom.com/wiki/List_of_Canon_Characters']

    def parse(self, response):
        links = response.css("td:nth-child(2) a::attr(href)")
        for link in links:
            yield response.follow(link.get(), callback=self.parse_characters)

    
    def parse_characters(self, response):
        items = OnePieceScrapperItem()

        info = response.css(".pi-layout-default")

        for data in info:
            box = data.css(".pi-item-spacing.pi-border-color")

            for title in box:
                if title.css(".pi-data-label::text").get() == 'Official English Name:':
                    items['name'] = title.css(".pi-font").css("::text").get()
                
                elif title.css(".pi-data-label::text").get() == 'Affiliations:':
                    items['affiliations'] = title.css(".pi-font").css("::text").get()

                elif title.css(".pi-data-label::text").get() == 'Occupations:':
                    items['occupations'] = title.css(".pi-font").css("::text").get()

                elif title.css(".pi-data-label::text").get() == 'Origin:':
                    items['origin'] = title.css(".pi-font").css("::text").get()

                elif title.css(".pi-data-label::text").get() == 'Status:':
                    items['status'] = title.css(".pi-font").css("::text").get()

                elif title.css(".pi-data-label::text").get() == 'Age:':
                    items['age'] = title.css(".pi-font").css("::text").get()
                    
                elif title.css(".pi-data-label::text").get() == 'Birthday:':
                    items['birthday'] = title.css(".pi-font").css("::text").get()

                elif title.css(".pi-data-label::text").get() == 'Height:':
                    items['height'] = title.css(".pi-font").css("::text").get()

                elif title.css(".pi-data-label::text").get() == 'Weight:':
                    items['weight'] = title.css(".pi-font").css("::text").get()

                elif title.css(".pi-data-label::text").get() == 'Blood Type:':
                    items['blood_type'] = title.css(".pi-font").css("::text").get()

                elif title.css(".pi-data-label::text").get() == 'English Name:':
                    items['devil_fruit_name'] = title.css(".pi-font").css("::text").get()
                
                elif title.css(".pi-data-label::text").get() == 'Type:':
                    items['devil_fruit_type'] = title.css(".pi-font").css("::text").get()

                elif title.css(".pi-data-label::text").get() == 'Bounty:':
                    items['bounty'] = title.css(".pi-font").css("::text").get()


            

            # pass
            yield items

