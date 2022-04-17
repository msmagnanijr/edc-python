"""Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv
Obtenha, dentre os jogos do gênero de ação (Action), tiro (Shooter) e plataforma (Platform):
Quais são as três marcas que mais publicaram jogos dos três gêneros combinados? Indique também o total de jogos de cada marca.
Quais são as três marcas que mais venderam os três gêneros combinados? Indique também o total de vendas de cada marca.
Qual é a marca com mais publicações em cada um desses gêneros nos últimos dez anos? Indique também o número total de jogos dela.
Qual foi a marca que mais vendeu em cada um desses gêneros nos últimos dez anos, no Japão? Indique também o total de vendas dela."""

import requests
import sys
import pandas as pd

url = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv'

def get_csv(url):
    response = requests.get(url)
    data = response.text.splitlines()
    return data

def get_top_publishers():

    data = get_csv(url)
    size = len(data)
    sales = []

    for i in range(1, size):
        aux = data[i].split(',')
        sales.append(aux[:])
        aux.clear()

    sales_list_size = len(sales)

    genres = []

    for i in range (0, sales_list_size):
        aux = sales[i]
        if sales[i][3] == 'Action':
            genres.append(aux[:])
        elif sales[i][3] == 'Shooter':
            genres.append(aux[:])
        elif sales[i][3] == 'Platform':
            genres.append(aux[:])
        aux.clear()

    genre_list_size = len(genres)

    for i in range (genre_list_size):
        del(genres[i][10:])

    total=[]

    for i in range (genre_list_size):
        aux=genres[i]
        total.append(aux[4])
        aux.clear()

    publishers = sorted(set(total))

    publisher_count=[]

    for i in range(len(publishers)):
        aux=publishers[i]
        aux_1=total.count(aux)
        publisher_count.append(aux_1)

    return publisher_count, publishers

def pandas_report():

    dataframe = pd.read_csv('https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv')
    dataframe = dataframe[((dataframe["Genre"] == "Action") | (dataframe["Genre"] == "Shooter") | (dataframe["Genre"] == "Platform"))]

    print('Jogos Publicados')
    release = dataframe.groupby('Developer')['Publisher'].count().sort_values(ascending=False)[0:3]
    print(release)

    print('Jogos Vendidos')
    sold = dataframe.groupby('Developer')['Global_Sales'].sum().sort_values(ascending=False)[0:3]
    print(sold)

    print('Jogos Vendidos no Japão nos 10 ultimos anos')

    print('Action')
    action = dataframe[(dataframe["Genre"] == "Action") & (dataframe["Year_of_Release"] >= 2011)]
    japan_action = action.groupby('Developer')['JP_Sales'].sum().sort_values(ascending=False)[0:1]
    print(japan_action)

    print('Shooter')
    shooter = dataframe[(dataframe["Genre"] == "Shooter") & (dataframe["Year_of_Release"] >= 2011)]
    japan_shooter = shooter.groupby('Developer')['JP_Sales'].sum().sort_values(ascending=False)[0:1]
    print(japan_shooter)

    print('Plataforma')
    platform = dataframe[(dataframe["Genre"] == "Platform") & (dataframe["Year_of_Release"] >= 2011)]
    japan_platform = platform.groupby('Developer')['JP_Sales'].sum().sort_values(ascending=False)[0:1]
    print(japan_platform)

def main():
    publisher_count, publishers = get_top_publishers()

    top_publishers = sorted(publisher_count, reverse=True)
    top_publishers =  top_publishers[:3]

    firt_publisher = publisher_count.index(top_publishers[0])
    second_publisher =  publisher_count.index(top_publishers[1])
    third_publisher =  publisher_count.index(top_publishers[2])

    firt_publisher  = publishers[firt_publisher]
    second_publisher = publishers[second_publisher]
    third_publisher = publishers[third_publisher]

    print('\nAs marcas que mais publicaram jogos foram:\n')
    print(f'Primeiro lugar a {firt_publisher} com {top_publishers[0]} jogos publicados')
    print(f'Segundo lugar a {second_publisher} com {top_publishers[1]} jogos publicados')
    print(f'Terceiro lugar a {third_publisher} com {top_publishers[2]} jogos publicados')

    print('\n')

    pandas_report()

if __name__ == "__main__":
    sys.exit(main())