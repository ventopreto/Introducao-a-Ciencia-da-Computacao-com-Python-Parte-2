'''Exercício 2: Soma de matrizes
Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz que represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.'''
m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
def soma_matrizes(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m_soma = []
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[0])):
                linha.append(m1[i][j] + m2[i][j])
            m_soma.append(linha)
    else:
        m_soma = False
    return(m_soma)


print(soma_matrizes(m1, m2))
