import scrapy
from bs4 import BeautifulSoup
from itcast.items import ItcastItem
class ItcastteacherSpider(scrapy.Spider):
    name = 'itcastteacher'
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#ajavaee"]
    custom_settings = {
        'ITEM_PIPELINES': {
            'itcast.pipelines.ItcastPipeline': 300,
        }
    }
    def parse(self, response):
        try:
            #item = ItcastItem()
            #divlist = response.xpath('//div[@class="li_txt"]')
            #print(divlist)
            '''for div in divlist:
                item.name = div.xpath('/h3/text()').extract()
                item.position = div.xpath('/h4/text()').extract()
                item.info = div.xpath('/p/text()').extract()
                print(item)
                yield item'''
            soup = BeautifulSoup(response.text,'html.parser')
            divs = soup.find_all(attrs={"class": "li_txt"})
            for div in divs:
                #print(div)
                item = ItcastItem()
                for tag in div.children:
                    if tag.name == 'h3':
                        item['nam'] = tag.string
                        print(tag.string)
                    elif tag.name == 'h4':
                        item['position'] = tag.string
                        print(tag.string)
                    elif tag.name == 'p':
                        item['info'] = tag.string
                        print(tag.string)
                    else:
                        continue
                yield item
        except:
            pass