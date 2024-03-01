import requests
import pymongo
from bs4 import BeautifulSoup


#client = pymongo.MongoClient("mongodb+srv://yazlab:yazlab@cluster0.ier7hbc.mongodb.net/")
#db = client["yazlab"]
#collection = db["kaynak"]

def dergiParkScraping(search_text,page):
    def scrapeInfo(link):
        linksoup =  BeautifulSoup(requests.get(link).text, 'html.parser')
        article_title = linksoup.find('h3','article-title').get_text().strip()
        
        article_authors = []
        for author in linksoup.find('p','article-authors').find_all('a'):
            article_authors.append(author.get_text().strip())
        
        article_type = linksoup.find('div','kt-portlet__head-label').get_text().strip()
        
        article_date = " ".join(linksoup.find('span','article-subtitle').get_text().strip().split())
        
        article_journal_title = linksoup.find('h1',id='journal-title').get_text().strip()
        
        article_keywords = []
        for keyword in linksoup.find('div','article-keywords data-section').find_all('a'):
            article_keywords.append(keyword.get_text().strip())
        
        article_summary = linksoup.find('div',class_ = 'article-abstract data-section').find('p').get_text().strip()
        
        article_referances = []
        for referance in linksoup.find('div','article-citations data-section').find_all('li'):
            article_referances.append(referance.get_text().strip())
        
        #TODO yayın id ve alıntı sayısı doi numarası filan bunlar nolucak ? ve bunşarı veri tabanına atmak lazım
        #article_citation_count = ??
        
        article_url = 'https://dergipark.org.tr' + linksoup.find('div',id = 'article-toolbar').find('a')['href']
        


    url = 'https://dergipark.org.tr/tr/search/'+str(page)+'?q='+search_text+'&section=articles'
    response = requests.get(url)
    html_content = response.text


    soup = BeautifulSoup(html_content, 'html.parser')
    titles = soup.find_all(class_  = 'card-title')
    article_links = []
    
    for title in titles:
        article_links.append(title.findChild('a')['href'])

    for link in article_links:
        scrapeInfo(link)
    
    
    
    
    
        
search_text = 'prostate'
dergiParkScraping(search_text,1)


#classı "gs_r gs_or gs_scl" olanlar arama sonuçlarının şeysi
#classı "gs_r" de bunu mu demek istediniz şeyleri var

