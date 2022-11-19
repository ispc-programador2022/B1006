from bs4 import BeautifulSoup
import requests

website = 'https://unidades-territoriales.obraspublicas.gob.ar/Localities'
result = requests.get(website)
content =result.text

soup= BeautifulSoup(content,'lxml')
print(soup.prettify())


#extraccion codigo  completo de la web