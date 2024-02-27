import requests
from bs4 import BeautifulSoup

# Web sayfasını iste
url = 'https://scrapeme.live/shop'
response = requests.get(url)

# HTML içeriğini al
html_content = response.text

# BeautifulSoup kullanarak HTML içeriğini işle
soup = BeautifulSoup(html_content, 'html.parser')
print (soup.prettify())

# Örneğin, tüm başlıkları (h1 etiketleri) alalım
basliklar = soup.find_all('a')

# Başlıkları ekrana yazdır
for baslik in basliklar:
    print(baslik.text)
