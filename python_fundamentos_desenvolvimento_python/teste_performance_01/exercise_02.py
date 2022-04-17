""" 
2. Faça uma função em Python que receba do usuário a idade de uma pessoa em anos, 
meses e dias e retorne essa idade expressa em dias. Considere que todos os anos têm 365 dias.
"""

import sys
from datetime import datetime

sys.tracebacklimit = 0
now = datetime.now()

fields = [
    {'label': 'Por favor, entre com o ano do seu nascimento, como por exemplo "1988": ', 'value': 0},
    {'label': 'Por favor, entre com o mês do seu nascimento, como por exemplo "06": ', 'value': 0},
    {'label': 'Por favor, entre com o dia do seu nascimento, como por exemplo "23": ', 'value': 0}

]

def validate_year(year):
    try:
        if int(year) >= 1900 and int(year) <= now.year:
            return True
        else:
            raise ValueError
    except ValueError:
        raise ValueError('Ano inválido!')

def validate_month(month):
    try:
        if int(month) >= 1 and int(month) <= 12:
            return True
        else:
            raise ValueError
    except ValueError:
        raise ValueError('Mês inválido')

def validate_day(days):
    try:
        if int(days) >= 1 and int(days) <= 31:
            return True
        else:
            raise ValueError
    except ValueError:
        raise ValueError('Dia inválido')

def number_of_days(year, month, day):
    interval_years  = now.year-year
    interval_months = now.month-month
    interval_days   = now.day-day

    return ((interval_years*365)+(interval_months*30)+interval_days)

def main():
    print('Sua idade em "dia(s)" será calculada baseando-se na data do seu nascimento')
    print("\n")
    for field in fields:
        while True:
            field['value'] = input(f"{field['label']} ") or '0'
            if(not field['value'].replace(',', '').replace('.', '').isnumeric()
                or float(field['value']) <= 0):
                print('O valor informado não é válido!')
            else:
                break

    print("\n")

    if validate_year(fields[0]['value']) and validate_month(fields[1]['value']) and validate_day(fields[2]['value']):
        result = number_of_days(int(fields[0]['value']), int(fields[1]['value']), int(fields[2]['value']))
        print(f'Você possui {result} dia(s) de idade!')
    else:
        print('Ocorreu um erro inesperado!')

if __name__ == "__main__":
    sys.exit(main())