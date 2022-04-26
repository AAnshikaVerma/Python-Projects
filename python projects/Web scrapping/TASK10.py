import requests
import json
from bs4 import BeautifulSoup
import pprint
from task5 import movie_list

def analyse_language_and_directors(movie_list):
    # print(movie_list)
    direct_dic={}
    for movie in movie_list:
        director=movie['Director']
        direct_dic[director]={}
        count=0
        for i in range(len(movie_list)):
            if director==movie_list[i]['Director']:
                language=movie_list[i]['Original Language']
                count+=1
                direct_dic[director].update({language:count})
    with open("language_and_directors10.json","w") as f:
        json.dump(direct_dic, f,indent=6)
    print(direct_dic)

analyse_language_and_directors(movie_list)