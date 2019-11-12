num = [2, 5, 9, 1] # usando colchetes, cria uam lista, pode tbm ser criada como num = list()
num[2] = 3
num.append(7) # Insere um valor no fim da lista
num.sort(reverse=True) # Deixa a lista ordenada do menor pro maior, e se usar o REVERSE, do maior pro menor
num.insert(2, 7) # Na
# posicao 2, insere o elemento 7

if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 4')
print(num)
print(f'Essa lsita tem {len(num)} elementos.')

print('-'*30)
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...')

for c, v enumerate(valores):
    print(f'{v}...')