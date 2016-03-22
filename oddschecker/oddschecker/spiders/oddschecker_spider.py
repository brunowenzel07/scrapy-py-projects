from scrapy.spiders import Spider
from scrapy.selector import Selector
from oddschecker.items import OddscheckerItem

class OddscheckerSpider(Spider):
    name = "oddschecker"
    allowed_domains = ["http://www.oddschecker.com/horse-racing/"]
    start_urls = [
        "http://www.oddschecker.com/horse-racing/2016-03-23-haydock/15:30/winner",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        items = []
        length = len(response.xpath("//tr[@class='diff-row eventTableRow bc']//text()"))
        for data in range(len(response.xpath("//tr[@class='diff-row eventTableRow bc']//text()"))):
        	item = OddscheckerItem()
        	# item['number'] = str(data)
        	item['name'] = response.xpath("//tr[@class='diff-row eventTableRow bc'][{}]//text()".format(data)).extract()
        	# item['trainer'] = response.xpath("//div[@class='jockeyTrainer smalls']/p[0]/text()").extract()
        	print item
        	items.append(item)

        return items