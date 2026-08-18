import numpy as np
import pandas as pd

def definir_h (a, b, n):
    return (b-a)/n

def f(x):
    return np.exp(x)

print("Digite os seguintes valores:\n")
b = int(input("Valor do limite superior: "))
a = int(input("Valor do limite inferior: "))

while True:
    n = int(input("Qual o numero de subintervalos: ")) 
    if(n%2==0): 
        break
    print("O valor deve ser um numero par")

h = definir_h(a, b, n)
print(h)

# Defini intervalos Xi
i = 0
intervalos = []

for i in range(i, n + 1):
    x = a + i * h
    intervalos.append(x)

print(intervalos)


soma_impares = 0
soma_pares = 0


for i in range(1, n, 2):
    soma_impares += f(intervalos[i])


for i in range(2, n-1, 2):
    soma_pares += f(intervalos[i])


integral_aproximada = (h / 3) * (f(intervalos[0]) + 4 * soma_impares + 2 * soma_pares + f(intervalos[n]))

print(f"\nValor aproximado da integral: {integral_aproximada}")


valor_exato = np.exp(1) - 1
erro = abs(valor_exato - integral_aproximada)
print(f"Valor exato (e - 1): {valor_exato}")
print(f"Erro empírico: {erro}")


