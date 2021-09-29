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
        for i in range(len(movies_name)):
            print(i,':-',movies_name[i])
        inputmivie=int(input('enter which movies number information you want in depth '))
        print('your selected movies is-',movies_name[inputmivie])
        director,genre=[],[]
        movie_details={}
        reqst=requests.get(movies_url[inputmivie])
        soup=BeautifulSoup(reqst.text,"html.parser")
        div=soup.find('div',class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt")
        ti=div.find('ul',class_="ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt")
        time='o'
        for i in ti:
            time=i.get_text()
        gnre=soup.find('div',class_="GenresAndPlot__ContentParent-cum89p-8 bFvaWW Hero__GenresAndPlotContainer-kvkd64-11 twqaW")
        gen=gnre.find('div',class_="ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL")
        for j in gen:
            li=j.get_text()
            genre.append(li)
        bio=soup.find('p',class_="GenresAndPlot__Plot-cum89p-6 bUyrda").get_text()
        di=soup.find('div',class_="ipc-metadata-list-item__content-container").find('ul')
        for i in di:
            gf=i.get_text()
            director.append(gf)
        movie_details['Name']=movies_name[inputmivie]
        movie_details['Director']=director
        movie_details['Country']='India'
        movie_details['Bio']=bio
        movie_details['Runtime']=time
        movie_details['Genre']=genre
        dic=json.dumps(movie_details,indent=3)
        print(dic)
    crape_movie_details()
scrape_top_list()
print('this is detail of movie perticular in depth')