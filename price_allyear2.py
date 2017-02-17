# -*- coding:utf-8 -*-


import os
import re
import random
import time
import json
import time
import requests
from lxml import etree


def spider_url(id,start,end):
	"""spider  url and parse string content"""
	page = 0
	info = []
	while True:
		USER_AGENTS = [
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
			"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
			"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
			"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
			"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
			"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
			"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
			"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
			"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
			"Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
			"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
			"Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
		]
		n = random.randrange(0, len(USER_AGENTS))

		headers = {
			"User-Agent":USER_AGENTS[n]}
		proxies = {
			"https": "https://58.67.159.50:80",
			"https": "https://113.108.253.195:9797",
			"https": "https://101.231.46.34:8000",
			"https": "https://211.103.250.145:80",
			"https": "https://202.111.175.97:8080",
			"https": "https://58.59.68.91:9797",
			"https": "https://218.63.208.223:3128",
			"https": "https://58.251.132.181:8888",
			"https": "https://59.44.244.14:9797",
			"https": "https://58.214.5.229:80",
			"https": "https://219.146.2.105:23",
			"https": "https://110.208.27.75:9000"


		}
		url = "http://nc.mofcom.gov.cn/channel/gxdj/jghq/jg_list.shtml?par_craft_index=13075&craft_index=%s&startTime=%s&endTime=%s&par_p_index=&p_index=&keyword=&page="%(id,start,end)
		url = url + str(page)
		print url
		#get html page
		time.sleep(5)
		re = requests.get(url,headers=headers,proxies=proxies)
		html = re.text
		#print html
		selector = etree.HTML(html)
		item = selector.xpath("//div[@class='pmCon']//table/tbody/tr")
		if item:
			#print item
			info = []
			product = item[0].xpath("//td[1]/text()")[0].encode("utf-8").strip()
			j = 0
			for each in item:
				data = {}
				data["name"] = each.xpath("//td[1]/text()")[j].encode("utf-8").strip()
				data["price"] = each.xpath("//td[2]/text()")[j].encode("utf-8").strip()
				data["market"] = each.xpath("//td[3]/a/text()")[j].encode("utf-8").strip()
				data["date"] = each.xpath("//td[4]/text()")[j].encode("utf-8").strip()
				date = each.xpath("//td[4]/text()")[j].encode("utf-8").strip()
				#data = "%s\t%s\t%s\t%s\n"%(name.strip(),price.strip(),market.strip(),date.strip())
				info.append(data)
				#print data

				if j < len(item):
					j += 1
			s = start.split('-')
			e = end.split('-')
			s = reduce(lambda x,y:x+y,s)
			e = reduce(lambda x,y:x+y,e)
			path = "%s%s"%(id,product)
			if page == 0:
				if  not os.path.exists(path):
					os.mkdir("./" + path)
				os.chdir("./" + path)
			with open("./%s%s-%s.json" % (product,s,e),	"a+") as f:
				#info = "%s" % info
				info = json.dumps(info,ensure_ascii=False)
				f.write(info)
			print date
			if date.strip() == start or date.strip() == "2014-01-02" :
				break
			else:
				page += 1


def get_page(id,start,end):
	"""get the total page number"""
	headers = {
			"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
	proxies = {}
	url = "http://nc.mofcom.gov.cn/channel/gxdj/jghq/jg_list.shtml?par_craft_index=13075&craft_index=%s&startTime=%s&endTime=%s&par_p_index=&p_index=&keyword=&page=0"%(id,start,end)
	print url
	r = requests.get(url,headers=headers)
	html = r.text
	#print html
	page = re.search(r'[\w|\s]*<script>[\w|\s]*v_PageCount[\w|\s]+;$',html)
	print page
	#selector = etree.HTML(html)
	#item2 = selector.xpath("//div[@class='new_page2']/a")
	#print item2
	#for i in item2:
	#	print i 
	

		
		
		
def run():
	"""run the spider
	"""

	
	id=raw_input("please enter product id:")
	#start=raw_input("please enter starttime[eg:2017-01-01]:")
	#end=raw_input("please enter endtime[eg:2017-01-01]:")
	#year = raw_input("please enter year :")
	for year in [2014,2015,2016]:
		year = str(year)
		for i in range(1,5):
			if i == 1:
				start = year + "-01-01"
				end = year + "-03-31"
				spider_url(id,start,end)
				os.chdir("../")
			elif i == 2:
				start = year + "-03-31"
				end = year + "-06-30"
				spider_url(id,start,end)
				os.chdir("../")
			elif i == 3:
				start = year + "-06-30"
				end = year + "-09-30"
				spider_url(id,start,end)
				os.chdir("../")
			elif i == 4:
				start = year + "-09-30"
				end = year + "-12-31"
				spider_url(id,start,end)
				os.chdir("../")
	#get_page(id,start,end)
if __name__ == "__main__":
	s = time.time()
	if not os.path.exists("./vegetable"):
		os.mkdir("./vegetable")
	os.chdir("./vegetable")
	run()
	os.chdir("../")
	time = s-time.time()
	print("spend %s min"%(int(time)/60)) 

