# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:45:24 2020

@author: USER
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def get_movies_info(movie_url): 
    html = requests.get(movie_url)
    sp = BeautifulSoup(html.text,'lxml')
    
    print('='*70)
    print('='*70)
    
    rating = sp.select('strong span')
    print(f'The movie rating is : {rating[0].text}')

    print('\n')

    cast = sp.select('.primary_photo+ td a')
    cast_list = []

    for i in range(len(cast)) :
        cast_list.append(cast[i].text.strip('\n'))
    print(f'cast list : {cast_list}')

    print('\n')

    img = sp.select('.poster img')[0].get('src')
    print(f'url of poster : {img}')
    
    movie_info = {'rating':rating, 'cast':cast, }
    return movie_info
    
def get_movies_url (*args):    
    url = 'https://www.imdb.com/' 
    driver = webdriver.Chrome()
    
    for movie_title in args:
        driver.get(url)
        search_elem = driver.find_element_by_css_selector('#suggestion-search')
        search_elem.send_keys(movie_title)
        
        search_botton_elem = driver.find_element_by_css_selector('#suggestion-search-button')
        search_botton_elem.click()
        
        search_result_elem = driver.find_element_by_css_selector('.odd:nth-child(1) .primary_photo+ .result_text a')
        search_result_elem.click()
        
        current_url = driver.current_url
        movie_info = get_movies_info(current_url)
        
    driver.close()
    
    
    
get_movies_url("Mad Max : Fury Road","1917" )    
