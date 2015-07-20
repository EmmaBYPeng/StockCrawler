# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

def serialize_value(value):
  return "%s\n" % str(value) 

class StockItem(scrapy.Item):
  # define the fields for your item here like:
  title = scrapy.Field(serializer=serialize_value)
  openPrice = scrapy.Field(serializer=serialize_value)
  date = scrapy.Field(serializer=serialize_value)
