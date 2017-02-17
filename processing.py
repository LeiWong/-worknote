# -*- coding:utf-8 -*-

import urllib2
import urllib
from lxml import etree
from multiprocessing import Process,Queue
import os
import random
import re

def spider():
	re = urllib2.Request("http://www.snh48.com/member_list.php")
	html = urllib2.urlopen(re).read()
	#print html
	selector = etree.HTML(html)
	image = selector.xpath("//img/@src")

	q= Queue()
	for item in image:
		print item

		item = "http://www.snh48.com/" + item
		q.put(item)
	return q
def get_image(q):
	if  not os.path.exists("./snh48"):
		os.mkdir("./snh48")
	url = q.get()
	x= random.randint(0,1000)
	name = "x" + str(x)
	if os.path.exists("./snh48/%s.jpg"%name):
		name = "x"+str(x+0.1)
	urllib.urlretrieve(url,"./snh48/%s.jpg"%name)
		
	
def main():
	result = spider()

	if result:
		p1 = Process(target=get_image,args=(result,))
		p2 = Process(target=get_image,args=(result,))
		p1.start()
		p2.start()
		p1.join()
		p2.join()
		
if __name__ == "__main__":
	main()



