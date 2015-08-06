#coding=utf-8


from scrapy.item import Item, Field

class LagouItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position = Field()
    positionUrl = Field()
    department = Field()
    salaryMin = Field()
    salaryMax = Field()
    city = Field()
    workYearMin = Field()
    workYearMax = Field()
    education = Field()
    fulltime = Field()
    advantage = Field()
    postTime = Field()
    description = Field()
    company = Field()
    companyImgUrl = Field()
    companyPage = Field()
    companyField = Field()
    companyUrl = Field()
    companyPopulationMin = Field()
    companyPopulationMax = Field()
    companyStatus = Field()
    address = Field()

