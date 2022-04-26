import requests
import json
from bs4 import BeautifulSoup
import pprint
from task5 import movie_list

def analyse_movies_language(movie_details_list):
    Language=[]
    lang_list={}
    for i in movie_details_list:
        if i['Original Language'] not in Language:
            Language.append(i['Original Language'])
    for i in Language:
        key=i
        # print(key)
        count=0
        for j in movie_details_list:

            lang=j['Original Language']  

            if str(i)==str(lang):
                count+=1
                # print(count)
            lang_list.update(({key:count}))
    with open("Analyse_movie_lang6.json","w") as f:
        json.dump(lang_list, f,indent=6)
    return lang_list

analyse_movies_language(movie_list)