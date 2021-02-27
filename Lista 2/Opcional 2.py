"""
Exercício 2: Ordem lexicográfica
Como pedido no segundo vídeo da semana, escreva a função primeiro_lex(lista) que recebe uma lista de strings como parâmetro e devolve o primeiro string na ordem lexicográfica. Neste exercício, considere letras maiúsculas e minúsculas.

Dica: revise a segunda vídeo-aula desta semana.
"""

def primeiro_lex(lista):
    primeiro = 1000000000000000
    primeira_letra = ""
    for palavra in lista:
        if ord(palavra[0]) <= primeiro:
            primeiro = ord(palavra[0])
            primeira_letra = palavra
    return primeira_letra

print(primeiro_lex(['maria', 'josé', 'PAULO', 'Catarina']))