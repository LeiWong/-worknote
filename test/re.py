#coding:utf-8
import re

def foo():
    data = " rthrtlo;l var v_PageCount = 6; var pg = new showPages('pg','page'); pg.pageCount =v_PageCount;  // 定义总页数(必要) pg.printHtml_nonstandard(2); "

    result = re.search(r'v_PageCount = (\d);',data)
    print result.group(1)

foo()