import requests
import json
from bs4 import BeautifulSoup
import pprint
import os
from task1 import top_movie_list
from task4 import scrap_movie_details

url=top_movie_list[0]['Url']

def movie_details(movie_detail):
    # print(movie_detail)
    movie_id=""
    for id in movie_detail[33:]:
            movie_id+=id
    # print(movie_id)
    file_name=movie_id+'.json'
    text=os.path.exists(file_name)
    if text==True:
        with open(file_name,'r') as f:
            a=json.load(f)
            # a=f.read()
        # return a
        print(a)
    else:
        data=scrap_movie_details(url)
        with open(file_name,"w") as f:
           json.dump(data, f,indent=6)
#         #    f.write(a)
#         #    f.close()
        print(data)
movie_details(url)