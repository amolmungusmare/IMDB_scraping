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
    movies_list=[]
    for i in range(len(movies_year)):
        Top_250={}
        Top_250['Rank']=int(i+1)
        Top_250["Name"]=str(movies_name[i])
        Top_250['URL']=str(movies_url[i])
        Top_250['Year']=movies_year[i][1:5]
        Top_250["Rating"]=float(movies_rating[i])
        movies_list.append(Top_250)
    with open('task_1.json','w') as amol:
        t=json.dump(movies_list,amol,indent=3)
        amol.close()
    print('The data of 250 movies has been saved succesfully!')
scrape_top_list()