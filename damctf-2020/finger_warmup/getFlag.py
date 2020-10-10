from bs4 import BeautifulSoup
import requests

baseURL = "https://finger-warmup.chals.damctf.xyz/"
code = ""

response = requests.get(baseURL)
soup = BeautifulSoup(response.text, 'html.parser')

link = soup.a
tryAgainText = link.text

while link:
    code = link.get('href')
    response = requests.get(baseURL+code)
    soup = BeautifulSoup(response.text, 'html.parser')
    link = soup.a

print(soup.pre.text)

