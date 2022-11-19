from bs4 import BeautifulSoup
import requests

website = 'https://unidades-territoriales.obraspublicas.gob.ar/Localities'
result = requests.get(website)
content =result.text

soup= BeautifulSoup(content,'lxml')
#print(soup.prettify())



box = soup.find('div', class_='panel body')



title = soup.find('div').get_text()



with open(f'{title}.txt','w') as file:
	file.write(title)

