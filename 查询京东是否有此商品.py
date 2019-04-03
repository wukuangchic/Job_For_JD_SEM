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
file = open("京东待查询关键词"+time.strftime("%Y-%m-%d",time.localtime())+".csv")
numi = 0
file2 = open("导出-"+time.strftime("%Y-%m-%d",time.localtime())+".xls","a")
for each in file.readlines():
    try:
        each = each.replace("\n","")
        print("%d-----%s"%(numi,each))
        list_temp = []
        list_temp1 = [each]
        sop = BeautifulSoup(urlopen(get_brand_searchurl(each),timeout = 30).read(),"lxml")
        list1 = []
        try:
            for cherror in sop.findAll("div",{"class","check-error"}):
                cherror = cherror.get_text()
                list1.append(cherror)
                print(cherror)
            if list1 != []:
                i = (cherror.replace("\n","")).replace(" ","")
                i = i.replace("\t","")
            else:
                i = "找到啦"
        except:
            i = "sop出错"
        list_temp2 = [i]
        for i in sop.findAll("div",{"class","sl-key"}):
            i = i.get_text()
            i = i.replace("\n","")
            i = i.replace("\t","")            
            list_temp1.append(i)
        for i in sop.findAll("div",{"class","sl-value"}):
            i = i.get_text()
            i = i.replace("\n","")
            i = i.replace("\t","")
            i = i.replace("确定取消","")
            list_temp2.append(i)
        print(list_temp1[2:])
        for i in range(0,20):
            try:                
                list_temp.append(list_temp1[i])
                list_temp.append(list_temp2[i])
            except:
                break
        if numi % 97 == 0:
            file2.close()
            file2 = open("导出-"+time.strftime("%Y-%m-%d",time.localtime())+".xls","a")
        for i in list_temp:
            file2.write(i)
            file2.write("\t")
        file2.write("\n")
        numi +=1
    except:
        print("出错啦")
file2.close()
