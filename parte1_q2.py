def verifica_palindromo(palavra):
    palavra = palavra.lower()  
    palavra_invertida = palavra[::-1]  # Inverter a palavra

    if palavra == palavra_invertida:
        return True
    else:
        return False

while True:
    print("\nMenu:")
    print("1. Verificar se uma palavra é um palíndromo")
    print("2. Sair do programa")

    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == "1":
        palavra = input("Digite uma palavra: ")

        if verifica_palindromo(palavra):
            print("Sim, a palavra ", palavra, "é palíndroma.")
        else:
            print("Não, a palavra", palavra, "não é palíndroma.")

    elif opcao == "2":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Digite novamente.\n")
