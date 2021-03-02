"""
Exercício 1: Lista ordenada
Escreva a função ordenada(lista), que recebe uma lista com números inteiros como parâmetro e devolve o booleano True se a lista estiver ordenada e False se a lista não estiver ordenada.
"""

def ordenada(lista):
    fim = len(lista)
    for i in range(fim-1):
        posiçao_do_minimo = i
        for j in range(i+1, fim):
            if lista[j] < lista[posiçao_do_minimo]:
                print(lista[j], lista[posiçao_do_minimo])
                return False
    return True


