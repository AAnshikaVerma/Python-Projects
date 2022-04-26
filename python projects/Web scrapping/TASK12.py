import requests
import json
from bs4 import BeautifulSoup
import pprint
import os
from task1 import top_movie_list
# cast_list=[]
for i in top_movie_list[:5]:
    url=i['Url']
    # cast_list=[]
    movie_cast_list=[]
    def scrape_movie_cast(url):
        file_name=url[33:]
        # print(file_name)
        file=os.path.exists("movie_cast_"+file_name+".json")
        if file==True:                           
            with open("movie_cast_"+file_name+".json") as f:
                data=json.load(f)
            return data
            # print(data)
        else:
            page=requests.get(url)
            soup=BeautifulSoup(page.text,"html.parser")
            tag=soup.find("div",class_="castSection")
            alltags=tag.find_all('div',class_="cast-item media inlineBlock")
            # print(alltags)
            # dic={}
            for cast in alltags:
                link=cast.find('a',class_='unstyled articleLink')
                link1=link['href']
                # print(link1)
                name=cast.find('span').get_text().strip()
                # print(name)
                dic={}
                dic['link']=link1
                dic['name']=name
                # print(dic)
                movie_cast_list.append(dic)
            with open("movie_cast_"+file_name+".json","w") as f:
                json.dump(movie_cast_list, f,indent=6)
            return cast_list
                # print(movie_cast_list)
    # url=top_movie_list[0]['Url']
    cast_list=scrape_movie_cast(url)
    # cast_list.append(movie_cast_list)
# print(cast_list)