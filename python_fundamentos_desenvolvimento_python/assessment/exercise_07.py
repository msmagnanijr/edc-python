"""Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link: https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv
Dentre os seguintes países nórdicos: Suécia, Dinamarca e Noruega, verifique: No século XXI (a partir de 2001), qual foi o maior medalhista de ouro, considerando apenas as seguintes modalidades:
Curling, Patinação no gelo (skating), Esqui (skiing), Hóquei sobre o gelo (ice hockey)
Para cada esporte, considere todas as modalidades, tanto no masculino quanto no feminino.
Sua resposta deve imprimir um relatório mostrando o total de medalhas de cada um dos países e em que esporte, ano, cidade e gênero (masculino ou feminino) cada medalha foi obtida."""

import requests
import csv
import json
from collections import Counter

url = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv'
sports = ['Curling', 'Skating', 'Skiing', 'Ice Hockey']

def filter_gold_medals_by_country_and_sport_year(medals, country, year):
    gold_medals = []
    for medal in medals:
        if medal['NOC'] == country:
            if medal['Medal'] == 'Gold':
                if medal['Sport'] in sports:
                    if int(medal['Year']) >= int(year):
                        gold_medals.append(medal)
    return gold_medals


def sum_gold_medals_by_country(medals, country, year):
    gold_medals = filter_gold_medals_by_country_and_sport_year(medals, country, year)
    return len(gold_medals)

def get_csv(url):

    response = requests.get(url)
    reader = csv.DictReader(response.text.splitlines())
    medals = []
    for row in reader:
        medals.append(row)
    return medals

def get_csv_by_line(url):
    response = requests.get(url)
    rows =  [data.split(",") for data in response.text.split("\n")]
    return rows

def olympics_games_report():

    response = requests.Session().get(url)
    lines = [data.split(",") for data in response.text.split("\n")]
    header = lines.pop(0)
    aux = []

    print(header)

    for line in lines:
        aux.append({header[index]: item for index, item in enumerate(line)})

    counter = dict(Counter([item["NOC"] for item in aux]))

    aux_report = {}

    for key in counter.keys():
        aux_report[key] = {}
        aux_report[key]["Total de Medalhas"] = counter[key]

    for key in aux_report.keys():
        aux_report[key]["data"] = []

        for medal in [item for item in aux if item["NOC"] == key]:
            medal_data = {"Pais": medal["NOC"], "Cidade": medal["City"], "Modalidade": medal["Sport"], "Ano": medal["Year"], "Genero": "Masculino" if medal["Event gender"] == "M" else "Femenino"}

        aux_report[key]["data"].append(medal_data)
    else:
        for country in aux_report.keys():
            print("\n")
            print('Total de Medalhas: %d' % aux_report[country]['Total de Medalhas'])
            print( 'Pais','|','Cidade','|', 'Modalidade','|', 'Ano','|', 'Genero')
            for medals in aux_report[country]['data']:
                print(medals['Pais'],' ', medals['Cidade'],' ', medals['Modalidade'],' ', medals['Ano'],' ', medals['Genero'])
def main():
    medals = get_csv(url)
    print(f'O maior medalhista de Ouro considerando apenas as modalidades "{" - ".join(sports)}"  é a Noruega com {sum_gold_medals_by_country(medals, "NOR","2001")}  medalhas de ouro.')
    print(f'\nEm segundo colocado considerando apenas as modalidades "{" - ".join(sports)}"  foi a Suécia com {sum_gold_medals_by_country(medals, "SWE", "2001")} medalhas de ouro.' )
    print(f'\nA Dinamarca não ganhou nehuma ({sum_gold_medals_by_country(medals, "DNK","2001")}) medalha de ouro nas modalidades "{" - ".join(sports)}" ')
    olympics_games_report()

if __name__ == '__main__':
    main()