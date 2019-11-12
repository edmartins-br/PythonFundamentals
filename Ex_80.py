# Exercício Python 080: Crie um programa onde o usuário
# possa digitar cinco valores numéricos e cadastre-os em
# uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

pos = ""
num = ""
valores = []

for c in range(0,5):
    num = int(input("Digite o numero: "))
    c += 1
    valores.append(c)
print(valores)


#valores.append(1)
#valores.append(2)
#valores.append(3)
#valores.append(4)

#for c in range(0,5):
#    num = int(input("Digite o numero: "))
#    pos = int(input("Digite a posicao: "))
#    valores.insert(pos, num)
#print(valores)
