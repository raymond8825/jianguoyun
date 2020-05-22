import requests
import re
from bs4 import BeautifulSoup


def getHtml(url):
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = "utf-8"  # 此步骤非常重要，否则乱码
    return r.text


def getInfo(html):
    stockList = []
    soup = BeautifulSoup(html, "html.parser")
    with open("c:/Users/PeterLei/Desktop/stock.html", "w", encoding="utf-8") as f:
        # f.write(soup.prettify())# soup的属性为string类型
        f.close()
        print("文件写入完成")
    for a in soup.find_all("a"):  # 遍历html中所有的a标签，当然就存在不符合要求的a标签，要做处理
        try:
            stockList.append(re.findall(r"\d{6}", a.attrs["href"])[0])
        except:
            continue
    return stockList


def printInfo(urlStock, stockList):
    for i in stockList:
        try:
            stockInfo = urlStock+i
            r = requests.get(stockInfo)
            r.raise_for_status()
            print(r.url)
            soup = BeautifulSoup(r.text, "html.parser")
            # 拿到股票的名字和编号
            name = soup.find("p", attrs={"class": "title"}).string
            # 拿到所有的td标签的集合
            spanList = soup.find_all("tbody")[1].find_all("span")
            # 新建一个字典用于保存该股票的属性
            kv = {}
            kv["name"] = name
            for attrs in spanList:
                # print(attrs.text)
                # print(attrs.parent.text.split(":"))
                kv[attrs.parent.text.split(":")[0]] = attrs.parent.text.split(":")[1]
            for key in kv:
                print("{0}:{1}".format(key, kv[key]))
            with open(r"C:\Users\PeterLei\Desktop\test.txt","a") as f:
                f.write(str(kv)+"\n")
        except:
            continue



def main():
    url = "http://quote.eastmoney.com/stock_list.html"
    urlStock = "https://www.laohu8.com/hq/s/"
    html = getHtml(url)  # 东方财富网上爬取所有股票名称
    stockList = getInfo(html)
    printInfo(urlStock, stockList)


main()