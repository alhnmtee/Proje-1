from bs4 import BeautifulSoup
import requests


url = "https://scholar.google.com/scholar?start="+str(1-1)+"0&q="+"artificiial".replace(' ','+',-1)+"&hl=en&as_sdt=0,5"
headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    "Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}
    
               
response = requests.get(url,headers=headers)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

didyoumean = soup.find_all('div')
for m in didyoumean:   
    print(didyoumean)
