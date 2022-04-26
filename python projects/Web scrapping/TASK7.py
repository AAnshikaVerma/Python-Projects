import requests
import json
from bs4 import BeautifulSoup
import pprint
from task5 import movie_list

def analyse_movies_director(movie_details_list):
    D=[]
    dirct_list={}
    for i in movie_details_list:
        if i['Director'] not in D:
            D.append(i['Director'])
    for i in D:
        key=i
        # print(key)
        count=0
        for j in movie_details_list:

            dirct=j['Director']  

            if str(i)==str(dirct):
                count+=1
                # print(count)
            dirct_list.update(({key:count}))
    with open("Analyse_movie_director7.json","w") as f:
        json.dump(dirct_list, f,indent=6)
    return dirct_list

analyse_movies_director(movie_list)