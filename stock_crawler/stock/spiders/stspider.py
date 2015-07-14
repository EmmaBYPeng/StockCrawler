from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from stock.items import StockItem
from scrapy.http import Request

class MySpider(BaseSpider):
  name = "stock"

  symbolfile = open("symbol.txt")
  symbolslist = symbolfile.read().split("\n")
  start_urls = ['http://finance.yahoo.com/q?s=' + x for x in symbolslist]

  allowed_domians = ["http://finance.yahoo.com/"]
    
  def parse(self, response):
    hxs = Selector(response)
    item = StockItem()
    
    item['title'] = hxs.xpath('//div[@class="title"]/h2/text()').extract()
    item['value'] = hxs.xpath('//span[@class="time_rtq_ticker"]/span/text()').extract()
    return item
