#coding:utf-8
page=1
def foo():
	global page
	page= page + 1
	print page
	print str(page)

#foo()
#print page

def foo2():
	data = []

	for i in range(1,10):
		content = {
		i:i+1
			}
		data.append(content)
	with open('./hello.json','w+') as f:
		data = "%s"%data
		f.writelines(data)
	return data

import os
def foo3():
	path = os.mkdir("./hello")
	print path

if __name__ == "__main__":
	#result = foo2()
	#print result
	foo3()
