# Faca um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final, mostre qual foi o Maior valor e o menor valor digitado e as suas respectivas
# posicoes na lista.

valores = []

for c in range (0,5):
    valores.append(int(input("Insira um valor: ")))
print(valores)

for c, v in enumerate(valores):
    print(f"Na posicao {c} encontrei o valor {v}!")
maior = max(valores)
menor = min(valores)

print(f"O MAIOR valor digitado foi o {maior} nas posicoes...", end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i}...", end='')
print()
print("-=" * 30)

print(f"O MENOR valor digitado foi o {menor} nas posicoes...", end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i}...", end='')
print()


