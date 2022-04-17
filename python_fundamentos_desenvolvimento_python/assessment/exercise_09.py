"""Obtenha, usando requests ou urllib, a página HTML https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html dentro de seu programa em Python e faça:
Imprima o conteúdo referente apenas à tabela apresentada na página indicada.
Escreva um programa que obtenha do usuário uma sigla do estado da região Centro-Oeste e apresenta suas informações correspondentes na tabela. O resultado deve apresentar
apenas o conteúdo, sem formatação. Ou seja, as tags não devem aparecer. Não esqueça de checar se a sigla pertence à região."""

import requests
import urllib.request
from bs4 import BeautifulSoup
import sys

valid_states =  ['DF', 'GO', 'MT', 'MS']
url = 'https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html'

def get_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return urllib.request.urlopen(url).read().decode('utf-8')
    except Exception as e:
        print(f'Erro ao acessar a url: {url}')
        print(e)
        return None

def parse_html(text):
    soap = BeautifulSoup(text, "html.parser")
    return soap

def get_user_input():
    sigla = input('Digite a sigla de um estado que seja da região centro-oeste: ')
    return sigla.upper()

def print_table(soap):
    for div in soap.find_all('div', class_='tabela'):
        print(div.text)

def print_table_line(soap, sigla):
    for div in soap.find_all('div', class_='linha'):
        if sigla in div.text:
            print(div.text)

def main():
    print_table(parse_html(get_html(url)))
    while True:
        sigla = get_user_input()
        if sigla in valid_states:
            print_table_line(parse_html(get_html(url)), sigla)
            break
        else:
            print('Estado inválido!')
            print('Estados válidos: ', valid_states)

if __name__ == "__main__":
    sys.exit(main())