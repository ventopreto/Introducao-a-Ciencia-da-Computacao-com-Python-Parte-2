"""
Exercício 1: Ordenação com insertion sort
Implemente a função insertion_sort(lista), que recebe uma lista com números inteiros como parâmetro e devolve esta lista ordenada. Utilize o algoritmo insertion sort.
"""
def insertion_sort(seq):
    for i in range(1,len(seq)):
        element = seq[i]
        j = i
        while (j > 0 and seq[j-1] > element):
            seq[j] = seq[j-1]
            j = j - 1
            i += 1
        seq[j] = element
    return seq
