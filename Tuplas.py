print('=-' * 30)
print('MUNDO 3 - AULAS DE TUPLAS')
print('=-' * 30)

lanche = ('hamburger', 'suco', 'pizza', 'pudim')
print(lanche[1]) # mostra o segundo elemento pois a contagem se inicia no zero
print(lanche[2])
print(lanche[1:3]) # mostra do 1 ao 3 ignorando o elemento 3
print(lanche[-3]) # mostr ao terceiro elemento contanto do final par ao inicio
print(lanche[-2]) # mostr ao segundo elemento contanto do final par ao inicio
print(lanche[2:]) # mostra do 2 ate o final
print(lanche[:2]) # mostra do inicio ate o 2 ignorando o 2
print(lanche[-2:]) # mostra do elemento 2, contando do final para o inicio, ate o começo

# --------------------------------------------------------------------------------------------
print('=-' * 30)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print(len(lanche))

# --------------------------------------------------------------------------------------------
print('=-' * 30)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} ma posicao {cont}')
print('Comi pra caramba!')

# --------------------------------------------------------------------------------------------
print('=-' * 30)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} ma posicao {pos}')
print('Comi pra caramba!')

# --------------------------------------------------------------------------------------------
print('=-' * 30)
print(sorted(lanche))

# --------------------------------------------------------------------------------------------
print('=-' * 30)
a = (1, 2, 3, 4)
b = (5, 6, 2)
c = a + b
d = b + a
print('Ao somar duas tuplas voce concatena as duas tuplas')
print(c)
print(d)

print('Quantas vezes aparece o numero 2 dentro da tupla')
print(c.count(2))
print('Em que posicao esta o numero 6?')
print(c.index(6))

pessoa = ('Eduardo', 32, 'M', 127.3)
print('No Python é possivel guardar valores tanto numericos quanto strings dentro das tuplas')
print(pessoa)
del(pessoa)
print(pessoa)