"""
Exercício 1: Gerando listas grandes
Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro n e devolve uma lista contendo n números inteiros aleatórios.
"""
from random import randint

def lista_grande(n):
    lista = []
    i = 0
    while i < n:
        lista.append(randint(1,10000))
        i+=1
    return lista

