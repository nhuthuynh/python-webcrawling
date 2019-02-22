import scrapy

class Category(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    subCategories = scrapy.Field()
    subCategoriesLink = scrapy.Field()