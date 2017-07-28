import requests
import urllib.request
from bs4 import BeautifulSoup

def main():
    try:
        online_values()
    except requests.exceptions.ConnectionError as e:
        offline_values()

def online_values():
    response_one_dollar= requests.get('http://www.xe.com/es/currencyconverter/convert/?Amount=1&From=USD&To=COP')
    soup_one_dollar = BeautifulSoup(response_one_dollar.content, 'html.parser')
    container_dollar = soup_one_dollar.find('span', 'uccResultAmount')
    one_dollar = container_dollar.contents[0]
    print('El dolar en este momento tiene un valor de: ${} COP'.format(one_dollar))
    response_one_cop= requests.get('http://www.xe.com/es/currencyconverter/convert/?Amount=1&From=COP&To=USD')
    soup_one_cop = BeautifulSoup(response_one_cop.content, 'html.parser')
    container_cop = soup_one_cop.find('span', 'uccResultAmount')
    one_cop = container_cop.contents[0]
    one_dollar_without_dot = one_dollar.replace('.', '')
    one_dollar_ready_to_parse = one_dollar_without_dot.replace(',', '.')
    one_dollar_float = float(one_dollar_ready_to_parse)
    one_cop_without_dot = one_cop.replace('.', '')
    one_cop_ready_to_parse = one_cop_without_dot.replace(',', '.')
    one_cop_float = float(one_cop_ready_to_parse)
    operate(one_dollar_float, one_cop_float)

def offline_values():
    one_dollar_float = 1
    one_cop_float = 1
    print('El dolar en este momento tiene un valor de: ${} COP'.format(one_dollar_float))
    operate(one_dollar_float, one_cop_float)

def operate(one_dollar_float, one_cop_float):

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [d]olares a pesos
            [p]esos a dolares
            [s]alir
        '''))
        
        if command == 'd':
            dollar_to_cop(one_dollar_float)
        elif command == 'p':
            cop_to_dollar(one_cop_float)
        else:
            break
    
def dollar_to_cop(one_dollar_float):
    dollar_amount = float(input('Cantidad de dolares: '))
    result = one_dollar_float * dollar_amount
    print('${} Dolares son ${} Pesos Colombianos'.format(dollar_amount, result))

def cop_to_dollar(one_cop_float):
    cop_amount = float(input('Cantidad de pesos: '))
    result = one_cop_float * cop_amount
    print('${} Pesos Colombianos son ${} Dolares'.format(cop_amount, result))
    

if __name__ == '__main__':
    main()