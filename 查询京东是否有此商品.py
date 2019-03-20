from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import sys
def get_brand_searchurl(i):##品牌名转换为京东搜索结果页
    try:
        temp1 = str(i.encode("utf-8"))
        temp2 = "https://search.jd.com/Search?keyword="+(temp1.replace("b'\\x","%").replace("\\x","%").replace("b'",""))[:-1]+"&enc=utf-8"
        return(temp2)
    except:
        print("获取品牌错误")
temp = input("本程序将查询京东搜索结果中是否有此商品\n请在同一目录创建“京东待查询关键词.csv”\n按回车键继续")
file = open("京东待查询关键词.csv")
for each in file.readlines():
    try:
        each = each.replace("\n","")
        print(each)
        list_temp = [each]
        sop = BeautifulSoup(urlopen(get_brand_searchurl(each)).read(),"lxml")
        list1 = []
        try:
            for cherror in sop.findAll("div",{"class","check-error"}):
                cherror = cherror.get_text()
                list1.append(cherror)
                print(cherror)
            if list1 != []:
                i = (cherror.replace("\n","")).replace(" ","")
            else:
                i = "找到啦"
        except:
            i = "找到啦"            
        list_temp.append(i)
        file2 = open("京东查询结果"+time.strftime("%Y-%m-%d",time.localtime())+".xls","a")
        for i in list_temp:
            file2.write(i)
            file2.write("\t")
        file2.write("\n")
        file2.close()
    except:
        temp = 0
