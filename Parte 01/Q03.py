def calcular_soma_impares(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 != 0:
            soma += numero
    return soma


with open("numeros.csv", "r") as arquivo:
    conteudo = arquivo.read()

# Separar os números por vírgula e converter cada número em um inteiro
numeros = [int(numero) for numero in conteudo.split(",")]

soma_impares = calcular_soma_impares(numeros)

print("A soma dos números ímpares é:", soma_impares)
