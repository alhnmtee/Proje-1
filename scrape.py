import requests
from bs4 import BeautifulSoup

url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=machin+learning&btnG='

response = requests.get(url)



# HTML içeriğini al

html_content = response.text



# BeautifulSoup kullanarak HTML içeriğini işle

soup = BeautifulSoup(html_content, 'html.parser')

print (soup.prettify())

#classı "gs_r gs_or gs_scl" olanlar arama sonuçlarının şeysi
#classı "gs_r" de bunu mu demek istediniz şeyleri var