import requests
import pandas as pd
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_="KzDlHZ")
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)



prices=soup.find_all('div',class_="Nx9bqj _4b5DiR")
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)


rates=soup.find_all('div',class_="XQDdHH")
rate=[]
for i in rates[0:20]:
    d=i.get_text()
    rate.append(float(d))



images=soup.find_all('img',class_="DByuf4")
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)



links=soup.find_all('a',class_="CGtC98")
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)


df=pd.DataFrame()
df["Name"]=name
df["Price"]=price
df["Rating"]=rate
df["Images"]=image
df["Links"]=link
print(df)

df.to_csv("Mobiledes.csv")