"""
Exercício 1: Contando vogais ou consoantes
Escreva a função conta_letras(frase, contar="vogais"), que recebe como primeiro parâmetro uma string contendo uma frase e como segundo parâmetro uma outra string. Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função deve devolver o numero de vogais presentes na frase. Quando ele for definido como "consoantes", a função deve devolver o número de consoantes presentes na frase. Se este parâmetro não for passado para a função, deve-se assumir o valor "vogais" para o parâmetro.
"""

def conta_letras(frase, contar="vogais"):
    frase = frase.lower()
    frase = frase
    count = 0
    vogais = "aeiou"
    for letra in frase:
        if contar == "vogais":
            if letra in vogais:
                count += 1
        else:
            if letra not in vogais and letra != " ":
                count += 1
    return count

print(conta_letras('programamos em python', 'vogais'))