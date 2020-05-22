import requests
from bs4 import BeautifulSoup

url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
useragent={"user-agent":"Mozilla/5.0"}
cookies={"cookies":"cna=JwquFEooaAsCAXu1+I2M2ilq; sca=c23abb04; cnaui=1692793887; aui=1692793887; cdpid=Uoe9b65j9YRtFw%253D%253D; cap=2bab; cmida=1401053355_20190826224208; yunpk=1771966837168880; cad=g4slJsVktqLhXQ+I5FemAwFS9SCfxzBtPbzuoQ9+7pA=0001; tbsa=f84a6a8346c26e3f236fc331_1568638953_8; atpsida=14ecb100dc209e4acce0fb21_1568638953_8; atpsidas=350497fb1b12d0209e684b0d_1568638953_8"}
r=requests.get(url,headers=useragent,cookies=cookies)
print(r.status_code)
soup=BeautifulSoup(r.text,"html.parser")
with open("c:/Users/PeterLei/Desktop/amazon.html","wb") as f:
    f.write(soup.prettify().encode(encoding="utf-8"))
    f.close()
print("done")









