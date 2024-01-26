import requests
from bs4 import BeautifulSoup

# URL de la page Indeed
url = 'https://fr.indeed.com/jobs?q=data+scientist&l=&from=searchOnHP&vjk=e6e6455063780de5'

# Envoi d'une requête HTTP pour obtenir le contenu de la page
response = requests.get(url)

# Analyse du contenu HTML avec BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Recherche des éléments contenant les informations de salaire
salaires = soup.find_all('div', class_='salary-snippet')

# Extraction et affichage des informations de salaire
for salaire in salaires:
    print(salaire.text.strip())
