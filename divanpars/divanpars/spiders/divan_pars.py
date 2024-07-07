# Написать spider для нахождения всех источников освещения с сайта divan.ru
# Нужно взять название источника освещения, цену и ссылку
import scrapy

class DivanParsSpider(scrapy.Spider):
    name = "divan_pars"
    allowed_domains = ["https://www.divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        # Парсинг данных о светильниках
        items = response.css('div._Ud0k')
        for item in items:
            yield {
                'name': item.css('div.wYUX2 span::text').get(),
                'price': item.css('div.q5Uds span::text').get(),
                'link': response.urljoin(item.css('a').attrib['href'])
            }

        # Обработка пагинации
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# scrapy crawl divan_pars