import requests
import urllib.request
from bs4 import BeautifulSoup

def main():
	for i in range(1, 6):
		response = requests.get('https://xkcd.com/{}'.format(i))
		soup = BeautifulSoup(response.content, 'html.parser')
		image_container = soup.find(id='comic')
		image_url = image_container.find('img')['src']
		image_name = image_url.split('/')[-1]
		print('Descargando la imagen {}'.format(image_name))
		urllib.request.urlretrieve('https:{}'.format(image_url), image_name)

if __name__ == '__main__':
	main()