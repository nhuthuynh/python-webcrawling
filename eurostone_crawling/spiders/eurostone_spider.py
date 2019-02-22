# -*- coding: utf-8 -*-
import scrapy
from eurostone_crawling.items import EurostoneCrawlingProductItem


class EurostoneSpiderSpider(scrapy.Spider):
    name = 'eurostone_spider'
    allowed_domains = ['eurostone.vn']
    start_urls = ['http://eurostone.vn/da-marble-cam-thach/']

    def get_products(self, product_selector, response):
        productItem = EurostoneCrawlingProductItem()
        productItem["name"] = product_selector.xpath('./div[@class="item_img"]/a/@title').extract_first()
        productItem["url"] = response.urljoin(product_selector.xpath('./div[@class="item_img"]/a/@href').extract_first())
        productItem["image_urls"] = [response.urljoin(product_selector.xpath('./div[@class="item_img"]//img/@src').extract_first())]
        productItem["code"] = product_selector.xpath('normalize-space(./div[@class="item_content"]//p[contains(@class, "label")]/text())').extract_first()
        productItem["price"] = product_selector.xpath('normalize-space(./div[@class="item_content"]//p[@class="price"])').extract_first()
        productItem["type"] = product_selector.xpath('./div[@class="item_content"]//div[2]/text()').extract_first()
        productItem["made"] = product_selector.xpath('./div[@class="item_content"]//div[1]/text()').extract_first()
        return productItem

    def parse(self, response):

        # crawl product
        products = response.xpath('.//div[@id="category"]/div[@class="s_list"]//div[@class="item"]')
        for product in products:
            yield self.get_products(product, response)

        # crawl next page of product list
        next_pagination_url = response.xpath('//div[@id="category"]//ul[@class="pagination"]//li[last()]//a[contains(@rel, "next")]/@href').get()
        next_category_url = response.xpath('//ul[@id="menu_17"]//li[@class="active"]/following-sibling::li[1]/a/@href').get()
        next_url = ''

        if next_pagination_url is not None:
            next_url = response.urljoin(next_pagination_url)
        elif next_category_url is not None:
            next_url = response.urljoin(next_category_url)
        print('next page', next_pagination_url, next_category_url, next_pagination_url)
        if next_url is not None:
            yield scrapy.Request(url=next_url, callback=self.parse)
