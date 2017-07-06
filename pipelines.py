# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymysql
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

class DatailspiderPipeline(ImagesPipeline):
	def open_spider(self,spider):
		self.con=pymysql.Connect(user='root',password='zero',db='tests',charset='UTF8')
		self.cu=self.con.cursor()
    def process_item(self, item, spider):
    	title=item['title']
    	url=item['url']
    	img=item['img']
    	h1=item['h1']
    	p=item['p']
    	insert_sql="replace into datail (title,url,img,h1,p) values(%s,%s,%s,%s,%s)"
    	value=[title,url,img,h1,p]
    	self.cu.execute(insert_sql,value)
    	self.con.commit()
    	return item
    	def spider_close(self,spider):
    		self.con.close()
