from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.linkedin.com/in/cyro-gabriel").content

soup = BeautifulSoup(site,'html.parser')

#print(soup.prettify())
print(soup.find('Empregos'))









