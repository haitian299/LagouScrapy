#encoding: utf-8

from scrapy.spiders import Spider
from scrapy.selector import Selector

from lagou.items import LagouItem

class LagouSpider(Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    download_dalay = 2
    start_urls = [
        "http://www.lagou.com/jobs/400000.html?source=search&i=search-7"
    ]

    def parse(self, response):
        sel = Selector(response)
        lagou = LagouItem()
        lagou['position'] = sel.xpath('//dl[@class="job_detail"]/dt/h1/@title').extract()[0]
        lagou['positionUrl'] = response.url
        lagou['department'] = sel.xpath('//dl[@class="job_detail"]/dt/h1/div/text()').extract()[0]
        lagou['salary'] = sel.xpath('//dd[@class="job_request"]/span[1]/text()').extract()[0]
        lagou['city'] = sel.xpath('//dd[@class="job_request"]/span[2]/text()').extract()[0]
        lagou['workYear'] = sel.xpath('//dd[@class="job_request"]/span[3]/text()').extract()[0]
        lagou['education'] = sel.xpath('//dd[@class="job_request"]/span[4]/text()').extract()[0]
        lagou['fulltime'] = sel.xpath('//dd[@class="job_request"]/span[5]/text()').extract()[0]
        lagou['advantage'] = sel.xpath('//dd[@class="job_request"]/text()').extract()[0]
        lagou['postTime'] = sel.xpath('//dd[@class="job_request"]/div/text()').extract()[0]
        
        print lagou['department']
