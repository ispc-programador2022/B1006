from bs4 import BeautifulSoup
import requests

website = 'https://unidades-territoriales.obraspublicas.gob.ar/Localities'
result = requests.get(website)
content =result.text

soup= BeautifulSoup(content,'lxml')



#box = soup.find('div', class_='form-group-sm').get_text()   #este si!!!!
#box =soup.find('id',class_='DataTables_Table_0').get_text() error
#box =soup.find('table',ID_='DataTables_Table_0').get_text()
#box =soup.find(id='DataTables_Table_0').get_text() 
#box =soup.find('td','class_sorting').get_text()


box = soup.find('div', class_='panel-body').get_text()  


#ciudades= soup.find('tbody').get_text() 

print(box)


#with open('prov.txt','w') as file: bajar   para imprimir  file.write(box)

