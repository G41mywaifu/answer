# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class productItem(scrapy.Item):



    name = scrapy.Field()
    id= scrapy.Field()
    brandId = scrapy.Field()
    img_urls= scrapy.Field()
    detail = scrapy.Field()
  

    pass
