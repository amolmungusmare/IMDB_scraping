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
        m_g={}
        for i in range(len(movies_name)):
            reqst=requests.get(movies_url[i])
            soup=BeautifulSoup(reqst.text,"html.parser")
            genre=soup.find("span",class_="ipc-chip__text").text
            m_g[movies_name[i]]=genre
        by_genre={}
        for j in m_g.values():
            if j not in by_genre:
                by_genre[j]=1
            else:
                by_genre[j]=by_genre[j]+1
        jon=json.dumps(by_genre,indent=3)
        print(jon)
    crape_movie_details()
scrape_top_list()
print('defferentiat by genre....')