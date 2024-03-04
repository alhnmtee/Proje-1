import requests
import pymongo
from bs4 import BeautifulSoup

#TODO ElasticSearch araştırdım bi hesap açtım güya bir şeyler denedim ama sync aşaması hata verdi tamamlayamadım.Yapamadım


client = pymongo.MongoClient("mongodb+srv://yazlab:yazlab@cluster0.ier7hbc.mongodb.net/")
db = client["yazlab"]
collection = db["kaynak"]


def save_to_mongodb(article_dict):
    # MongoDB'ye kaydet
    collection.insert_one(article_dict)
    #print("Veri MongoDB'ye başarıyla kaydedildi.")

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
        for author in linksoup.find('p', 'article-authors').find_all('a'):
            article_authors.append(author.get_text().strip())

        if article_authors:
            article_dict['authors'] = article_authors
        
        
        article_dict['type'] = linksoup.find('div','kt-portlet__head-label').get_text().strip()
        
        article_dict['date'] = " ".join(linksoup.find('span','article-subtitle').get_text().strip().split())
        
        #article_journal_title = linksoup.find('h1',id='journal-title').get_text().strip()
        article_dict['journal_title'] =linksoup.find('h1',id='journal-title').get_text().strip()
        
        article_keywords = []
        for keyword in linksoup.find('div','article-keywords data-section').find_all('a'):
            article_keywords.append(keyword.get_text().strip())
            article_dict['keywords'] = article_keywords
        
        #article_summary = linksoup.find('div',class_ = 'article-abstract data-section').find('p').get_text().strip()
        #article_dict['summary'] = linksoup.find('div',class_ = 'article-abstract data-section').find('p').get_text().strip()
        article_summary = linksoup.find('div', class_='article-abstract data-section').find_all('p')

        for p_element in article_summary:
            text = p_element.get_text(strip=True)
            if text:
                article_dict['summary'] = text
                break

        if 'summary' not in article_dict:
            article_dict['summary'] = "No summary available"


        #print(article_dict['summary'])

        
      
        
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
        article_dict['url'] = article_url


        
        #print("*** ***" + str(article_dict['summary']))
        save_to_mongodb(article_dict)

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
    
    
    
    

 #Burası test için şu an böyle ama ileride arama yapılacak ve arama sonuçlarından çekilecek    
#search_text = "data"
#dergiParkScraping(search_text,1)


#classı "gs_r gs_or gs_scl" olanlar arama sonuçlarının şeysi
#classı "gs_r" de bunu mu demek istediniz şeyleri var