import requests
import json
from bs4 import BeautifulSoup
import pprint
from task1 import top_movie_list

url=top_movie_list[0]['Url']
# print(url)
def scrap_movie_details(movie_url):

    page=requests.get(movie_url)
    soup=BeautifulSoup(page.text,"html.parser")
    # print(soup)
    title=soup.find('div',class_="col mob col-center-right col-full-xs mop-main-column")
    # print(title)
    title1=title.find('div',class_="thumbnail-scoreboard-wrap")
    # print(title1)
    poster=title1.find('img',class_="posterImage js-lazyLoad")
    poster1=poster['src']
    # print(poster1)
    name=title1.find("h1",class_="scoreboard__title" ).get_text()
    # print(name)
    s=soup.find('ul',class_="content-meta info")
    # print(s)
    genre=s.find('div',class_='meta-value genre').get_text().split()
    # print(genre)
    sub_tle=s.find_all('li',class_="meta-row clearfix")
    # print(sub_tle)
    movie_d={}

    movie_d['Name']=name
    # key=[]
    # value=[]
    for i in sub_tle:
        k=i.find('div',class_="meta-label subtle").get_text()
        key=k[:-1]
        # print(key)
        value=i.find('div',class_="meta-value").get_text().strip().replace(" ","").replace('\n',"").replace('\u00a0'," ")
        # print(value)
        movie_d[key]=value
    time=int(movie_d["Runtime"][0])*60
    for i in movie_d['Runtime'][2:]:
                if 'm' not in i:
                    time+=int(i)
                else:
                    break
    movie_d["Runtime"]=str(time)+' m'
    movie_d["Poster_image_url"]=poster1
    movie_d["Original Language"]=movie_d["Original Language"].strip().split()
    movie_d["Genre"]=genre
    with open("movie_details4.json","w") as f:
        json.dump(movie_d, f,indent=6)
    return movie_d

scrap=scrap_movie_details(url)