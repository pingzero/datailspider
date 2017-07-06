import scrapy
from ..items import DatailspiderItem

class datailspider(scrapy.Spider):
	name='datailspider'
	start_urls=['http://news.dmzj.com/']
	def parse(self,response):
		item=DatailspiderItem()
		item['title']=response.xpath(".//div[@class='briefnews_con_li']/div[2]/h3/a/").extract()
		item['url']=response(".//div[@class='briefnews_con_li']/div[2]/h3/a/@href").extract()
		for link in item['url']:
			yield scrapy.Request(link,self.parse_item)
		item['img']=response.xpath(".//div[@class='briefnews_con_li']/div[1]/a/img/@src").extract()
		yield item
		new_url=response.xpath(".//*[@id='page']/a[last()-1]").extract()[0]
		if new_url:
			yield scrapy.Request(new_url,self.parse)
	def parse_item(self,response):
		item['h1']=response.xpath(".//h1/text()").extract()[0]
		item['p']=response.xpath(".//div[@class='news_content_con']").extract()
		print(item['h1'])


