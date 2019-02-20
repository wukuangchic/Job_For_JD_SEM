def get_brand_searchurl(i):##品牌名转换为京东搜索结果页
    try:
        import sys
        temp1 = str(i.encode("utf-8"))
        temp2 = "https://search.jd.com/Search?keyword="+(temp1.replace("b'\\x","%").replace("\\x","%").replace("b'",""))[:-1]+"&enc=utf-8"
        print(temp2)
        return(temp2)
    except:
        print("获取品牌错误")
def find_brand_url(i):##打开品牌名搜索结果页
    try:
        from bs4 import BeautifulSoup
        from urllib.request import urlopen
        temp3 = BeautifulSoup(urlopen(i).read(),"lxml")
        return(temp3)
    except:
        print("打开搜索结果页错误")
def get_url_name(i):##获取店铺名称及链接
    try:
        from bs4 import BeautifulSoup
        for each_line in i.findAll("a"):
            getext = each_line.get_text()
            if getext == "进入店铺":
                geturl = each_line.get("href")
                print("http:%s"%geturl)
                for each_line in i.findAll("a"):
                    geturl_temp = each_line.get("href")
                    if geturl_temp == geturl:
                        getext = each_line.get_text()
                        if "店" in getext and "进入店铺" != getext:
                            print(getext)
                            return([getext,"http:"+geturl])
                            break
                break                
    except:
        print("获取链接错误")


print('本程序依赖于BeauifulSoup4库\n在本程序相同目录下\n命名“temp_brand_prlist.csv”文件\n表格第一列为所需抓取旗舰店地址的品牌\n按回车键继续')
temp = input('')
list2 = []
file = open("temp_brand_prlist.csv",)
for each in file.readlines():
    each = each.strip('\n')
    gbs_each = get_brand_searchurl(each)
    fb_each = find_brand_url(gbs_each)
    list_each = get_url_name(fb_each)
    try:
        list_each.append(each)
    except:
        list_each=["","",each]
    file_out = open("print_brand_list.csv","a")
    for each in list_each:
        file_out.write(each)
        file_out.write(",")
    file_out.write('\n')
print("程序结束\n已命名文件“print_brand_list.csv”")
    
    

