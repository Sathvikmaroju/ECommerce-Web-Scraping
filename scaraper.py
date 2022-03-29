import requests
from bs4 import BeautifulSoup 
import csv 


def get_title(string):
    x=5
    while True:
        res=''
        if (string[x-5:x]=='title' and string[x-6:x-5]!='"'):
            res +=string[x+2:]
            return res.split('"')[0]
        else:
            x+=1

webpage = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")

soup = BeautifulSoup(webpage.content,features="lxml")
div_soup = soup.find_all("div", class_="col-sm-4 col-lg-4 col-md-4")

data=[]
for i in div_soup:
    product_name = get_title(str(i.find('a',class_='title')))
    product_price = i.find('h4').text
    Rating = len(i.find_all('span',class_='glyphicon glyphicon-star'))
    reviews_count = i.find('p',class_='pull-right').text.split()[0]
    
    data.append([product_name, product_price, Rating, reviews_count])


fields = ['Product Name', 'Product Price', 'Rating','Reviews Count'] 

with open('laptops.csv', 'w') as file: 
    csvwriter = csv.writer(file) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(data)

