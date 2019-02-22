import scrapy

class Product(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()
    code = scrapy.Field()
    type = scrapy.Field()
    made = scrapy.Field()