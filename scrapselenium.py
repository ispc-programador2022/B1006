from selenium import webdriver

website= "https://unidades-territoriales.obraspublicas.gob.ar/Localities"
from selenium.webdriver.chrome.service import Service

s = Service("C://Users\User//Downloads//chromedriver//chromedriver.exe")
driver = webdriver.Chrome(service=s)

