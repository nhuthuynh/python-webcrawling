# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EurostoneCrawlingProductItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()
    code = scrapy.Field()
    type = scrapy.Field()
    made = scrapy.Field()
    price = scrapy.Field()


class EurostoneCrawlingCategoryItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    subCategories = scrapy.Field()
    subCategoriesLink = scrapy.Field()
