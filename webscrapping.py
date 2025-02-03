import requests
import pandas as pd
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme")
sou=BeautifulSoup(response.content,'html.parser')

names=sou.find_all('div',class_="KzDlHZ")
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
else:    
    name.append("No name available")
prices=sou.find_all('div',class_="Nx9bqj _4b5DiR")
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
else:
    price.append("No price available")
images=sou.find_all('img',class_="DByuf4")
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
else:
    image.append("No image available")
ratings=sou.find_all('div',class_="XQDdHH")
rates=[]
for i in ratings[0:20]:    
    d = i.get_text()
    rates.append(float(d))
else:
    rates.append("No ratings available")

memory=sou.find_all('li',class_="J+igdf")
ram=[]
for i in memory[0:20]:
    try:
        d=i.get_text()
        if 'RAM' in d and 'ROM' in d:
            ram.append(d)
        else:
            ram.append("No memory information")
    except:
        ram.append("No memory information")
    d=i.get_text()
    if 'RAM' in d and 'ROM' in d:
        ram.append(d)
    else:
        ram.append("No memory information")
links=sou.find_all('a',class_="CGtC98")
link=[]
for i in links[0:20]:
    href = i.get('href')
    if href:
        link.append("https://www.flipkart.com" + href)
    else:
        link.append("No link available")
max_length = min(len(name), len(price), len(image), len(rates), len(ram), len(link))

name = name[:max_length]
price = price[:max_length]
image = image[:max_length]
rates = rates[:max_length]
ram = ram[:max_length]
link = link[:max_length]
df=pd.DataFrame() # row columns
df["Names"]=name
df["Prices"]=price
df["Images"]=image
df["ratings"]=rates
df["memory"]=ram
df["Links"]=link
df.to_csv('mobiles info.csv')