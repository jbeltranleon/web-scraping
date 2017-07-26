import requests
import urllib.request
from bs4 import BeautifulSoup

def main():
	response = requests.get('http://www.xe.com/es/currencyconverter/convert/?Amount=1&From=USD&To=COP')
	soup = BeautifulSoup(response.content, 'html.parser')
	value_container = soup.find('span', 'uccResultAmount')
	value = value_container.contents[0]
	print('El dolar en este momento tiene un valor de: {} COP'.format(value))
	operate(value)

def operate(value):
	value_without_dot = value.replace('.', '')
	value_ready_to_parse = value_without_dot.replace(',', '.')
	value_float = float(value_ready_to_parse)
	print(value_float+1)
	
	

if __name__ == '__main__':
	main()