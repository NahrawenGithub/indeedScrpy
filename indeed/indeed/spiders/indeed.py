import os

import scrapy
import sys


# from indeed.indeed.items  import IndeedItem
import self as self


class indeedSpider(scrapy.Spider) :
    name = 'indeed'
    Q = None
    print("\ntest1\n")
    def start_requests(self):
        urls = ["https://fr.indeed.com/emplois?as_and=Software+Developper&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=0&l=%C3%8Ele-de-France&fromage=any&limit=20&sort=&psf=advsrch&from=advancedsearch" ,
                "https://www.indeed.com/jobs?as_and=&as_phr=Sales+Representative&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=0&l=United+States&fromage=any&limit=30&sort=date&psf=advsrch&from=advancedsearch",
                "https://br.indeed.com/empregos?as_and=Financial+Analyst&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=0&l=S%C3%A3o+Paulo&fromage=any&limit=10&sort=&psf=advsrch&from=advancedsearch"
                ]
        print("\ntest1\n")
        for url in urls :
            yield scrapy.Request(url , self.parse)


    def parse(self , response ):
        print("\nopen1\n")

        cards = response.xpath('//div[@class="jobsearch-SerpJobCard unifiedRow row result "]')
        print("\nopen2\n")

        for clickCard in cards :
            items = IndeedItem()
        # jobTitle
            items['jobTitle'] = clickCard.xpath('.h2//a/@title').extract()[0]
            self.Q.put('title parsed......')
            print("\nopen\n")

            # companyName
            if clickCard.xpath('.//div/span[@class="company"]/text()').extract()[0].strip() == '':
                items['companyName'] = clickCard.xpath(
                    './/div/span[@class="company"]/a/text()').extract()[0].strip()
            else:
                items['companyName'] = clickCard.xpath(
                    './/div/span[@class="company"]/text()'
                ).extract()[0].strip()
            self.Q.put('companyName parsed......')

            # url
            items['url'] = clickCard.xpath(
                './/h2/a/@href').extract()[0]
            self.Q.put('url parsed......')

            #
            # items['Summary'] = clickCard.xpath(
            #     '//*[@id="p_e2b9b47c4fa9aaa8"] > div ').extract()[0].strip()
            # self.Q.put('Summary parsed......')
            #

        self.Q.put(f"\n{items['jobTitle']}\n{items['companyName']}\n{items['url']}\n")
        yield items



class IndeedItem(scrapy.Item):
                # define the fields for your item here like:
                jobTitle = scrapy.Field()
                companyName = scrapy.Field()
                Summary = scrapy.Field()
                Location = scrapy.Field()
                DatePosted = scrapy.Field()
                url = scrapy.Field()