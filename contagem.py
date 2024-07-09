import os
import time

cont = int(input("Digite um número Inteiro: "))

while cont >= 0:
    os.system('cls') # limptar o terminal
    print(f'Contagem regressiva: {cont}...')
    time.sleep(1) # atrasa o proximo comando
    cont -= 1

os.system('cls')
print('BOOOOOOMMMMMMMMMMMM!!!!!')