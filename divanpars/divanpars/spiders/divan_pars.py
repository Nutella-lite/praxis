import scrapy

class DivanParsSpider(scrapy.Spider):
    name = "divan_pars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        divans = response.css('div._Ud0k')
        for divan in divans:
            yield {
                'name' : divan.css('div.wYUX2 span::text').get(),
                'price' : divan.css('div.q5Uds span::text').get(),
                'link' : divan.css('a').attrib['href']
            }
# scrapy crawl divan_pars