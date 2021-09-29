# it will scrap data in depth of every movies with random sleep.......

import requests,random,json
import time as ttime
from bs4 import BeautifulSoup
url='https://www.imdb.com/india/top-rated-indian-movies/'
a=requests.get(url)
b=BeautifulSoup(a.text,"html.parser")
def scrape_top_list():
    lister=b.find('div',class_="lister")
    tboday=lister.find('tbody',class_="lister-list")
    trs=tboday.find_all('tr')
    movies_name,movies_url=[],[]
    for tr in trs:
        c=tr.find('td',class_="titleColumn").get_text()
        title=tr.find('td',class_="titleColumn").a.get_text()
        movies_name.append(title)
        l=tr.find('td',class_="titleColumn").a['href']
        link='https://www.imdb.com/'+l
        movies_url.append(link)
    def crape_movie_details():
        detail={}
        for i in range(len(movies_name)):
            rnom=random.randint(1,3)
            ttime.sleep(rnom)
            director,genre=[],[]
            movie_details={}
            reqst=requests.get(movies_url[i])
            soup=BeautifulSoup(reqst.text,"html.parser")
            div=soup.find('div',class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt")
            ti=div.find('ul',class_="ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt")
            time='o'
            for hg in ti:
                time=hg.get_text()
            genre=soup.find("span",class_="ipc-chip__text").text
            bio=soup.find('p',class_="GenresAndPlot__Plot-cum89p-6 bUyrda").get_text()
            di=soup.find('div',class_="ipc-metadata-list-item__content-container").find('ul')
            for z in di:
                gf=z.get_text()
                director.append(gf)
            movie_details['Name']=movies_name[i]
            movie_details['Director']=director
            movie_details['Country']='India'
            movie_details['Bio']=bio
            movie_details['Runtime']=time
            movie_details['Genre']=genre
            detail[movies_name[i]]=movie_details
        opn=open('Task_9','w')
        json.dump(detail,opn,indent=4)
    crape_movie_details()
scrape_top_list()