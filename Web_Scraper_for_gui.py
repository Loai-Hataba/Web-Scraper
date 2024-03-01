import time
import requests
from bs4 import BeautifulSoup
import sys
import pandas as pd
import os
from icecream import ic
animal = ''
chosen_section = ''
global products_done
global pages_done
# menu
def menu():
    # url to be modified for each product
    select_url = ''
    global animal
    category = ''
    print("made by Loai Hataba\n\n" +
        " " * 15 + "Web Scrapper 2.0\n\n"
                     "Categories:\n"
                     "A) Cats\n"
                     "B) Dogs\n"
                     "C) Birds\n"
                     "D) Small animals\n"
                     "E) Exit Program")
    category = input('Choose a category: ').upper()
    print('\n')
    if category == 'A':
        animal = 'Cats'
        select_url = section(animal)
    elif category == 'B':
        animal = 'Dogs'
        select_url = section(animal)
    elif category == 'C':
        animal = 'Birds'
        select_url = section(animal)
    elif category == 'D':
        animal = 'Small Animals'
        select_url = section(animal)
    elif category == 'E':
        quit()
    else:
        print("Invalid, please choose a valid category")
        menu()
    scrap(select_url, animal)


# categories
def section(animal, category):
    sections = ['Food', 'Health & Beauty', 'Toys', 'Food Supplies', 'Treats & Supplements', 'Accesories', 'Beds & Carriers', 'Training and Cleaning',
                'Scrapers', 'Sand & its Accessories', 'Cages & Accessories', 'Reptiles']
    global chosen_section
    section_url = ''
    if animal.lower() == 'cats':
        if category.lower() == 'food':
            chosen_section = 'food'
            section_url = '%D8%AC%D9%85%D9%8A%D8%B9-%D8%B7%D8%B9%D8%A7%D9%85-%D8%A7%D9%84%D9%82%D8%B7%D8%B7'
        elif category.lower() == 'health & beauty':
            chosen_section = 'health & beauty'
            section_url = '%D8%A7%D9%84%D8%B5%D8%AD%D8%A9-%D9%88%D8%A7%D9%84%D8%AC%D9%85%D8%A7%D9%84-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
        elif category.lower() == 'toys':
            chosen_section = 'toys'
            section_url = '%D8%A3%D9%84%D8%B9%D8%A7%D8%A8-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
        elif category.lower() == 'food supplies':
            chosen_section = 'food supplies'
            section_url = '%D9%85%D8%B3%D8%AA%D9%84%D8%B2%D9%85%D8%A7%D8%AA-%D8%A7%D9%84%D8%B7%D8%B9%D8%A7%D9%85'
        elif category.lower() == 'treats & supplements':
            chosen_section = 'treats & supplements'
            section_url = '%D9%85%D9%83%D8%A7%D9%81%D8%A2%D8%AA-%D9%88%D9%85%D9%83%D9%85%D9%84%D8%A7%D8%AA-%D8%A7%D9%84%D9%82%D8%B7%D8%B7'
        elif category.lower() == 'accesories':
            chosen_section = 'accesories'
            section_url = '%D8%A7%D9%84%D8%A5%D9%83%D8%B3%D8%B3%D9%88%D8%A7%D8%B1%D8%A7%D8%AA'
        elif category.lower() == 'beds & carriers':
            chosen_section = 'beds & carriers'
            section_url = '%D8%A7%D9%84%D8%A3%D8%B3%D8%B1%D8%A9-%D9%88%D8%A7%D9%84%D9%86%D9%88%D8%A7%D9%82%D9%84'
        elif category.lower() == 'training and cleaning':
            chosen_section = 'training and cleaning'
            section_url = '%D8%A7%D9%84%D8%AA%D8%AF%D8%B1%D9%8A%D8%A8-%D9%88%D8%A7%D9%84%D8%AA%D9%86%D8%B8%D9%8A%D9%81'
        elif category.lower() == 'scrapers':
            chosen_section = 'scrapers'
            section_url = '%D8%AE%D8%AF%D8%A7%D8%B4%D8%A7%D8%AA-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
        elif category.lower() == 'sand and its accessories':
            chosen_section = 'sand and its accessories'
            section_url = '%D8%A7%D9%84%D8%B1%D9%85%D9%84-%D9%88%D9%85%D8%B3%D8%AA%D9%84%D8%B2%D9%85%D8%A7%D8%AA%D9%87-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
    elif animal.lower() == 'dogs':
        if category.lower() == 'food':
            chosen_section = 'food'
            section_url = '%D8%AC%D9%85%D9%8A%D8%B9-%D8%B7%D8%B9%D8%A7%D9%85-%D8%A7%D9%84%D9%83%D9%84%D8%A7%D8%A8-1'
        elif category.lower() == 'health & beauty':
            chosen_section = 'health & beauty'
            section_url = '%D8%A7%D9%84%D8%B5%D8%AD%D8%A9-%D9%88%D8%A7%D9%84%D8%AC%D9%85%D8%A7%D9%84-%D8%A7%D9%84%D9%83%D9%84%D8%A7%D8%A8'
        elif category.lower() == 'toys':
            chosen_section = 'toys'
            section_url = '%D8%A7%D9%84%D8%A3%D9%84%D8%B9%D8%A7%D8%A8-%D8%A7%D9%84%D9%83%D9%84%D8%A7%D8%A8'
        elif category.lower() == 'food supplies':
            chosen_section = 'food supplies'
            section_url = '%D9%85%D8%B3%D8%AA%D9%84%D8%B2%D9%85%D8%A7%D8%AA-%D8%A7%D9%84%D8%B7%D8%B9%D8%A7%D9%85-%D8%A7%D9%84%D9%83%D9%84%D8%A7%D8%A8'
        elif category.lower() == 'treats & supplements':
            chosen_section = 'treats & supplements'
            section_url = '%D9%85%D9%83%D8%A7%D9%81%D8%A2%D8%AA-%D9%88%D9%85%D9%83%D9%85%D9%84%D8%A7%D8%AA-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
        elif category.lower() == 'accesories':
            chosen_section = 'accesories'
            section_url = '%D8%A7%D9%84%D8%A5%D9%83%D8%B3%D8%B3%D9%88%D8%A7%D8%B1%D8%A7%D8%AA-%D8%A7%D9%84%D9%83%D9%84%D8%A7%D8%A8'
        elif category.lower() == 'beds & carriers':
            chosen_section = 'beds & carriers'
            section_url = '%D8%A3%D8%B3%D8%B1%D9%91%D8%A9-%D9%88%D8%A8%D9%8A%D9%88%D8%AA-%D9%88%D9%86%D9%88%D8%A7%D9%82%D9%84-%D8%A7%D9%84%D9%83%D9%84%D8%A7%D8%A8'
        elif category.lower() == 'training and cleaning':
            chosen_section = 'training and cleaning'
            section_url = '%D8%A7%D9%84%D8%AA%D8%AF%D8%B1%D9%8A%D8%A8-%D9%88%D8%A7%D9%84%D8%AA%D9%86%D8%B8%D9%8A%D9%81-%D8%A7%D9%84%D9%83%D9%84%D8%A7%D8%A8'
    elif animal.lower() == 'birds':
        if category.lower() == 'health & beauty':
            chosen_section = 'health & beauty'
            section_url = '%D8%A7%D9%84%D8%B5%D8%AD%D8%A9-%D9%88%D8%A7%D9%84%D8%B1%D8%B9%D8%A7%D9%8A%D8%A9-%D8%A7%D9%84%D8%B7%D9%8A%D9%88%D8%B1'
        elif category.lower() == 'toys':
            chosen_section = 'toys'
            section_url = '%D8%A7%D9%84%D8%A3%D9%84%D8%B9%D8%A7%D8%A8-%D8%A7%D9%84%D8%B7%D9%8A%D9%88%D8%B1'
        elif category.lower() == 'food':
            chosen_section = 'food'
            section_url = '%D8%AC%D9%85%D9%8A%D8%B9-%D8%B7%D8%B9%D8%A7%D9%85-%D8%A7%D9%84%D8%B7%D9%8A%D9%88%D8%B1'
        elif category.lower() == 'cages & accesories':
            chosen_section = 'cages & accesories'
            section_url = '%D8%A7%D9%84%D8%A3%D9%82%D9%81%D8%A7%D8%B5-%D9%88%D9%85%D8%B3%D8%AA%D9%84%D8%B2%D9%85%D8%A7%D8%AA%D9%87%D8%A7-%D8%A7%D9%84%D8%B7%D9%8A%D9%88%D8%B1'
    elif animal.lower() == 'small animals':
        if category.lower() == 'health & beauty':
            chosen_section = 'health & beauty'
            section_url = '%D8%A7%D9%84%D8%B5%D8%AD%D8%A9-%D9%88%D8%A7%D9%84%D8%B1%D8%B9%D8%A7%D9%8A%D8%A9-%D9%84%D9%84%D8%AD%D9%8A%D9%88%D8%A7%D9%86%D8%A7%D8%AA-%D8%A7%D9%84%D8%B5%D8%BA%D9%8A%D8%B1%D9%87'
        elif category.lower() == 'toys':
            chosen_section = 'toys'
            section_url = '%D8%A7%D9%84%D8%A3%D9%84%D8%B9%D8%A7%D8%A8-%D9%84%D9%84%D8%AD%D9%8A%D9%88%D8%A7%D9%86%D8%A7%D8%AA-%D8%A7%D9%84%D8%B5%D8%BA%D9%8A%D8%B1%D9%87'
        elif category.lower() == 'food':
            chosen_section = 'food'
            section_url = '%D8%AC%D9%85%D9%8A%D8%B9-%D8%B7%D8%B9%D8%A7%D9%85-%D8%A7%D9%84%D8%AD%D9%8A%D9%88%D8%A7%D9%86%D8%A7%D8%AA-%D8%A7%D9%84%D8%B5%D8%BA%D9%8A%D8%B1%D8%A9'
        elif category.lower() == 'cages & accesories':
            chosen_section = 'cages & accesories'
            section_url = '%D8%A7%D9%84%D8%A3%D9%82%D9%81%D8%A7%D8%B5-%D9%88%D9%85%D8%B3%D8%AA%D9%84%D8%B2%D9%85%D8%A7%D8%AA%D9%87%D8%A7-%D9%84%D9%84%D8%AD%D9%8A%D9%88%D8%A7%D9%86%D8%A7%D8%AA-%D8%A7%D9%84%D8%B5%D8%BA%D9%8A%D8%B1%D9%87'
        elif category.lower() == 'reptiles':
            chosen_section = 'reptiles'
            section_url = '%D8%B2%D9%88%D8%A7%D8%AD%D9%81'
    return section_url


