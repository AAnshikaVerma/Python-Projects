import requests
import json
from bs4 import BeautifulSoup
import pprint
from task5 import movie_list

def analyse_movies_genre(movie_details_list):
    genre_list=[]
    genre_dic={}
    for movie in movie_details_list:
        genre=movie['Genre']
        for i in genre:
            # print(i)
            if i not in genre_list:
                if i!='&':
                    genre_list.append(i)
    # print(genre_list)
    for k in genre_list:
        key=k
        # print(k)
        count=0
        for j in movie_details_list:

            G=j['Genre']  
            # print(G)
            for k1 in G:
                if str(k)==str(k1):
                    count+=1
                    # print(count)
                genre_dic.update(({key:count}))
    print(genre_dic)
    with open("Analyse_movie_genre11.json","w") as f:
        json.dump(genre_dic, f,indent=6)
    return genre_dic
analyse_movies_genre(movie_list)