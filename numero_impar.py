"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# Solicita um número inteiro ao usuário
numero = input("Digite um número inteiro: ")

try:
    # Tenta converter a entrada para inteiro
    conversao_inteiro = int(numero)
    # Verifica se o número é par ou ímpar
    if conversao_inteiro % 2 == 0:
        print("O número é Par")
    else:
        print("O número é Ímpar")
except ValueError:
    # Trata a exceção se a conversão falhar
    print("Isso não é um número inteiro. Por favor, tente novamente.")
