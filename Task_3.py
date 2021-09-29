import requests,json
from bs4 import BeautifulSoup
url='https://www.imdb.com/india/top-rated-indian-movies/'
a=requests.get(url)
b=BeautifulSoup(a.text,"html.parser")
def scrape_top_list():
    lister=b.find('div',class_="lister")
    tboday=lister.find('tbody',class_="lister-list")
    trs=tboday.find_all('tr')
    movies_rank,movies_name,movies_url,movies_rating,movies_year=[],[],[],[],[]
    for tr in trs:
        c=tr.find('td',class_="titleColumn").get_text()
        title=tr.find('td',class_="titleColumn").a.get_text()
        movies_name.append(title)
        yr=tr.find('td',class_="titleColumn").span.get_text()
        movies_year.append(yr)
        rting=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        movies_rating.append(rting)
        l=tr.find('td',class_="titleColumn").a['href']
        link='https://www.imdb.com/'+l
        movies_url.append(link)
    movies_list={}
    for i in range(len(movies_year)):
        Top_250={}
        Top_250['Rank']=int(i+1)
        Top_250["Name"]=str(movies_name[i])
        Top_250['URL']=str(movies_url[i])
        satish=movies_year[i][1:5]
        Top_250['Year']=int(satish)
        Top_250["Rating"]=float(movies_rating[i])
        movies_list[i]=Top_250
    def group_by_decade():
        movies={}
        for j in range(1952,2023,10):
            list=[]
            for i in movies_list.keys():
                if (movies_list[i]["Year"])>=j and (movies_list[i]["Year"])<=j+9 :
                    list.append(movies_list[i])
            movies.update({j:list})
        f=open("Task_3.json","w")
        n=json.dump(movies,f,indent=3)
    group_by_decade()
scrape_top_list()
print('data of 250 movies differentiate by dicade......!')