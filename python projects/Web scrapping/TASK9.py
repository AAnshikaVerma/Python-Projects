import requests
import json
from bs4 import BeautifulSoup
import pprint
import os
import random,time
from task1 import top_movie_list
from task4 import scrap_movie_details

# url=top_movie_list[0]['Url']
for i in top_movie_list[:10]:
    url=i['Url']
    def movie_details(movie_detail):
        # print(movie_detail)
        random_sleep=random.randint(1,3)
        movie_id=""
        for id in movie_detail[33:]:
                movie_id+=id
                # print(movie_id)
        file_name="/home/alka/Desktop/WEB_SCRAPING/"+movie_id+'.json'
        text=os.path.exists(file_name)
        if text==True:
            with open(file_name,'r') as f:
                a=json.load(f)
                # a=f.read()
            # return a
            print(a)
        else:
            time.sleep(random_sleep)
            data=scrap_movie_details(url)
            with open(file_name,"w") as f:
                json.dump(data, f,indent=6)
    #         #    f.write(a)
    #         #    f.close()
            print(data)
    movie_details(url)