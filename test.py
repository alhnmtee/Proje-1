from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()  
driver.get("https://dergipark.org.tr/tr/pub/cbayarfbe/issue/41718/461839")
html_content = driver.page_source
driver.quit()

# BeautifulSoup kullanarak HTML içeriğini işle
soup = BeautifulSoup(html_content, 'html.parser')

# Örneğin, başlık etiketlerini bulalım
titles = soup.find_all('h3')

# Başlıkları ekrana yazdır
for title in titles:
    print(title.text)

# Selenium tarayıcıyı kapat
