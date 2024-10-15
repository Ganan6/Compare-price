import requests
import json
import ssl
import certifi

from bs4 import BeautifulSoup

# Imitate the Mozilla browser
user_agent={'User-agent':'Mozilla/5.0'}

def compare_price(product_laughs,product_glomark):
    super = requests.get( product_laughs)
    soup_super=BeautifulSoup(super.content,'html.parser')   # Parsing HTML data
    super_price_id=soup_super.find(id='product-price-105320')   # Find id from source code and extracting the details needed
    price_element=super_price_id.find('span', class_='price')
    price_laughs_str=price_element.text.strip()
    price_laughs=float(price_laughs_str.replace('Rs.','').strip())  # Replacing Rs. with empty string to make it a float
    # print(price_laughs)
    super_product_name=soup_super.find('div', class_='product-name')
    product_name_lau=super_product_name.text.strip()
    product_name_laughs=product_name_lau.split()[0] # Splitting using space and taking 1st word
    # print(product_name_laughs)

    glo=requests.get(product_glomark)
    soup_glo=BeautifulSoup(glo.content,'html.parser')
    soup_glo_id=soup_glo.find('script', type='application/ld+json')
    json_data_str=soup_glo_id.string
    json_data=json.loads(json_data_str)
    price_glomark=float(json_data['offers'][0]['price'])
    # print(price_glomark)
    product_name_glomark=json_data['name']
    # print(product_name_glomark)

    print (f"Laugh's {product_name_laughs} is LKR {price_laughs}" )
    print(f"Glomark's {product_name_glomark} is LKR {price_glomark}")

    if price_glomark < price_laughs:
        dif=(price_laughs-price_glomark)
        print(f"Glomark's {product_name_glomark} is LKR{dif} cheaper")
        print(f"Buy Glomark's {product_name_glomark}")
    elif price_laughs<price_glomark:
        dif=(price_glomark-price_laughs)
        print(f"Laugh's {product_name_laughs} is LKR{dif} cheaper")
        print(f"Buy Laugh's {product_name_laughs}")
    else:
        print("Both prices are same")

compare_price('https://scrape-sm1.github.io/site1/COCONUT%20market1super.html','https://glomark.lk/coconut/p/11624')







