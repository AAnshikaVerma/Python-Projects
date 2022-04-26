import requests
import json
from bs4 import BeautifulSoup
import pprint
from task2 import dec

def group_by_decade(movie):
    
    moviedec={}
    list1=[]
    for i in movie:
        # print(i)
        i=int(i)
        mode=i%10
        # print(mode)
        decade=i-mode
        # print(decade)
        if decade not in list1:
            list1.append(decade)
    # print(list1)
    list1.sort()
    # print(list1)
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        # print(i)
        dec10=i+9
    # print(dec10)
        for x in movie:
            x=int(x)
            # print(x)
            if x<=dec10 and x>=i:
                # print(x)
                x=str(x)
                for v in movie[x]:
                    # print(v)
                    moviedec[i].append(v)
    # return moviedec

    with open("movie_decade3.json","w") as a:

        json.dump(moviedec, a,indent=6)

    return moviedec


group_by_decade(dec)