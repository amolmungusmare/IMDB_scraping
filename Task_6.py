import requests,json
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
        movie_details={}
        for y in range(50):
            reqst=requests.get(movies_url[y])
            soup=BeautifulSoup(reqst.text,"html.parser")
            di=soup.find('div',class_="ipc-metadata-list-item__content-container").a.get_text()
            movie_details[movies_name[y]]=di
        analise_director={}
        for i in movie_details.values():
            if i not in analise_director:
                analise_director[i]=1
            else:
                analise_director[i]=analise_director[i]+1
        jsn=json.dumps(analise_director,indent=3)
        print(jsn)
    crape_movie_details()
scrape_top_list()
print('analising of movies by direction')