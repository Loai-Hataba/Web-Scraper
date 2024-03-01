import time
import requests
from bs4 import BeautifulSoup
import sys
import pandas as pd
import os
animal = ''
chosen_section = ''
# menu



def menu():
    # url to be modified for each product
    select_url = ''
    category = ''
    global animal
    print("\nmade by Loai Hataba\n\n" +
        " " * 15 + "Web Scrapper 2.0\n\n"
                     "Categories:\n"
                     "A) Cats\n"
                     "B) Dogs\n"
                     "C) Birds\n"
                     "D) Reptiles\n"
                     "E) Small Pets\n"
                     "F) Exit Program")
    category = input('Choose a category: ').upper()
    print('\n')
    if category == 'A':
        animal = 'Cats'
    elif category == 'B':
        animal = 'Dogs'
    elif category == 'C':
        animal = 'Birds'
    elif category == 'D':
        animal = 'Reptiles'
    elif category == 'E':
        animal = 'Small Pets'
    elif category == 'F':
        quit()
    else:
        print("Invalid, please choose a valid category")
        menu()
    sec = section(animal)
    products = scrap(sec[0], sec[1])
    export(products, sec[1])


# categories
def section(animal):
    category = ''
    file_name = ''
    sections = ['Food', 'Health & Beauty', 'Toys', 'Food Supplies', 'Treats & Supplements', 'Accesories', 'Beds & Carriers', 'Training and Cleaning',
                'Scrapers', 'Sand & its Accessories', 'Cages & Accessories', 'Reptiles']
    section_url = ''
    # cats
    if animal.lower() == 'cats':
        print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                        f'A) Accesories\n'
                        f'B) Beds & Carriers\n'
                        f'C) Food\n'
                        f'D) Food Supplies\n'
                        f'E) Health & Beauty\n'
                        f'F) Treats & Supplements\n'
                        f'G) Sand & its Accessories\n'
                        f'H) Toys\n'
                        f'I) Training and Cleaning\n'
                        f'J) Scrapers\n'
                        f'K) Back\n'
                        f'L) Quit')
        category = input('Choose a category: ')
        # accessories
        if category.lower() == 'a':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                            f'A) Clothes\n'
                            f'B) Collars\n'
                            f'C) Leahses\n'
                            f'D) Necklaces\n'
                            f'E) Waistcoats\n'
                            f'F) Back\n'
                            f'G) Exit')
            category = input('Choose a category: ')
            # clothes
            if category.lower() == 'a':
                section_url = '%D9%85%D9%84%D8%A7%D8%A8%D8%B3-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Accessories-Clothes'
            #     collars
            elif category.lower() == 'b':
                section_url = '%D8%A3%D8%B7%D9%88%D8%A7%D9%82-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Accessories-Collars'
            # corsets
            elif category.lower() == 'c':
                section_url = '%D9%85%D8%B4%D8%AF%D8%A7%D8%AA-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Accessories-Corsets'
            # necklaces
            elif category.lower() == 'd':
                section_url = '%D9%82%D9%84%D8%A7%D8%A6%D8%AF-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Accessories-Necklaces'
            # waistcoats
            elif category.lower() == 'e':
                section_url = '%D8%B5%D8%AF%D8%B1%D9%8A%D8%A7%D8%AA-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Accessories-Waistcoats'
            # back
            elif category.lower() == 'f':
                menu()
            # exit
            elif category.lower() == 'g':
                quit()
            else:
                print('Invalid!')
        # beds and carriers
        elif category.lower() == 'b':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                            f'A) Beds\n'
                            f'B) Carriers\n'
                            f'C) Huts\n'
                            f'D) Back\n'
                            f'E) Exit')
            category = input('Choose a category: ')
            # beds
            if category.lower() == 'a':
                print('\n' + ' ' * 5 + f'Available categories:\n'
                                'A) Closed\n'
                                'B) Opened\n'
                                'C) Exit')
                category = input('Choose a category: ')
                # closed
                if category.lower() == 'a':
                    section_url = '%D8%A7%D8%B3%D8%B1%D9%87-%D9%85%D8%BA%D9%84%D9%82%D8%A9-%D9%82%D8%B7%D8%B7'
                    file_name = 'Cat-Beds & Carriers-Beds-Closed'
                # opened
                elif category.lower() == 'b':
                    section_url = '%D8%A7%D8%B3%D8%B1%D9%87-%D9%88%D8%B3%D8%A7%D8%A6%D8%AF-%D9%82%D8%B7%D8%B7'
                    file_name = 'Cat-Beds & Carriers-Beds-Opened'
                # exit
                elif category.lower() == 'c':
                    quit()
                else:
                    print('Invalid!')
            #     carriers
            elif category.lower() == 'b':
                print('\n' + ' ' * 5 + f'Available categories:\n'
                                'A) Bag\n'
                                'B) Box\n'
                                'C) Exit')
                category = input('Choose a category: ')
                # bag
                if category.lower() == 'a':
                    section_url = '%D9%86%D9%88%D8%A7%D9%82%D9%84-%D8%B4%D9%86%D8%B7-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                    file_name = 'Cat-Beds & Carriers-Carriers-Bag'
                # box
                elif category.lower() == 'b':
                    section_url = '%D9%86%D9%88%D8%A7%D9%82%D9%84-%D9%82%D8%B7%D8%B7-%D8%B5%D9%86%D8%A7%D8%AF%D9%8A%D9%82'
                    file_name = 'Cat-Beds & Carriers-Carriers-Box'
                # exit
                elif category.lower() == 'c':
                    quit()
                else:
                    print('Invalid!')
            # huts
            elif category.lower() == 'c':
                section_url = '%D8%A8%D9%8A%D9%88%D8%AA-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Beds & Carriers-Huts'
            # back
            elif category.lower() == 'd':
                menu()
            # exit
            elif category.lower() == 'e':
                quit()
            else:
                print('Invalid!')
        # food
        elif category.lower() == 'c':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                            'A) Dry\n'
                            'B) Wet\n'
                            'C) Exit')
            category = input('Choose a category: ')
            # Dry
            if category.lower() == 'a':
                print('\n' + ' ' * 5 + f'Available categories:\n'
                                'A) Adult\n'
                                'B) Kitten\n'
                                'C) Old\n'
                                'D) Exit')
                category = input('Choose a category: ')
                # adult
                if category.lower() == 'a':
                    section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%AC%D8%A7%D9%81-%D9%84%D9%84%D9%82%D8%B7%D8%B7-%D9%83%D8%A8%D9%8A%D8%B1%D8%A9-%D8%A7%D9%84%D8%B3%D9%86'
                    file_name = 'Cat-Food-Dry-Adult'
                # kitten
                elif category.lower() == 'b':
                    section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%AC%D8%A7%D9%81-%D9%84%D9%84%D9%83%D8%AA%D9%8A%D9%86'
                    file_name = 'Cat-Food-Dry-Kitten'
                # old
                elif category.lower() == 'c':
                    section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%AC%D8%A7%D9%81-%D9%84%D9%84%D9%82%D8%B7%D8%B7-%D8%A7%D9%84%D8%A8%D8%A7%D9%84%D8%BA%D8%A9'
                    file_name = 'Cat-Food-Dry-Old'
                #     exit
                elif category.lower() == 'd':
                    quit()
                else:
                    print('Invalid!')
            # Wet
            elif category.lower() == 'b':
                print('\n' + ' ' * 5 + f'Available categories:\n'
                                'A) Cans\n'
                                'B) Satches\n'
                                'C) Soup\n'
                                'D) Exit')
                category = input('Choose a category: ')
                # cans
                if category.lower() == 'a':
                    section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B1%D8%B7%D8%A8-%D9%82%D8%B7%D8%B7-%D9%85%D8%B9%D9%84%D8%A8%D8%A7%D8%AA'
                    file_name = 'Cat-Food-Wet-Cans'
                # staches
                elif category.lower() == 'b':
                    section_url = '%D8%A7%D9%83%D9%84-%D8%B1%D8%B7%D8%A8-%D9%82%D8%B7%D8%B7-%D8%A7%D8%B8%D8%B1%D9%81'
                    file_name = 'Cat-Food-Wet-Satches'
                # soup
                elif category.lower() == 'c':
                    section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B1%D8%B7%D8%A8-%D9%82%D8%B7%D8%B7-%D8%B4%D9%88%D8%B1%D8%A8%D8%A9'
                    file_name = 'Cat-Food-Wet-Soup'
                #     exit
                elif category.lower() == 'd':
                    quit()
                else:
                    print('Invalid!')
            # exit
            elif category.lower() == 'c':
                quit()
            else:
                print('Invalid!')
        # food supplies
        elif category.lower() == 'd':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                            f'A) Food Containers\n'
                            f'B) PLates\n'
                            f'C) Exit')
            category = input('Choose a category: ')
            # container
            if category.lower() == 'a':
                section_url = '%D8%AD%D8%A7%D9%81%D8%B8%D8%A7%D8%AA-%D8%B7%D8%B9%D8%A7%D9%85-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Food Supplies-Container'
            #     plates
            elif category.lower() == 'b':
                section_url = '%D8%A7%D8%B7%D8%A8%D8%A7%D9%82-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Food Supplies-Plates'
            #     exit
            elif category.lower() == 'c':
                quit()
            else:
                print('Invalid!')
        # health and beauty
        elif category.lower() == 'e':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                            f'A) Hair & Claw care\n'
                            f'B) Health Care\n'
                            f'C) Shampoo & Perfumes\n'
                            f'D) Wet Tissues\n'
                            f'E) Exit')
            category = input('Choose a category: ')
            # claw
            if category.lower() == 'a':
                section_url = '%D8%A7%D9%84%D8%B9%D9%86%D8%A7%D9%8A%D8%A9-%D8%A8%D8%A7%D9%84%D8%B4%D8%B9%D8%B1-%D9%88%D8%A7%D9%84%D9%85%D8%AE%D8%A7%D9%84%D8%A8-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Health & Beauty-Claw & hair'
            #     Health care
            elif category.lower() == 'b':
                section_url = '%D8%A7%D9%84%D8%B9%D9%86%D8%A7%D9%8A%D8%A9-%D8%A7%D9%84%D8%B5%D8%AD%D9%8A%D8%A9-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Health & Beauty-Health Care'
            #     shampoo
            elif category.lower() == 'c':
                section_url = '%D8%B4%D8%A7%D9%85%D8%A8%D9%88-%D9%88%D8%B9%D8%B7%D9%88%D8%B1'
                file_name = 'Cat-Health & Beauty-Shampoo'
            #     wet tissue
            elif category.lower() == 'd':
                section_url = '%D9%85%D9%86%D8%A7%D8%AF%D9%8A%D9%84-%D8%B1%D8%B7%D8%A8%D8%A9-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Health & Beauty-Wet Tissue'
            #     exit
            elif category.lower() == 'e':
                quit()
            else:
                print('Invalid!')
        # treats
        elif category.lower() == 'f':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                            f'A) Treats\n'
                            f'B) Supplements\n'
                            f'C) Exit')
            category = input('Choose a category: ')
            # treats
            if category.lower() == 'a':
                print('\n' + ' ' * 5 + f'Available categories:\n'
                                f'A) Cream\n'
                                f'B) Pieces\n'
                                f'C) Exit')
                category = input('Choose a category: ')
                # cream
                if category.lower() == 'a':
                    section_url = '%D8%AA%D8%B1%D9%8A%D8%AA-%D9%83%D8%B1%D9%8A%D9%85%D9%8A'
                    file_name = 'Cat-Treats & Supplements-Treats-Cream'
                # pieces
                elif category.lower() == 'b':
                    section_url = '%D9%85%D9%83%D8%A7%D9%81%D8%A7%D8%AA-%D8%B9%D8%B5%D9%8A'
                    file_name = 'Cat-Treats & Supplements-Treats-Pieces'
                # exit
                elif category.lower() == 'c':
                    quit()
                else:
                    print('Invalid!')
            #     supplements
            elif category.lower() == 'b':
                print('\n' + ' ' * 5 + f'Available categories:\n'
                                f'A) Liquid\n'
                                f'B) Squeezed\n'
                                f'C) Tablets\n'
                                f'D) Exit')
                category = input('Choose a category: ')
                # liquid
                if category.lower() == 'a':
                    section_url = '%D9%85%D9%83%D9%85%D9%84%D8%A7%D8%AA-%D9%82%D8%B7%D8%B7-%D8%B3%D8%A7%D8%A6%D9%84%D8%A9'
                    file_name = 'Cat-Treats & Supplements-Supplements-Liquid'
                # squeezed
                elif category.lower() == 'b':
                    section_url = '%D9%85%D9%83%D9%85%D9%84%D8%A7%D8%AA-%D9%82%D8%B7%D8%B7-%D8%B9%D8%B5%D8%A7%D8%B1'
                    file_name = 'Cat-Treats & Supplements-Supplements-Squeezed'
                #     tablets
                elif category.lower() == 'c':
                    section_url = '%D9%85%D9%83%D9%85%D9%84%D8%A7%D8%AA-%D9%82%D8%B7%D8%B7-%D8%A7%D9%82%D8%B1%D8%A7%D8%B5'
                    file_name = 'Cat-Treats & Supplements-Supplements-Tablets'
                # exit
                elif category.lower() == 'd':
                    quit()
                else:
                    print('Invalid!')
            #     exit
            elif category.lower() == 'c':
                quit()
            else:
                print('Invalid!')
        # sand
        elif category.lower() == 'g':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                            f'A) Basins\n'
                            f'B) Brushes\n'
                            f'C) Freshners\n'
                            f'D) Sand\n'
                            f'E) Scoops and Waste Bags\n'
                            f'F) Exit')
            category = input('Choose a category: ')
            # Basins
            if category.lower() == 'a':
                print('\n' + ' ' * 5 + f'Available categories:\n'
                                f'A) Closed Litter Boxes\n'
                                f'B) Opened Litter Boxes\n'
                                f'C) Litter box with filter\n'
                                f'D) Exit')
                category = input('Choose a category: ')
                # closed
                if category.lower() == 'a':
                    section_url = '%D9%84%D9%8A%D8%AA%D8%B1-%D8%A8%D9%88%D9%83%D8%B3-%D9%82%D8%B7%D8%B7-%D9%85%D8%BA%D9%84%D9%82'
                    file_name = 'Cat-Sand & its Accessories-Basins-Closed'
                # opened
                elif category.lower() == 'b':
                    section_url = '%D9%84%D9%8A%D8%AA%D8%B1-%D8%A8%D9%88%D9%83%D8%B3-%D9%82%D8%B7%D8%B7-%D9%85%D9%81%D8%AA%D9%88%D8%AD'
                    file_name = 'Cat-Sand & its Accessories-Basins-Opened'
                # filter
                elif category.lower() == 'c':
                    section_url = '%D9%84%D9%8A%D8%AA%D8%B1-%D8%A8%D9%88%D9%83%D8%B3-%D9%82%D8%B7%D8%B7-%D8%A8%D9%81%D9%84%D8%AA%D8%B1'
                    file_name = 'Cat-Sand & its Accessories-Basins-Filter'
                #     exit
                elif category.lower() == 'd':
                    quit()
                else:
                    print('Invalid!')
            #     Brushes
            elif category.lower() == 'b':
                section_url = '%D9%81%D8%B1%D8%B4%D8%A7%D8%AA-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Sand & its Accessories-Brushes'
            #     Freshners
            elif category.lower() == 'c':
                section_url = '%D9%85%D8%B9%D8%B7%D8%B1%D8%A7%D8%AA-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Sand & its Accessories-Freshners'
            # Sand
            elif category.lower() == 'd':
                print('\n' + ' ' * 5 + f'Available categories:\n'
                               f'A) Sand Substitute\n'
                               f'B) With a Scent\n'
                               f'C) Without a Scent\n'
                               f'D) Exit\n')
                category = input('Choose a category: ')
                # substitute
                if category.lower() == 'a':
                    section_url = '%D8%A8%D8%AF%D9%8A%D9%84-%D8%A7%D9%84%D8%B1%D9%85%D9%84'
                    file_name = 'Cat-Sand & its Accessories-Sand-Sand substitute'
                #     with scent
                elif category.lower() == 'b':
                    section_url = '%D8%B1%D9%85%D9%84-%D8%A8%D8%B1%D8%A7%D8%A6%D8%AD%D8%A9'
                    file_name = 'Cat-Sand & its Accessories-Sand-with Scent'
                #     without scent
                elif category.lower() == 'c':
                    section_url = '%D8%B1%D9%85%D9%84-%D8%BA%D9%8A%D8%B1-%D9%85%D8%B9%D8%B7%D8%B1'
                    file_name = 'Cat-Sand & its Accessories-Sand-without Scent'
                #     exit
                elif category.lower() == 'd':
                    quit()
                else:
                    print('Invalid!')
            # waste bags
            elif category.lower() == 'e':
                section_url = '%D8%A3%D9%83%D9%8A%D8%A7%D8%B3-%D9%81%D8%B6%D9%84%D8%A7%D8%AA-%D8%A7%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Sand & its Accessories-Waste Bags'
            # exit
            elif category.lower() == 'f':
                quit()
            else:
                print('Invalid!')
        # toys
        elif category.lower() == 'h':
            section_url = '%D8%A3%D9%84%D8%B9%D8%A7%D8%A8-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
            file_name = 'Cat-Toys'
        # training
        elif category.lower() == 'i':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                                   f'A) Cat Nip\n'
                                   f'B) Cleaning\n'
                                   f'C) Training\n'
                                   f'D) Exit')
            category = input('Choose a category: ')
            # catnip
            if category.lower() == 'a':
                section_url = '%D9%83%D8%A7%D8%AA%D9%86%D9%8A%D8%A8-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Training & Cleaning-Cat Nip'
            #     clean
            elif category.lower() == 'b':
                section_url = '%D8%AA%D9%86%D8%B8%D9%8A%D9%81-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Training & Cleaning-Cleaning'
            #     training
            elif category.lower() == 'c':
                section_url = '%D8%AA%D8%AF%D8%B1%D9%8A%D8%A8-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
                file_name = 'Cat-Training & Cleaning-Training'
            #     exit
            elif category.lower() == 'd':
                quit()
            else:
                print('Invalid!')
        # scrapers
        elif category.lower() == 'j':
            section_url = '%D8%AE%D8%AF%D8%A7%D8%B4%D8%A7%D8%AA-%D9%84%D9%84%D9%82%D8%B7%D8%B7'
            file_name = 'Cat-Scrapers'
        # back
        elif category.lower() == 'k':
            menu()
        # exit
        elif category.lower() == 'l':
            quit()
        else:
            print('Invalid!')
    # dogs
    elif animal.lower() == 'dogs':
        print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                        f'A) Accessories\n'
                        f'B) Beds & Carriers\n'
                        f'C) Food\n'
                        f'D) Food Supplies\n'
                        f'E) Health & Beauty\n'
                        f'F) Treats & Supplements\n'
                        f'G) Toys\n'
                        f'H) Training and Cleaning\n'
                        f'I) Back\n'
                        f'J) Quit')
        category = input('Choose a category: ').lower()
        # accessories
        if category.lower() == 'a':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                                   f'A) Clothes\n'
                                   f'B) Collars\n'
                                   f'C) Leahses\n'
                                   f'D) Necklaces\n'
                                   f'E) Waistcoats\n'
                                   f'F) Back\n'
                                   f'G) Exit')
            category = input('Choose a category: ')
            # clothes
            if category.lower() == 'a':
                section_url = '%D9%85%D9%84%D8%A7%D8%A8%D8%B3-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Accessories-Clothes'
                #     collars
            elif category.lower() == 'b':
                section_url = '%D8%A3%D8%B7%D9%88%D8%A7%D9%82-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Accessories-Collars'
            # leashes
            elif category.lower() == 'c':
                section_url = '%D9%85%D8%B4%D8%AF%D8%A7%D8%AA-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Accessories-Leashes'
            # necklaces
            elif category.lower() == 'd':
                section_url = '%D9%82%D9%84%D8%A7%D8%A6%D8%AF-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Accessories-Necklaces'
            # waistcoats
            elif category.lower() == 'e':
                section_url = '%D8%B5%D8%AF%D8%B1%D9%8A%D8%A7%D8%AA-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Accessories-Waistcoats'
            # back
            elif category.lower() == 'f':
                menu()
            # exit
            elif category.lower() == 'g':
                quit()
            else:
                print('Invalid!')
        #     beds
        elif category.lower() == 'b':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                            f'A) Beds\n'
                            f'B) Carriers\n'
                            f'C) Huts\n'
                            f'D) Back\n'
                            f'E) Exit')
            category = input('Choose a category: ')
            # beds
            if category.lower() == 'a':
                print('\n' + ' ' * 5 + f'Available categories:\n'
                                'A) Closed\n'
                                'B) Opened\n'
                                'C) Exit')
                category = input('Choose a category: ')
                # closed
                if category.lower() == 'a':
                    section_url = '%D8%A7%D8%B3%D8%B1%D9%87-%D9%83%D9%84%D8%A7%D8%A8-%D9%85%D8%BA%D9%84%D9%82%D8%A9'
                    file_name = 'Dogs-Beds & Carriers-Beds-Closed'
                # opened
                elif category.lower() == 'b':
                    section_url = '%D8%A7%D8%B3%D8%B1%D9%87-%D9%83%D9%84%D8%A7%D8%A8-%D9%88%D8%B3%D8%A7%D8%AF%D9%87'
                    file_name = 'Dogs-Beds & Carriers-Beds-Opened'
                # exit
                elif category.lower() == 'c':
                    quit()
                else:
                    print('Invalid!')
            #     carriers
            elif category.lower() == 'b':
                print('\n' + ' ' * 5 + f'Available categories:\n'
                                'A) Bag\n'
                                'B) Box\n'
                                'C) Exit')
                category = input('Choose a category: ')
                # bag
                if category.lower() == 'a':
                    section_url = '%D9%86%D9%88%D8%A7%D9%82%D9%84-%D8%B4%D9%86%D8%B7-%D9%83%D9%84%D8%A7%D8%A8'
                    file_name = 'Dogs-Beds & Carriers-Carriers-Bags'
                # box
                elif category.lower() == 'b':
                    section_url = '%D9%86%D9%88%D8%A7%D9%82%D9%84-%D8%B5%D9%86%D8%A7%D8%AF%D9%8A%D9%82-%D9%83%D9%84%D8%A7%D8%A8'
                    file_name = 'Dogs-Beds & Carriers-Carriers-Box'
                # exit
                elif category.lower() == 'c':
                    quit()
                else:
                    print('Invalid!')
            # huts
            elif category.lower() == 'c':
                section_url = '%D8%A8%D9%8A%D9%88%D8%AA-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Beds & Carriers-Huts'
            # back
            elif category.lower() == 'd':
                menu()
            # exit
            elif category.lower() == 'e':
                quit()
            else:
                print('Invalid!')
        #     food
        elif category.lower() == 'c':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                            'A) Dry\n'
                            'B) Wet\n'
                            'C) Exit')
            category = input('Choose a category: ')
            # Dry
            if category.lower() == 'a':
                print('\n' + ' ' * 5 + f'Available categories:\n'
                                'A) Adult\n'
                                'B) Puppy\n'
                                'C) Old\n'
                                'D) Exit')
                category = input('Choose a category: ')
                # adult
                if category.lower() == 'a':
                    section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%AC%D8%A7%D9%81-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8-%D8%A7%D9%84%D8%A8%D8%A7%D9%84%D8%BA%D9%87'
                    file_name = 'Dogs-Food-Dry-Adult'
                # puppy
                elif category.lower() == 'b':
                    section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%AC%D8%A7%D9%81-%D9%84%D9%84%D8%AC%D8%B1%D8%A7%D8%A1'
                    file_name = 'Dogs-Food-Dry-Puppy'
                # old
                elif category.lower() == 'c':
                    section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%AC%D8%A7%D9%81-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8-%D8%A7%D9%84%D9%85%D8%B3%D9%86%D9%87'
                    file_name = 'Dogs-Food-Dry-Old'
                #     exit
                elif category.lower() == 'd':
                    quit()
                else:
                    print('Invalid!')
            # Wet
            elif category.lower() == 'b':
                print('\n' + ' ' * 5 + f'Available categories:\n'
                                'A) Cans\n'
                                'B) Satches\n'
                                'C) Soup\n'
                                'D) Exit')
                category = input('Choose a category: ')
                # cans
                if category.lower() == 'a':
                    section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B1%D8%B7%D8%A8-%D9%83%D9%84%D8%A7%D8%A8-%D9%85%D8%B9%D9%84%D8%A8%D8%A7%D8%AA'
                    file_name = 'Dogs-Food-Wet-Cans'
                # staches
                elif category.lower() == 'b':
                    section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%AC%D8%A7%D9%81-%D9%83%D9%84%D8%A7%D8%A8-%D8%A7%D8%B8%D8%B1%D9%81'
                    file_name = 'Dogs-Food-Wet-Satches'
                # soup
                elif category.lower() == 'c':
                    section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B1%D8%B7%D8%A8-%D9%83%D9%84%D8%A7%D8%A8-%D8%A7%D8%B7%D8%A8%D8%A7%D9%82'
                    file_name = 'Dogs-Food-Wet-Soup'
                #     exit
                elif category.lower() == 'd':
                    quit()
                else:
                    print('Invalid!')
            # exit
            elif category.lower() == 'c':
                quit()
            else:
                print('Invalid!')
        #     food supplies
        elif category.lower() == 'd':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                            f'A) Food Containers\n'
                            f'B) PLates\n'
                            f'C) Exit')
            category = input('Choose a category: ')
            # container
            if category.lower() == 'a':
                section_url = '%D8%AD%D8%A7%D9%81%D8%B8%D8%A7%D8%AA-%D8%B7%D8%B9%D8%A7%D9%85-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Food Supplies-Container'
            #     plates
            elif category.lower() == 'b':
                section_url = '%D8%A7%D8%B7%D8%A8%D8%A7%D9%82-%D8%A7%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Food Supplies-Plates'
            #     exit
            elif category.lower() == 'c':
                quit()
            else:
                print('Invalid!')
        #     health and beauty
        elif category.lower() == 'e':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                            f'A) Hair & Claw care\n'
                            f'B) Health Care\n'
                            f'C) Shampoo & Perfumes\n'
                            f'D) Wet Tissues\n'
                            f'E) Exit')
            category = input('Choose a category: ')
            # claw
            if category.lower() == 'a':
                section_url = '%D8%A7%D9%84%D8%B9%D9%86%D8%A7%D9%8A%D8%A9-%D8%A8%D8%A7%D9%84%D8%B4%D8%B9%D8%B1-%D9%88%D8%A7%D9%84%D9%85%D8%AE%D8%A7%D9%84%D8%A8-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Health & Beauty-Claw & Hair'
            #     Health care
            elif category.lower() == 'b':
                section_url = '%D8%A7%D9%84%D8%B9%D9%86%D8%A7%D9%8A%D8%A9-%D8%A7%D9%84%D8%B5%D8%AD%D9%8A%D8%A9-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Health & Beauty-Health care'
            #     shampoo
            elif category.lower() == 'c':
                section_url = '%D8%A7%D9%84%D8%B4%D8%A7%D9%85%D8%A8%D9%88-%D9%88%D8%A7%D9%84%D8%B9%D8%B7%D9%88%D8%B1-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Health & Beauty-Shampoo'
            #     wet tissue
            elif category.lower() == 'd':
                section_url = '%D9%85%D9%86%D8%A7%D8%AF%D9%8A%D9%84-%D8%B1%D8%B7%D8%A8%D8%A9-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Health & Beauty-Wet Tissue'
            #     exit
            elif category.lower() == 'e':
                quit()
            else:
                print('Invalid!')
        #     treats
        elif category.lower() == 'f':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                            f'A) Treats\n'
                            f'B) Supplements\n'
                            f'C) Exit')
            category = input('Choose a category: ')
            # treats
            if category.lower() == 'a':
                print('\n' + ' ' * 5 + f'Available categories:\n'
                                f'A) Cream\n'
                                f'B) Pieces\n'
                                f'C) Exit')
                category = input('Choose a category: ')
                # cream
                if category.lower() == 'a':
                    section_url = '%D9%85%D9%83%D8%A7%D9%81%D8%A7%D8%AA-%D9%83%D9%84%D8%A7%D8%A8-%D9%83%D8%B1%D9%8A%D9%85%D9%8A'
                    file_name = 'Dogs-Treats & Supplements-Treats-Cream'
                # pieces
                elif category.lower() == 'b':
                    section_url = '%D9%85%D9%83%D8%A7%D9%81%D8%A7%D8%AA-%D9%83%D9%84%D8%A7%D8%A8-%D9%82%D8%B7%D8%B9'
                    file_name = 'Dogs-Treats & Supplements-Treats-Pieces'
                # exit
                elif category.lower() == 'c':
                    quit()
                else:
                    print('Invalid!')
            #     supplements
            elif category.lower() == 'b':
                print('\n' + ' ' * 5 + f'Available categories:\n'
                                f'A) Liquid\n'
                                f'B) Squeezed\n'
                                f'C) Tablets\n'
                                f'D) Exit')
                category = input('Choose a category: ')
                # liquid
                if category.lower() == 'a':
                    section_url = '%D9%85%D9%83%D9%85%D9%84%D8%A7%D8%AA-%D9%83%D9%84%D8%A7%D8%A8-%D8%B3%D8%A7%D8%A6%D9%84%D8%A9'
                    file_name = 'Dogs-Treats & Supplements-Supplements-Liquid'
                # squeezed
                elif category.lower() == 'b':
                    section_url = '%D9%85%D9%83%D9%85%D9%84%D8%A7%D8%AA-%D9%83%D9%84%D8%A7%D8%A8-%D8%B9%D8%B5%D8%A7%D8%B1'
                    file_name = 'Dogs-Treats & Supplements-Supplements-Squeezed'
                #     tablets
                elif category.lower() == 'c':
                    section_url = '%D9%85%D9%83%D9%85%D9%84%D8%A7%D8%AA-%D9%83%D9%84%D8%A7%D8%A8-%D8%A7%D9%82%D8%B1%D8%A7%D8%B5'
                    file_name = 'Dogs-Treats & Supplements-Supplements-Tablets'
                # exit
                elif category.lower() == 'd':
                    quit()
                else:
                    print('Invalid!')
            #     exit
            elif category.lower() == 'c':
                quit()
            else:
                print('Invalid!')
        #     toys
        elif category.lower() == 'g':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                            f'A) Biter\n'
                            f'B) Dolls\n'
                            f'C) Ropes\n'
                            f'D) Exit')
            category = input('Choose a category: ')
            # biter
            if category == 'a':
                section_url = '%D8%A7%D9%84%D8%B9%D8%A7%D8%A8-%D8%B9%D8%B6%D8%A7%D8%B6%D9%87-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Toys-Biter'
            #     Dolls
            elif category == 'b':
                section_url = '%D8%A7%D9%84%D8%B9%D8%A7%D8%A8-%D8%AF%D9%85%D9%89-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Toys-Dolls'
            #     ropes
            elif category == 'c':
                section_url = '%D8%A7%D9%84%D8%B9%D8%A7%D8%A8-%D8%AD%D8%A8%D9%84-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Toys-Ropes'
            #     exit
            elif category == 'd':
                quit()
            else:
                print('Invalid!')
        #     training
        elif category.lower() == 'h':
            print('\n' + ' ' * 5 + f'Available categories:\n'
                                   f'A) Matresses and Matress holder\n'
                                   f'B) Cleaning\n'
                                   f'C) Training\n'
                                   f'D) Exit')
            category = input('Choose a category: ')
            # matress
            if category.lower() == 'a':
                print('\n' + ' ' * 5 + f'Available categories:\n'
                                   f'A) Diapers\n'
                                   f'B) Matresses\n'
                                   f'C) Exit')
                category = input('Choose a category: ')
                # diapers
                if category == 'a':
                    section_url = '%D8%AD%D9%81%D8%A7%D8%B8%D8%A7%D8%AA-%D9%83%D9%84%D8%A7%D8%A8'
                    file_name = 'Dogs-Training & Cleaning-Matresses-Diapers'
                #     matress
                elif category == 'b':
                    section_url = '%D9%85%D9%81%D8%A7%D8%B1%D8%B4-%D9%83%D9%84%D8%A7%D8%A8'
                    file_name = 'Dogs-Training & Cleaning-Matresses-Matresses'
                #     exit
                elif category == 'c':
                    quit()
                else:
                    print('Invalid!')
            #     clean
            elif category.lower() == 'b':
                section_url = '%D8%AA%D9%86%D8%B8%D9%8A%D9%81-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Training & Cleaning-Cleaning'
            #     training
            elif category.lower() == 'c':
                section_url = '%D8%AA%D8%AF%D8%B1%D9%8A%D8%A8-%D9%84%D9%84%D9%83%D9%84%D8%A7%D8%A8'
                file_name = 'Dogs-Training & Cleaning-Training'
            #     exit
            elif category.lower() == 'd':
                quit()
            else:
                print('Invalid!')
        #     back
        elif category.lower() == 'i':
            menu()
        #     exit
        elif category.lower() == 'j':
            quit()
        else:
            print('Invalid!')
    # birds
    elif animal.lower() == 'birds':
        print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                        f'A) Cages & Accessories\n'
                        f'B) Food\n'
                        f'C) Health & Care\n'
                        f'D) Toys\n'
                        f'E) Back\n'
                        f'F) Quit')
        category = input('Choose a category: ').lower()
        # cages
        if category.lower() == 'a':
            print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                            f'A) Cages\n'
                            f'B) Foods & Drinks\n'
                            f'C) Branches & Swings\n'
                            f'D) Exit')
            category = input('Choose a category: ').lower()
            # cages
            if category == 'a':
                section_url = '%D8%A3%D9%82%D9%81%D8%A7%D8%B5-%D9%84%D9%84%D8%B7%D9%8A%D9%88%D8%B1'
                file_name = 'Birds-Cages & Accessories-Cages'
            # food
            elif category == 'b':
                section_url = '%D9%85%D8%A3%D9%83%D9%84%D9%8A%D8%A7%D8%AA-%D9%88%D9%85%D8%B4%D8%B1%D8%A8%D9%8A%D8%A7%D8%AA-%D9%84%D9%84%D8%B7%D9%8A%D9%88%D8%B1'
                file_name = 'Birds-Cages & Accessories-Foods & Drinks'
            # branch
            elif category == 'c':
                section_url = '%D8%A7%D8%BA%D8%B5%D8%A7%D9%86-%D9%88-%D8%A7%D8%B1%D8%A7%D8%AC%D9%8A%D8%AD'
                file_name = 'Birds-Cages & Accessories-Branches & Swings'
            # exit
            elif category == 'd':
                quit()
            else:
                print('Invalid!')
        #     food
        elif category.lower() == 'b':
            print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                            f'A) Nutrition\n'
                            f'B) Rewards\n'
                            f'C) Exit')
            category = input('Choose a category: ').lower()
            # nutrition
            if category == 'a':
                print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                                f'A) Small\n'
                                f'B) Medium\n'
                                f'C) Large\n'
                                f'D) Exit')
                category = input('Choose a category: ').lower()
                # small
                if category == 'a':
                    print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                                    f'A) Budgy\n'
                                    f'B) Zebra\n'
                                    f'C) Fisher\n'
                                    f'D) Canary\n'
                                    f'E) Finch\n'
                                    f'F) Exit')
                    category = input('Choose a category: ').lower()
                    # budgy
                    if category == 'a':
                        section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B7%D9%8A%D9%88%D8%B1-%D8%A8%D8%A7%D8%AF%D8%AC%D9%8A'
                        file_name = 'Birds-Food-Nutrition-Small-Budgy'
                    #     zebra
                    elif category == 'b':
                        section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B7%D9%8A%D9%88%D8%B1-%D8%B2%D9%8A%D8%A8%D8%B1%D8%A7'
                        file_name = 'Birds-Food-Nutrition-Small-Zebra'
                    #     fisher
                    elif category == 'c':
                        section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B7%D9%8A%D9%88%D8%B1-%D9%81%D9%8A%D8%B4%D8%B1'
                        file_name = 'Birds-Food-Nutrition-Small-Fisher'
                    #     canary
                    elif category == 'd':
                        section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B7%D9%8A%D9%88%D8%B1-%D9%83%D9%86%D8%A7%D8%B1%D9%8A'
                        file_name = 'Birds-Food-Nutrition-Small-Canary'
                    #     finch
                    elif category == 'e':
                        section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B7%D9%8A%D9%88%D8%B1-%D9%81%D9%8A%D9%86%D8%B4'
                        file_name = 'Birds-Food-Nutrition-Small-Finch'
                    #     exit
                    elif category == 'f':
                        quit()
                    else:
                        print('Invalid!')
                #     medium
                elif category == 'b':
                    print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                                    f'A) Conure\n'
                                    f'B) Cocktail (crown)\n'
                                    f'C) Quacker\n'
                                    f'D) Laurie\n'
                                    f'E) Exit')
                    category = input('Choose a category: ').lower()
                    # conure
                    if category == 'a':
                        section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B7%D9%8A%D9%88%D8%B1-%D9%83%D9%86%D9%8A%D9%88%D8%B1'
                        file_name = 'Birds-Food-Nutrition-Medium-Conure'
                #         cocktail
                    elif category == 'b':
                        section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B7%D9%8A%D9%88%D8%B1-%D9%83%D9%88%D9%83%D8%AA%D9%8A%D9%84-%D9%83%D8%B1%D9%88%D8%A7%D9%86'
                        file_name = 'Birds-Food-Nutrition-Medium-Cocktail'
                #         quacker
                    elif category == 'c':
                        section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B7%D9%8A%D9%88%D8%B1-%D9%83%D9%88%D9%8A%D9%83%D8%B1'
                        file_name = 'Birds-Food-Nutrition-Medium-Quacker'
                #         laurie
                    elif category == 'd':
                        section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B7%D9%8A%D9%88%D8%B1-%D9%84%D9%88%D8%B1%D9%8A'
                        file_name = 'Birds-Food-Nutrition-Medium-Laurie'
                #         exit
                    elif category == 'e':
                        quit()
                    else:
                        print('Invalid!')
                # large
                elif category == 'c':
                    print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                                    f'A) Amazon\n'
                                    f'B) Casco\n'
                                    f'C) Cockatoo\n'
                                    f'D) Macaw\n'
                                    f'E) Exit')
                    category = input('Choose a category: ').lower()
                    # amazon
                    if category == 'a':
                        section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B7%D9%8A%D9%88%D8%B1-%D8%A7%D9%84%D8%A7%D9%85%D8%A7%D8%B2%D9%88%D9%86'
                        file_name = 'Birds-Food-Nutrition-Large-Amazon'
                    #         casco
                    elif category == 'b':
                        section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B7%D9%8A%D9%88%D8%B1-%D9%83%D8%A7%D8%B3%D9%83%D9%88-%D8%A8%D8%A8%D8%BA%D8%A7%D8%A1-%D8%A7%D9%84%D8%A7%D9%81%D8%B1%D9%8A%D9%82%D9%8A'
                        file_name = 'Birds-Food-Nutrition-Large-Casco'
                    #         cockatoo
                    elif category == 'c':
                        section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B7%D9%8A%D9%88%D8%B1-%D9%83%D9%88%D9%83%D8%A7%D8%AA%D9%88'
                        file_name = 'Birds-Food-Nutrition-Large-Cockatoo'
                    #         macaw
                    elif category == 'd':
                        section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%B7%D9%8A%D9%88%D8%B1-%D9%85%D9%83%D8%A7%D9%88'
                        file_name = 'Birds-Food-Nutrition-Large-Macaw'
                    #         exit
                    elif category == 'e':
                        quit()
                    else:
                        print('Invalid!')
                # exit
                elif category == 'd':
                    quit()
                else:
                    print('Invalid!')
            #         rewards
            elif category == 'b':
                print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                                f'A) Pieces\n'
                                f'B) Sticks\n'
                                f'C) Exit')
                category = input('Choose a category: ').lower()
                # pieces
                if category == 'a':
                    section_url = '%D9%85%D9%83%D8%A7%D9%81%D8%A7%D8%AA-%D8%B7%D9%8A%D9%88%D8%B1-%D9%82%D8%B7%D8%B9'
                    file_name = 'Birds-Food-Rewards-Pieces'
                #     sticks
                elif category == 'b':
                    section_url = '%D9%85%D9%83%D8%A7%D9%81%D8%A7%D8%AA-%D8%B7%D9%8A%D9%88%D8%B1-%D8%B9%D8%B5%D9%8A'
                    file_name = 'Birds-Food-Rewards-Sticks'
                #     exit
                elif category == 'c':
                    quit()
                else:
                    print('Invalid!')
            # exit
            elif category == 'c':
                quit()
            else:
                print('Invalid!')
        #     health
        elif category.lower() == 'c':
            print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                            f'A) Vitamins & Supplements\n'
                            f'B) Hygeine & Feather care\n'
                            f'C) Exit')
            category = input('Choose a category: ').lower()
            # vitamin
            if category == 'a':
                print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                                f'A) Powder\n'
                                f'B) Liquid\n'
                                f'C) Stones\n'
                                f'D) Exit')
                category = input('Choose a category: ').lower()
                # powder
                if category == 'a':
                    section_url = '%D9%85%D9%83%D9%85%D9%84%D8%A7%D8%AA-%D8%B7%D9%8A%D9%88%D8%B1-%D8%A8%D9%88%D8%AF%D8%B1%D8%A9'
                    file_name = 'Birds-Health & Care-Vitamins-Powder'
        #             liquid
                elif category == 'b':
                    section_url = '%D9%85%D9%83%D9%85%D9%84%D8%A7%D8%AA-%D8%B7%D9%8A%D9%88%D8%B1-%D8%B3%D8%A7%D8%A6%D9%84%D8%A9'
                    file_name = 'Birds-Health & Care-Vitamins-Liquid'
                #     stones
                elif category == 'c':
                    section_url = '%D9%85%D9%83%D9%85%D9%84%D8%A7%D8%AA-%D8%B7%D9%8A%D9%88%D8%B1-%D8%A7%D8%AD%D8%AC%D8%A7%D8%B1'
                    file_name = 'Birds-Health & Care-Vitamins-Stones'
                #     exit
                elif category == 'd':
                    quit()
                else:
                    print('Invalid!')
        #         feather
            elif category == 'b':
                section_url = '%D8%A7%D9%84%D9%86%D8%B8%D8%A7%D9%81%D8%A9-%D9%88%D8%A7%D9%84%D8%B9%D9%86%D8%A7%D9%8A%D8%A9-%D8%A8%D8%A7%D9%84%D8%B1%D9%8A%D8%B4-%D9%84%D9%84%D8%B7%D9%8A%D9%88%D8%B1'
                file_name = 'Birds-Health & Care-Hyegeine'
        #         exit
            elif category == 'c':
                quit()
            else:
                print('Invalid!')
        #     toys
        elif category.lower() == 'd':
            section_url = '%D8%A7%D9%84%D8%A3%D9%84%D8%B9%D8%A7%D8%A8-%D8%A7%D9%84%D8%B7%D9%8A%D9%88%D8%B1'
            file_name = 'Birds-Toys'
        #     back
        elif category.lower() == 'e':
            menu()
        #     exit
        elif category.lower() == 'f':
            quit()
        else:
            print('Invalid!')
    # reptiles
    elif animal.lower() == 'reptiles':
        print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                        f'A) Food\n'
                        f'B) Health & Care\n'
                        f'C) Basins \n'
                        f'D) Back\n'
                        f'E) Quit')
        category = input('Choose a category: ')
        # food
        if category.lower() == 'a':
            section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D8%A7%D9%84%D8%B2%D9%88%D8%A7%D8%AD%D9%81'
            file_name = 'Reptiles-Food'
        #     health
        elif category.lower() == 'b':
            section_url = '%D8%A7%D9%84%D8%B5%D8%AD%D8%A9-%D9%88%D8%A7%D9%84%D8%B1%D8%B9%D8%A7%D9%8A%D8%A9-%D8%A7%D9%84%D8%B2%D9%88%D8%A7%D8%AD%D9%81'
            file_name = 'Reptiles-Health & Care'
        #     basin
        elif category.lower() == 'c':
            section_url = '%D8%A7%D9%84%D8%A3%D8%AD%D9%88%D8%A7%D8%B6-%D9%88%D9%85%D8%B3%D8%AA%D9%84%D8%B2%D9%85%D8%A7%D8%AA%D9%87%D8%A7-%D8%A7%D9%84%D8%B2%D9%88%D8%A7%D8%AD%D9%81'
            file_name = 'Reptiles-Basins'
        #     back
        elif category.lower() == 'd':
            menu()
            #     quit
        elif category.lower() == 'e':
            quit()
        else:
            print('Invalid!')
    # small pets
    elif animal.lower() == 'small pets':
        print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                        f'A) Food\n'
                        f'B) Health & Care\n'
                        f'C) Cages & Accessories\n'
                        f'D) Toys\n'
                        f'E) Back\n'
                        f'F) Quit')
        category = input('Choose a category: ').lower()
        # food
        if category.lower() == 'a':
            print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                            f'A) Food\n'
                            f'B) Treats\n'
                            f'C) Exit')
            category = input('Choose a category: ').lower()
            # food
            if category == 'a':
                section_url = '%D8%B7%D8%B9%D8%A7%D9%85-%D9%84%D9%84%D8%AD%D9%8A%D9%88%D8%A7%D9%86%D8%A7%D8%AA-%D8%A7%D9%84%D8%B5%D8%BA%D9%8A%D8%B1%D9%87'
                file_name = 'Small Pets-Food-Food'
            #     treats
            elif category == 'b':
                section_url = '%D9%85%D9%83%D8%A7%D9%81%D8%A2%D8%AA-%D9%84%D9%84%D8%AD%D9%8A%D9%88%D8%A7%D9%86%D8%A7%D8%AA-%D8%A7%D9%84%D8%B5%D8%BA%D9%8A%D8%B1%D9%87'
                file_name = 'Small Pets-Food-Treats'
            #     exit
            elif category == 'c':
                quit()
            else:
                print('Invalid!')
        #     health
        elif category.lower() == 'b':
            print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                            f'A) Vitamins\n'
                            f'B) Hygeine and Fur care\n'
                            f'C) Exit')
            category = input('Choose a category: ').lower()
            # vitamins
            if category == 'a':
                section_url = '%D9%81%D9%8A%D8%AA%D8%A7%D9%85%D9%8A%D9%86%D8%A7%D8%AA-%D9%88-%D9%85%D9%83%D9%85%D9%84%D8%A7%D8%AA-%D9%84%D9%84%D8%AD%D9%8A%D9%88%D8%A7%D9%86%D8%A7%D8%AA-%D8%A7%D9%84%D8%B5%D8%BA%D9%8A%D8%B1%D8%A9'
                file_name = 'Small Pets-Health & Care-Vitamins'
            #     hygeine
            elif category == 'b':
                section_url = '%D8%A7%D9%84%D9%86%D8%B8%D8%A7%D9%81%D8%A9-%D9%88%D8%A7%D9%84%D8%B9%D9%86%D8%A7%D9%8A%D8%A9-%D8%A8%D8%A7%D9%84%D9%81%D8%B1%D9%88-%D9%84%D9%84%D8%AD%D9%8A%D9%88%D8%A7%D9%86%D8%A7%D8%AA-%D8%A7%D9%84%D8%B5%D8%BA%D9%8A%D8%B1%D8%A9'
                file_name = 'Small Pets-Health & Care-Hygeine & Fur care'
            #     exit
            elif category == 'c':
                quit()
            else:
                print('Invalid!')
        #     cages
        elif category.lower() == 'c':
            print('\n' + ' ' * 5 + f'Avaialable {animal} categories:\n'
                            f'A) Cages\n'
                            f'B) Carriers\n'
                            f'C) Huts\n'
                            f'D) Food Containers\n'
                            f'E) Exit')
            category = input('Choose a category: ').lower()
            # cages
            if category == 'a':
                section_url = '%D8%A3%D9%82%D9%81%D8%A7%D8%B5-%D9%84%D9%84%D8%AD%D9%8A%D9%88%D8%A7%D9%86%D8%A7%D8%AA-%D8%A7%D9%84%D8%B5%D8%BA%D9%8A%D8%B1%D8%A9'
                file_name = 'Small Pets-Cages & Accessories-Cages'
            #     carriers
            elif category == 'b':
                section_url = '%D9%86%D9%88%D8%A7%D9%82%D9%84-%D9%84%D9%84%D8%AD%D9%8A%D9%88%D8%A7%D9%86%D8%A7%D8%AA-%D8%A7%D9%84%D8%B5%D8%BA%D9%8A%D8%B1%D8%A9'
                file_name = 'Small Pets-Cages & Accessories-Carriers'
            #     huts
            elif category == 'c':
                section_url = '%D8%A7%D9%83%D9%88%D8%A7%D8%AE-%D9%88%D9%85%D8%AA%D8%A7%D9%87%D8%A7%D8%AA-%D9%84%D9%84%D8%AD%D9%8A%D9%88%D8%A7%D9%86%D8%A7%D8%AA-%D8%A7%D9%84%D8%B5%D8%BA%D9%8A%D8%B1%D9%87'
                file_name = 'Small Pets-Cages & Accessories-Huts'
            #     container
            elif category == 'd':
                section_url = '%D9%85%D8%A3%D9%83%D9%84%D9%8A%D8%A7%D8%AA-%D9%88%D9%85%D8%B4%D8%B1%D8%A8%D9%8A%D8%A7%D8%AA-%D9%84%D9%84%D8%AD%D9%8A%D9%88%D8%A7%D9%86%D8%A7%D8%AA-%D8%A7%D9%84%D8%B5%D8%BA%D9%8A%D8%B1%D8%A9'
                file_name = 'Small Pets-Cages & Accessories-Container'
            #     exit
            elif category == 'e':
                quit()
            else:
                print('Invalid!')
        #     toys
        elif category.lower() == 'd':
            section_url = '%D8%A7%D9%84%D8%A3%D9%84%D8%B9%D8%A7%D8%A8-%D9%84%D9%84%D8%AD%D9%8A%D9%88%D8%A7%D9%86%D8%A7%D8%AA-%D8%A7%D9%84%D8%B5%D8%BA%D9%8A%D8%B1%D9%87'
            file_name = 'Small Pets-Toys'
        #     back
        elif category.lower() == 'e':
            menu()
        #     quit
        elif category.lower() == 'f':
            quit()
        else:
            print('Invalid!')
    return section_url, file_name


