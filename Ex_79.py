# Crie um programa onde o usuário possa digitar vários
# valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores
# únicos digitados, em ordem crescente.

lista = []
ans = ""

while ans in "Ss":
    n = int(input("Digite um número: "))
    if n not in lista:
        lista.append(n)
    else:
        print("O numero digitado já está na lista e não será adicionado!")
    ans = str(input("Deseja continuar? "))

print("FINALIZADO!")
print(f"Voce digitou os números {lista.sort()}")

