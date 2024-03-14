from json import dumps
from pyparsing import html_comment
import requests
import pymongo
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch
#TODO ElasticSearch araştırdım bi hesap açtım güya bir şeyler denedim ama sync aşaması hata verdi tamamlayamadım.Yapamadım


client = pymongo.MongoClient("mongodb+srv://yazlab:yazlab@cluster0.ier7hbc.mongodb.net/")
db = client["yazlab"]
collection = db["kaynak"]

es = Elasticsearch('http://localhost:9200')


def save_to_mongodb(article_dict):
    # MongoDB'ye kaydet
    collection.insert_one(article_dict)
    


def googleScholarScraping(search_text,page):
   
    def scrapeInfo(article_soup:BeautifulSoup): 
        print("google article scrapeleniyor")
        article_dict = {}
        pdf_url = article_soup.find('a')['href']
        innerSoup = article_soup.find('div',class_='gs_ri')
        article_url = innerSoup.find('h3','gs_rt').find('a')['href']
        article_title = innerSoup.find('h3','gs_rt').find('a').get_text()
        
        temptext = innerSoup.find('div','gs_a').get_text()
        article_authors = temptext.split('-')[0].strip()
        
        
        article_journal = temptext.split('-')[2].strip()
        if(article_journal.find(',')!=-1):
            article_journal='kaynak  bulunamadı'
        
        
        try:
            article_year = temptext.split('-')[1].split(',')[1].strip()
        except:
            article_year = 'yıl bilgisi alınamadı'
            
        article_summary = innerSoup.find('div','gs_rs').get_text()
        article_cites = innerSoup.find('div','gs_fl gs_flb').find_all('a')[2].get_text().split(' ')[2]
        
        article_dict['authors'] = article_authors
        article_dict['date']=article_year
        article_dict['journal_title'] =article_journal
        article_dict['_id']=article_title
        article_dict['title'] = article_title
        article_dict['cites'] = article_cites
        article_dict['summary'] = article_summary
        article_dict['pdf_url'] = pdf_url
        article_dict['article_url'] = article_url
        
        try:
            print("\ngoogle'dan kaydedildi\n")
            print(article_dict)
            print("\n\n")
            save_to_mongodb(article_dict)
        except:
            print("veritabanına google scholardan kaydedilemedi")
            
    for num in range(0,page):
        url = "https://scholar.google.com/scholar?start="+str(num-1)+"0&q="+search_text.replace(' ','+',-1)+"&hl=en&as_sdt=0,5"           
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        articles = soup.find_all(class_ ="gs_r gs_or gs_scl")
        
        for article in articles:
            scrapeInfo(article)
    
    for document in collection.find():
        document_id = document.pop('_id')  # _id alanını belgeden çıkarın
        es.index(index='your_elasticsearch_index', id=document_id, body=dumps(document))
  
    

def dergiParkScraping(search_text,page):
    def scrapeInfo(link):
        article_dict = {}

        linksoup =  BeautifulSoup(requests.get(link).text, 'html.parser')
        title_element = linksoup.find_all('h3', 'article-title')
        article_title = ""
        for title in title_element:
            if(len(title['aria-label']) > 16): # <h3 class="article-title" aria-label="Makale Başlığı: "> bu şekilde ekstra eleman yüzünden patlıyor "Makale Başlığı: " buu 16 karakter , 
                article_title=title['aria-label'][16:]#16 dan büyük olanı alıyoruz
                article_dict['title'] = article_title
                
        
        #print(article_title.get_text().strip() + link)
     
        #TODO yorum satırlı kısımlar yeniden yazılacak yukarıdaki article_title bulma şekline göre
     
       # if title_element and len(title_element.get_text().strip()) > 2:
          #  article_dict['title'] = title_element.get_text().strip()
        
        #TODO başlık ve özel almayan sayfalardan biri https://dergipark.org.tr/tr/pub/cbayarfbe/issue/41718/461839 neden olmadığını araştırmak gerek
       
        
       # if title_element and len(title_element.get_text().strip()) > 2:
         #   article_dict['title'] = title_element.get_text().strip()

        # Yazarları al
        article_authors = []
        try:
            for author in linksoup.find('p', 'article-authors').find_all('a'):
                article_authors.append(author.get_text().strip())
        except:
            print("Yazar eklemede bir hatayla karşılaşıldı")

        if article_authors:
            article_dict['authors'] = article_authors
        
        
        article_dict['type'] = linksoup.find('div','kt-portlet__head-label').get_text().strip()
        
        article_dict['date'] = " ".join(linksoup.find('span','article-subtitle').get_text().strip().split())
        
        #article_journal_title = linksoup.find('h1',id='journal-title').get_text().strip()
        article_dict['journal_title'] =linksoup.find('h1',id='journal-title').get_text().strip()
        
        article_dict['_id']=linksoup.find('h1',id='journal-title').get_text().strip()
        
        article_keywords = []
        try:
            for keyword in linksoup.find('div','article-keywords data-section').find_all('a'):
                article_keywords.append(keyword.get_text().strip())
                article_dict['keywords'] = article_keywords
        except:
            print("anahtar kelime yok")

        
        #article_summary = linksoup.find('div',class_ = 'article-abstract data-section').find('p').get_text().strip()
        #article_dict['summary'] = linksoup.find('div',class_ = 'article-abstract data-section').find('p').get_text().strip()
        try:
            article_summary = linksoup.find('div', class_='article-abstract data-section').find_all('p')
            for p_element in article_summary:
                text = p_element.get_text(strip=True)
                if text:
                    article_dict['summary'] = text
                    break
        except:
            pass
        

        if 'summary' not in article_dict:
            article_dict['summary'] = "Özet alınamadı"

    

        
      
        
        article_referances = []
        try:
            for referance in linksoup.find('div','article-citations data-section').find_all('li'):
                article_referances.append(referance.get_text().strip())
                article_dict['referances'] = article_referances
        except:
            print("referans yok")
            
        #TODO yayın id ve alıntı sayısı doi numarası filan bunlar nolucak ? ve bunşarı veri tabanına atmak lazım
        #TODO article_citation_count = ??
        
        article_url = 'https://dergipark.org.tr' + linksoup.find('div',id = 'article-toolbar').find('a')['href']
        article_dict['pdf_url'] = article_url
        article_dict['article_url'] = link


        
        #print("*** ***" + str(article_dict['summary']))
        try:
            save_to_mongodb(article_dict)
        except:
            print("Veri kaydedilemedi")
            
    for num in range(1,page+1):
        url = 'https://dergipark.org.tr/tr/search/'+str(num)+'?q='+search_text+'&section=articles'
        response = requests.get(url)
        html_content = response.text


        soup = BeautifulSoup(html_content, 'html.parser')
        titles = soup.find_all(class_  = 'card-title')
        article_links = []
        
        for title in titles:
            article_links.append(title.findChild('a')['href'])

        for link in article_links:
            scrapeInfo(link)
    
        
    
    
    for document in collection.find():
        document_id = document.pop('_id')  # _id alanını belgeden çıkarın
        es.index(index='your_elasticsearch_index', id=document_id, body=dumps(document))
    
    

 #Burası test için şu an böyle ama ileride arama yapılacak ve arama sonuçlarından çekilecek    
#search_text = "data"



#classı "gs_r gs_or gs_scl" olanlar arama sonuçlarının şeysi
#classı "gs_r" de bunu mu demek istediniz şeyleri var