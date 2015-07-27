#coding: utf-8

from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from lagou.items import LagouItem

class LagouSpider(CrawlSpider):
    name = "lagou"
    allowed_domains = ["www.lagou.com"]
    download_dalay = 2
    start_urls = [
        "http://www.lagou.com"
    ]
    rules = (
        
        Rule(LinkExtractor(allow=(r'http://www.lagou.com/jobs/\d+\.html', )), callback='parse_item'),
    )

    def parse_item(self, response):
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

        lagou['advantage'] = sel.xpath('//dd[@class="job_request"]/text()').extract()[5].rstrip().lstrip()

        lagou['postTime'] = sel.xpath('//dd[@class="job_request"]/div/text()').extract()[0]

        descriptionRaw = sel.xpath('//dd[@class="job_bt"]//p').extract()
        description = ''
        for p in descriptionRaw :
            description += p
        lagou['description'] = description

        lagou['company'] = sel.xpath('//dl[@class="job_company"]/dt//h2/text()').extract()[0].lstrip().rstrip()

        lagou['companyImgUrl'] = sel.xpath('//dl[@class="job_company"]/dt/a/img/@src').extract()[0]

        lagou['companyPage'] = sel.xpath('//dl[@class="job_company"]/dt/a/@href').extract()[0]

        lagou['companyField'] = sel.xpath('//dl[@class="job_company"]/dd/ul[1]/li[1]/text()').extract()[0]

        lagou['companyPopulation'] = sel.xpath('//dl[@class="job_company"]/dd/ul[1]/li[2]/text()').extract()[0]

        lagou['companyUrl'] = sel.xpath('//dl[@class="job_company"]/dd/ul[1]/li[3]/a/@href').extract()[0]

        lagou['companyStatus'] = sel.xpath('//dl[@class="job_company"]/dd/ul[2]/li/text()').extract()[0]

        lagou['address'] = sel.xpath('//dl[@class="job_company"]/dd/div[1]/text()').extract()[0]

        return lagou
