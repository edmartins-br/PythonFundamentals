'''
import math
import random
import emoji

# from math import sqrt, floor - usar isso para importar partes especificar da biblioteca
num = int(input('Digite um valor: '))
raiz = math.sqrt(num)
print('A raiz de {} e {}'.format(num, raiz))

num = random.randint(1, 10) # sortear um numero inteiro de 1 ate 10
print(num)

print(emoji.emojize("Ola mundo :earth_americas:", use_aliases=True))


# 01 Crie um programa que leia um numero real qualquer pelo teclado e msotre na tela a sua porcao inteira
real = float(input('Digite um valor REAL: '))
res = int(real)
print('A parte inteira do numero qeu voce digitou e {}:'.format(res))

# 02 Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule
# e mostre o comprimento da sua hipotenusa

from math import sqrt, cos, sin, tan, radians # import math ----> importa todas as funcoes da biblioteca e nao soemnte as descritas
op = float(input('Digite o valor do cateto oposto: '))
ad = float(input('Digite o valor do Cateto Adjacente: '))
hip = sqrt((op ** 2) + (ad ** 2)) # pode ser utilizado tbm com a biblioteca -----> math.hypot(op, ad)
print('Comprimento da Hipotenusa = {}'.format(hip))

# 03 Faca um porgrama que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente deste angulo

ang = float(input('Digite o angulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print('Sin = {:.3f}, Cos = {:.3f} e Tan = {:.3f}'.format(sen, cos, tan))


# sortear um aluno

import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Primeiro aluno: '))
a3 = str(input('Primeiro aluno: '))
a4 = str(input('Primeiro aluno: '))

lista = [a1, a2, a3, a4]

escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

'''
from random import shuffle
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = [a1, a2, a3, a4]

ordem = shuffle(lista)
print('A ordem sera: ')
print(lista)