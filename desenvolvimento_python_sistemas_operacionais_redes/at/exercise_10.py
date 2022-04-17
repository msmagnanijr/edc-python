"""Baseado no exemplo apresentado em aula, onde raspamos dados do finance.yahoo.com(ScrapingPrice), crie um app que obtenha
informações de memória e cpu e data/horário. Armazene os dados(data/horário, memória e cpu) em intervalos de tempo de 5 segundos em em arquivo csv.
Você pode definir uma thread ou outro processo para criar uma segunda funcionalidade na aplicação,
onde você lerá as informações do arquivo csv e imprimirá dois gráficos(memória e cpu) que irá monitorar a evolução dos dados"""

import psutil
import sys
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from cycler import cycler
import matplotlib as mpl
import threading
from matplotlib.animation import FuncAnimation

style.use('seaborn-dark')
#print(style.available)
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
mpl.rcParams['axes.prop_cycle'] = cycler(color=['r', 'g', 'b', 'y'])
fig = plt.figure()

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Monitorando Recursos do Sistema Operacional')

def get_memory_cpu_data_every_5_seconds():
    try:
        while True:
            data = (psutil.cpu_percent(), psutil.virtual_memory().percent)
            write_memory_cpu_data(data)
            time.sleep(5)
    except KeyboardInterrupt:
        sys.exit()

def write_memory_cpu_data(data):
    with open('memory_cpu_data.csv', 'a') as f:
        f.write(f'{time.strftime("%d-%m-%Y %H:%M:%S")},{data[0]},{data[1]}\n')

def write_memory_cpu_data_head():
    with open('memory_cpu_data.csv', 'w') as f:
        f.write('Time,CPU,Memory\n')

def plot_memory_cpu(i):
    data = pd.read_csv('memory_cpu_data.csv')[-5:]

    x_values = data['Time']
    y_values = data['CPU']
    z_values = data['Memory']

    ax1.clear()
    ax1.plot(x_values, y_values, 'tab:orange')
    ax1.set_title('Consumo de CPU', fontsize=12)
    ax1.tick_params(axis="x", labelrotation=15)

    ax2.clear()
    ax2.plot(x_values, z_values, 'tab:green')
    ax2.set_title('Consumo de Memória', fontsize=12)
    ax2.tick_params(axis="x", labelrotation=15)


def main():
    try:
        write_memory_cpu_data_head()
        t = threading.Thread(target=get_memory_cpu_data_every_5_seconds)
        t.start()
        ani = FuncAnimation(plt.gcf(), plot_memory_cpu, 1000)
        plt.tight_layout()
        plt.show()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    sys.exit(main())