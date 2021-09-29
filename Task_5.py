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
        start=int(input('enter starting point:- '))
        end=int(input('enter last last point:- '))
        for y in range(start,end):
            director=[]
            movie_details={}
            reqst=requests.get(movies_url[y])
            soup=BeautifulSoup(reqst.text,"html.parser")
            div=soup.find('div',class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt")
            ti=div.find('ul',class_="ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt")
            time='o'
            for i in ti:
                time=i.get_text()
            genre=soup.find("span",class_="ipc-chip__text").text
            bio=soup.find('p',class_="GenresAndPlot__Plot-cum89p-6 bUyrda").get_text()
            di=soup.find('div',class_="ipc-metadata-list-item__content-container").a.get_text()
            director.append(di)
            movie_details['Name']=movies_name[y]
            movie_details['Director']=director
            movie_details['Country']='Inida'
            movie_details['Bio']=bio
            movie_details['Runtime']=time
            movie_details['Genre']=genre
            dic=json.dumps(movie_details,indent=2)
            print(dic)
    crape_movie_details()
scrape_top_list()
print('detail of more that one movie that you want in range')