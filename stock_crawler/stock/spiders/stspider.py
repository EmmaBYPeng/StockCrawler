from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from stock.items import StockItem
from scrapy.http import Request
import re

class MySpider(BaseSpider):
  name = "stock"

  #symbolfile = open("symbol.txt")
  #symbolslist = symbolfile.read().split("\n")
  #symbolslist = ['%5EHSI', '%5EHSCE', '%5EHSCC', '%5EDJI', '%5EIXIC', '%5EGSPC', 
  #               '000001.SS', 'CBOE', '%5EOVX'] 
  # CBOE only up to 2010, HSCC up to 2011, OVX up to 2007

  # Data from 1995 to 2015
  symbolslist = ['%5EHSI', '%5EHSCE', '%5EDJI', '%5EIXIC', '%5EGSPC', '000001.SS'] 
  start_urls = ['http://finance.yahoo.com/q/hp?s=' + x + 
                '&a=00&b=1&c=1995&d=06&e=16&f=2015&g=d' for x in symbolslist]

  allowed_domians = ["finance.yahoo.com"]
    
  def parse(self, response):
    hxs = Selector(response)
    
    next_page = map(lambda x: 'http://finance.yahoo.com' + x, hxs.xpath('//a[@rel="next"]/@href').extract())

    if not not next_page:
      yield Request(next_page[0], self.parse)

    titles = hxs.xpath('//div[@class="title"]/h2/text()').extract()
    openPrice = hxs.xpath('//tr/td[@class="yfnc_tabledata1"][position()=2]/text()').extract()
    date = hxs.xpath('//tr/td[@class="yfnc_tabledata1"][position()=1]/text()').extract()
    items = []
    for title in titles:
      item = StockItem()
      item['title'] = title
      item['openPrice'] = openPrice     
      item['date'] = date
      items.append(item)

    for item in items:
      yield item

