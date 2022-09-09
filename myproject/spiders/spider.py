import datetime
import sys
from ..items import MyprojectItem
import scrapy

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['lauwpauw.com','dnnsoftware.com','iconutopia.com','inspirecleanenergy.com',
                       'careelite.de','theworldwithmnr.com','balisafarimarinepark.com','loans.com',
                       'blueandgreentomorrow.com','cartrade.com']

    start_urls = ['https://www.lauwpauw.com/7-reasons-sketching-is-more-important-then-drawing/?lang=en',
                 'https://www.dnnsoftware.com/blog/why-sketching-is-an-important-part-of-the-design-process',
                 'https://iconutopia.com/6-reasons-why-sketching-is-important/',
                 'https://www.inspirecleanenergy.com/blog/sustainable-living/ways-to-protect-the-environment',
                 'https://www.careelite.de/en/why-environmental-protection-is-so-important/',
                 'https://www.theworldwithmnr.com/post/why-it-s-important-to-protect-our-environment',
                 'https://www.balisafarimarinepark.com/reasons-to-protect-wildlife-2/',
                 'https://www.loans.com.au/car-loans/green-car-loans/5-environmental-benefits-of-green-cars',
                 'https://blueandgreentomorrow.com/spend/5-important-reasons-to-buy-eco-friendly-car/',
                 'https://www.cartrade.com/blog/2014/greens/benefits-of-eco-friendly-cars-964.html']

    def start_requests(self):
        for url in self.start_urls:
            index = self.start_urls.index(url) + 1
            parse_name = 'parse_' + str(index)
            yield scrapy.Request(url,callback=self.parse,method='GET',dont_filter=True)

    def parse(self, response):
        if 'lauwpauw' in response.url:
            item = MyprojectItem()
            item['url'] = response.url
            item['title'] = response.xpath(r'//*[@id="post-2558"]/header/h2/text()').extract()[0]
            item['introduction'] = response.xpath(r'//*[@id="post-2558"]/div[2]/p[2]/text()').extract()[0]
            yield item
        elif 'dnnsoftware' in response.url:
            item = MyprojectItem()
            item['url'] = response.url
            item['title'] = response.xpath(r'//*[@id="dnn_ctr1568_Dispatch_DetailView_ScopeWrapper"]/div[1]/div[1]/div[1]/h3/text()').extract()[0]
            item['introduction'] = '-'
            yield item

        elif 'iconutopia' in response.url:
            item = MyprojectItem()
            item['url'] = response.url
            item['title'] = response.xpath(r'//*[@id="post-642"]/h1/text()').extract()[0]
            item['introduction'] = response.xpath(r'//*[@id="post-642"]/div/p[1]/text()').extract()[0]
            yield item

        elif 'inspirecleanenergy' in response.url:
            item = MyprojectItem()
            item['url'] = response.url
            item['title'] = response.xpath(r'//*[@id="__next"]/div/div[1]/main/div/main/section[1]/div/h1/text()').extract()[0]
            item['introduction'] = response.xpath(r'//*[@id="__next"]/div/div[1]/main/div/main/section[2]/div/div[2]/div[1]/h2/text()').extract()[0]
            yield item

        elif 'careelite' in response.url:
            item = MyprojectItem()
            item['url'] = response.url
            item['title'] = response.xpath(r'//*[@id="post-27237"]/div[2]/div/h1/text()').extract()[0]
            item['introduction'] = response.xpath(r'//*[@id="text-6"]/div/p[2]/text()').extract()[0]
            yield item

        elif 'theworldwithmnr' in response.url:
            item = MyprojectItem()
            item['url'] = response.url
            item['title'] = response.xpath(r'//*[@id="content-wrapper"]/div[2]/div/div[2]/div/div[1]/div[1]/article/div/div[1]/div[2]/h1/span/span/text()').extract()[0]
            item['introduction'] = response.xpath(r'//*[@id="viewer-crja5"]/span/text()').extract()[0]
            yield item

        elif 'balisafarimarinepark' in response.url:
            item = MyprojectItem()
            item['url'] = response.url
            item['title'] = response.xpath(r'//*[@id="page"]/div[2]/div/div/h1/text()').extract()[0]
            item['introduction'] = response.xpath(r'//*[@id="breadcrumbs"]/span/span/span/strong/text()').extract()[0]
            yield item

        elif 'loans' in response.url:
            item = MyprojectItem()
            item['url'] = response.url
            item['title'] = response.xpath(r'/html/body/div[2]/div/div[1]/div/h1/text()').extract()[0]
            item['introduction'] = '-'
            yield item

        elif 'blueandgreentomorrow' in response.url:
            item = MyprojectItem()
            item['url'] = response.url
            item['title'] = response.xpath(r'//*[@id="mvp-post-feat-text-wrap"]/div/div/h1/text()').extract()[0]
            item['introduction'] = '-'
            yield item

        else:
            item = MyprojectItem()
            item['url'] = response.url
            item['title'] = response.xpath(r'//h1[@class = "article-title"]/text()').extract()[0]
            item['introduction'] = '-'
            yield item