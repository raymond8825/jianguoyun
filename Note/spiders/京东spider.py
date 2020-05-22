import requests


r=requests.get("https://item.jd.com/100006635632.html")
r.raise_for_status()
#r.apparent_encoding=r.encoding
with open("c:Users/PeterLei/Desktop/jingdong.html","w") as f:
    f.write(r.text)
    f.close
        