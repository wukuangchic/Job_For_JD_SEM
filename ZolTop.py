def O_W(T_url):##将一张网页的品牌排名导出,导出第一个元素是品牌排行，第二个元素是下一个查找的产品排行网址
    try:
        web = BeautifulSoup(urlopen(T_url).read())
        L_tAll = []
        L_t = []
        title = web.find("li",{"class","active"})
        title = str(title.get_text())
        title = title.replace("品牌排行","")
        print("%s\n本次获取排行榜:%s"%(T_url,title))
        rank = 1
        for brand in web.findAll("a",{"class","name"}):
            B_name = brand.get_text()
            print("第%d名：%s"%(rank,B_name))
            L_temp = [title,str(rank),B_name]
            L_t.append(L_temp)
            rank += 1
        L_tAll.append(L_t)
        goods = (web.find("a",text=("热门"+str(L_t[0][0])+"排行"))).get("href")
        L_tAll.append(goods)
        return(L_tAll)
    except:
        return([0,0])
def F_O(P_O):##将品牌导出到Excel
    try:
        F_file= open("中关村品牌排名"+time.strftime("%Y-%m-%d",time.localtime())+".xls","a")
        for F_1 in P_O:
            for F_2 in F_1:
                F_file.write(F_2)
                F_file.write("\t")
            F_file.write("\n")
        F_file.close()
        temp = P_O[0][0]
        return(temp)
    except:
        temp=0
def G_O(T_url):##获取产品排行
    try:
        web = BeautifulSoup(urlopen(str(T_url)).read())
        L_t = []
        title = web.find("li",{"class","active"})
        title = str(title.get_text())
        title = title.replace("排行","").replace("热门","")
        print("%s\n%s的产品排行榜:"%(T_url,title))
        rank = 1
        for goods in web.findAll("div",{"class","rank__name"}):
            G_name = goods.get_text()
            print("第%d名：%s"%(rank,G_name))
            L_temp = [title,str(rank),G_name]
            L_t.append(L_temp)
            rank += 1
        return(L_t)
    except:
        return([0,0])
def F_O2(P_O):##将产品导出到Excel
    try:
        F_file= open("中关村产品排名"+time.strftime("%Y-%m-%d",time.localtime())+".xls","a")
        for F_1 in P_O:
            for F_2 in F_1:
                F_file.write(F_2)
                F_file.write("\t")
            F_file.write("\n")
        F_file.close()
        temp = P_O[0][0]
        return(temp)
    except:
        temp=0
temp = input("本程序将在同一目录下创建Excel文件\n各类别排行将导入到此Excel表格中\n按回车键继续")
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
for P_num in range(0,2000):
    P_num = str(P_num)
    W_url = ("http://top.zol.com.cn/compositor/"+P_num+"/manu_attention.html")
    P_Out = O_W(W_url)
    F_O(P_Out[0])
    G_Out = G_O(P_Out[1])
    F_O2(G_Out)
