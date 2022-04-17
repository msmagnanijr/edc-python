import psutil
import platform
import time

# Código 1

# mem = psutil.virtual_memory()
# print(mem.total)

# Código 2

# mem = psutil.virtual_memory()
# capacidade = round(mem.total/(1024*1024*1024), 2)
# print("Capacidade total de MP:", capacidade, "GB")

# Codigo 3

# print(platform.processor())
# print(platform.node())
# print(platform.platform())
# print(platform.system())

# Codigo 4

# psutil.cpu_percent()

# Codigo 5

# for i in range(0, 100):
#     print(psutil.cpu_percent())
#     time.sleep(1)

# Código 6

# disco = psutil.disk_usage('.')

# print("Total:", disco.total, "B")
# print("Em uso:", disco.used, "B")
# print("Livre:", disco.free, "B")

# print("Total:", round(disco.total/(1024*1024*1024), 2), "GB")
# print("Em uso:", round(disco.used/(1024*1024*1024), 2), "GB")
# print("Livre:", round(disco.free/(1024*1024*1024), 2), "GB")

# print("Percentual de disco Usado:", disco.percent, "%")

# Código 7

# dic_interfaces = psutil.net_if_addrs()
# print(dic_interfaces['enp0s20f0u2u1u2'][0].address)