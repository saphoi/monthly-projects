import time

print("informe a quantidade de minutos")
minutos = int(input())

print("informe a quantidade de segundos")
segundos = int(input())

i = 0
while i == 0:
    if segundos > 0:
        segundos = segundos - 1
        time.sleep(1)
        print(f'{minutos} minutos, {segundos} segundos', end="\r")
    if minutos > 0 and segundos == 0:
        minutos = minutos - 1
        segundos = segundos + 59
        time.sleep(1)
        print(f'{minutos} minutos, {segundos} segundos', end="\r")
    if minutos == 0 and segundos == 0:
        time.sleep(1)
        print("\nfim")
        i = 1
