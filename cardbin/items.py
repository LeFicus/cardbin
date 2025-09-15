# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CardbinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    bin_iin = scrapy.Field()
    brand = scrapy.Field()
    card_type = scrapy.Field()
    category = scrapy.Field()
    bank = scrapy.Field()
    bank_url = scrapy.Field()
    country = scrapy.Field()
    country_short = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    pass
