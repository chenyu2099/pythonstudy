#from calculator import Count
# class TestCount:
#      def test_add(self):
#          try:
#              j = Count(2, 3)
#              add = j.add()
#              assert(add == 5),'Ineger addition tesult error!'
#          except AssertionError as msg:
#              print(msg)
#          else:
#              print('Test pass!')
#
#
# mytest = TestCount()
# mytest.test_add()
# import unittest
#
# class TestCount(unittest.TestCase):#单元测试
#
#    def setUp(self):
#       print("test start")
#
#    def test_add(self):
#       j = Count(2,4)
#       self.assertEqual(j.add(),5)
#
#    def tearDown(self):
#       print("test end")
#
# if __name__ == "__main__" :
#    unittest.main()




#跨目录调用文件(在同一个二级目录下)
# import sys
# from os.path import dirname, abspath
#__file__获取文件所在路径
#abspath(__file__)获取绝对路径
#dirname()获取上层目录
# project_path = dirname(dirname(abspath(__file__)))
# sys.path.append(project_path+ "\\module")
#from calculatora import add
# print(add(9, 3))
# print(abspath(__file__))#文件完整路径
#
# print(dirname(abspath(__file__)))#当前文件所在目录
# print(dirname(dirname(abspath(__file__))))#第二层目录python 完整路径E:\python\module
#
# print(dirname(dirname(abspath(__file__)))+"\\module")#导入文件所在目录


"""
try:
    open("abc.txt",'r')
except FileNotFoundError:
    print("异常了")
"""
"""
try:
    print(a)
except BaseException as msg:#获取异常并打印
    print(msg)

try:
    a = "异常测试"
    print(a)
except NameError as msg: #
    print(msg)
else:
    print("没有异常时执行")

try:
    a = 1
    print(a)
except NameError as msg:# try ...except...finally finally无论是否出现异常都会执行
    print(msg)
finally:
    print("怎么都执行")

def say_hello(name=None):
    if name is None:
        raise NameError('"name" cannot be empty')#定义跑出异常的内容
    else:
        print("hello, %s" %name)

say_hello()

百度样例代码
<input id="kw" class="s_ipt" autocomplete="off" maxlength = "100" value = "" name = "wd">
<input id="su" class="bg s_btn" type="submit" value="百度一下">
<a class="mnav" name="tj_trnews" href="http://news.baidu.com">新闻</a>
<a class="mnav" name="tj_lang" href="http://news.baidu.com">很长很长的文字</a>

"""
find_element_by_id("kw")#根据ID定位
find_element_by_id("su")
find_element_by_name("wd")#根据name定位
find_element_by_class_name(s_ipt)#根据Class定位
find_element_by_tag_name("input")#根据tagname(标签名)
find_element_by_link_text("新闻")#通过标签对之间的文字信息定位
find_element_by_partial_link_text("很长的文字")#通过标签对之间的部分文字信息定位
#xpath定位

driver.find_element_by_xpath("//input[@id='kw']")#标签名
driver.find_element_by_xpath("//*[@name='wd']")#可以不指定标签名
"""<form id="form" class="fm" action="/s" name="f">
<span class="s_ipt_wr">
 <input id="kw" .....>
</span>
<span class="s_btn_wr">
<input id="su".....>
</span>
"""
find_element_by_xpath("//span[@Class='S_ipt_wr']/input")
driver.find_element_by_xpath('//img[@alt="div1-img1"]')