# Web Scraping
def scrap(url, animal, path, category):
    animal_temp = []
    category_temp = []
    global products_done
    products_done = 0
    global pages_done
    pages_done = 0
    product_links = []
    animal_products = []
    baseurl = 'https://aleef.com/en/collections/'
    # identify the user visiting the website
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    # API's
    r1 = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(r1.content, 'lxml')

    # get final page number
    try:
        page_number_temp = (soup1.find_all('li', {'class': 'pagination-num'}))
        page_number = page_number_temp[-1].text.strip()
    except:
        page_number = 1

# go through all pages
    for x in range(1, int(page_number)+1):
        #requesting the url
        r = requests.get(f'{url}?page={x}', headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        product_list = soup.find_all('li', class_='product')
        # go through each product
        for item in product_list:
            # find <a> and enter href value (links in href)
            for link in item.find_all('a', href = True):
                # access tag
                product_links.append(baseurl + link['href'])
                break
        pages_done += 1


    for link in product_links:
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        try:
            product_name = (soup.find('h1', class_='productView-title').text.strip())
        except:
            product_name = 'Not found' + str(products_done)
        try:
            product_price_temp = (soup.find('span', class_='price-item').text.strip())
        except:
            product_price_temp = 'Not found' + str(products_done)
        try:
            product_description = (soup.find('div', class_='tab-popup-content').text.strip())
        except:
            product_description = 'Not found' + str(products_done)
        try:
            product_brand = (soup.find('span', class_='productView-info-value').text.strip())
        except:
            product_brand = 'Not found' + str(products_done)
        try:
            product_image = (soup.find('div', class_='media', href = True))['href']
        except:
            product_image = 'Not found' + str(products_done)

        # price algorithm
        product_price_temp2 = ''
        for j in product_price_temp:
            if j.isdigit() or j == '.':
                product_price_temp2 += j
            if len(product_price_temp2) > 4:
                break
        product_price_temp3 = (product_price_temp2.split('.'))[0] + '.' + product_price_temp2.split('.')[1]
        product_price = (float(product_price_temp3))

        image_downloader(products_done, product_name, animal, category, product_image,path)

        productsss = {
            'Name': product_name,
            'Brand': product_brand,
            'Price': product_price,
            'Description': product_description,
            'Image': product_image
        }
        animal_products.append(productsss)
        products_done += 1
    export(animal_products, path, animal, category)



# download image
def image_downloader(products_done, product_name, animal, category, product_image, path):
    os.makedirs(rf'{path}\{animal}-{category}', exist_ok=True)
    # identify the user visiting the website
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    # download picture
    image_name_temp = str(products_done) + ' ' + product_name.replace(r"\\", '').replace('\"', '').replace(repr(r"\n"), '').replace('<', '').replace('>', '').replace('?', '').replace('*', '')
    image_name = ''
    i = 0
    # delete tages <..>
    while i < len(image_name_temp):
        if image_name_temp[i] == "<":
            j = i + 1
            while j < len(image_name_temp):
                if image_name_temp[j] == '>':
                    i = j + 1
                    break
                j += 1
        if image_name_temp[i].isspace():
            image_name += ' '
        else:
            image_name += image_name_temp[i]
        i += 1
    #     download image
    try:
        with open(rf'{path}\{animal}-{category}\{image_name}.jpg', 'wb') as f:
            im = requests.get(f'https:{product_image}', headers=headers)
            f.write(im.content)
    except:
        with open(rf'{path}\{animal}-{category}\{products_done}.jpg', 'wb') as f:
            im = requests.get(f'https:{product_image}', headers=headers)
            f.write(im.content)


# Export CSV
def export(data, path, animal, category):
    df = pd.DataFrame(data)
    df.to_csv(rf'{path}\{animal}-{category}\{animal} {category}.csv', encoding='utf-8-sig')
    print("File Created Succesfully...")

# scrap('https://aleef.com/en/collections/%D8%B2%D9%88%D8%A7%D8%AD%D9%81', 'Dogs',  r'C:\Users\loaiw\OneDrive\Desktop\Webscraper', 'food')
# menu()
# time.sleep(5)