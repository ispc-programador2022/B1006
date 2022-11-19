from bs4 import BeautifulSoup
import requests

website = 'https://unidades-territoriales.obraspublicas.gob.ar/Localities'
result = requests.get(website)
content =result.text

soup= BeautifulSoup(content,'lxml')

#box = soup.find('div', class_='form-group-sm') #arroja los valores  con la clase 

#box = soup.find('select', id_='filter-province') arroja 'none' como respuesta

#title= soup.find('h3').get_text() arroja el texto none

#box = soup.find('id',class_='filter-province') none como  respuesta

#box = soup.find('select', class_='filter-province') none como respuesta

box = soup.find('div', class_='form-group-sm').get_text()   #este si!!!!

#print(box)

with open('prov.txt','w') as file:
    file.write(box)