# Web Scraping
def scrap(url, category):
    animal_temp = []
    category_temp = []
    products_done = 0
    pages_done = 0
    product_links = []
    animal_products = []
    baseurl = 'https://aleef.com/en/collections/'
    url = baseurl + url
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
        print(f'\rPages done: {pages_done}', end='')
    print('')
    # for every product
    for link in product_links:
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        product_name = (soup.find('h1', class_='productView-title').text.strip())
        product_price_temp = (soup.find('span', class_='price-item').text.strip())
        product_description = (soup.find('div', class_='tab-popup-content').text.strip())
        product_brand = (soup.find('span', class_='productView-info-value').text.strip())
        try:
            product_image = (soup.find('div', class_='media', href = True))['href']
        except:
            product_image = ''
        # price algorithm
        product_price_temp2 = ''
        for j in product_price_temp:
            if j.isdigit() or j == '.':
                product_price_temp2 += j
            if len(product_price_temp2) > 4:
                break
        product_price_temp3 = (product_price_temp2.split('.'))[0] + '.' + product_price_temp2.split('.')[1]
        product_price = (float(product_price_temp3))
        try:
            image_downloader(products_done, product_name, category, product_image, code)
        except:
            pass

        productsss = {
            'Name': product_name,
            'Description': product_description,
            'Brand': product_brand,
            'Price': product_price,
            'Image': product_image
        }
        animal_products.append(productsss)
        products_done += 1
        print(f'\rProducts Done: {products_done}', end='')
    print('')
    return animal_products



# download image
def image_downloader(products_done, product_name, category, product_image, code):
    os.makedirs(rf'{path}\{category}', exist_ok=True)
    # identify the user visiting the website
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    # download picture
    image_name = code + str(products_done) + ' ' + product_name.replace(r"\\", '').replace('\"', '').replace(repr(r"\n"), '').replace('<', '').replace('>', '').replace('?', '').replace('*', '')
    #     download image
    try:
        with open(rf'{path}\{category}\{image_name}.jpg', 'wb') as f:
            im = requests.get(f'https:{product_image}', headers=headers)
            f.write(im.content)
    except:
        with open(rf'{path}\{category}\{code}{products_done}.jpg', 'wb') as f:
            im = requests.get(f'https:{product_image}', headers=headers)
            f.write(im.content)


# Export CSV
def export(data, category):
    df = pd.DataFrame(data)
    df.to_csv(rf'{path}\{category}\{category}.csv', encoding='utf-8-sig')
    print("File Created Succesfully...")
    menu()

path = input('Choose Path: ')
code = input('Please enter Code: ')

menu()
time.sleep(10)