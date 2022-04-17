"""Obtenha, usando requests ou urllib, o conteúdo sobre as PyLadies no link http://brasil.pyladies.com/about e:
Conte todas as palavras no corpo da página, e indique quais palavras apareceram apenas uma vez.
Conte quantas vezes apareceu a palavra ladies no conteúdo da página"""

import requests
import urllib.request
from bs4 import BeautifulSoup
import sys

url = 'http://brasil.pyladies.com/about'

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

def get_words(soap):
    words = soap.get_text().replace('\n', ' ').lower()
    return words

def get_words_count(html_words):
    total_words = 0
    words = []
    for html_word in html_words.split():
        total_words += 1
        words.append(html_word)
    return total_words, words

def get_ladies_count(words):
    return words.count('ladies')

def main():
    text = get_html(url)
    soap = parse_html(text)
    words = get_words(soap)
    result = get_words_count(words)
    print(f'Total as palavras: {result[1]}')
    print(f'Total de palavras: {result[0]}')
    print(f'Total de palavras únicas: {len(set(result[1]))}')
    print(f'Total vezes que apareceu a palavra ladies: {get_ladies_count(words)}')


if __name__ == "__main__":
    sys.exit(main())