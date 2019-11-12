# Aulas sobre condicoes

# =========== EXERCICIO 28 ============
# Escreva um programa que faca o computador pensar em um numero inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
print('Vou pensar em um numero e voce deve adivinhar!')
n = random.randint(0, 5)
nu = int(input('Digite o numero e vamos ver se voce acertou: '))
print('PROCESSANDO...')
sleep(3)
if nu == n:
    print('PARABENS! VOCE ACERTOU!')
else:
    print('INFELIZMENTE, VOCE ERROU!')


# =========== EXERCICIO 29 ============

# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassaar 80km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por cada Km aciam do limite.

v = int(input('QUAL FOI A VELOCIDADE DO CARRO?').strip())
if v > 80:
    exc = v - 80
    multa = exc * 7
    print('VOCE FOI MULTADO em R${},00'.format(multa))
else:
    print('VOCE NAO FOI MULTADO! CONTINUE!')


# =========== EXERCICIO 30 ============

# Crie um programa que leia um número inteiro e mostra na tela se ele é PAR ou IMPAR.

num = int(input('DIGITE UM VALOR INTEIRO: ').strip())
if num % 2 == 0:
    print('NUMERO PAR')
else:
    print('NUMERO IMPAR')



# =========== EXERCICIO 31 ============

# Desenvolva um programa que pergunte a distãncia de uma viagem em Km. Calcule o preço da passagem, cobrando
# R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

dis = float(input('QUAL A DISTANCIA DA VIAGEM?').strip())
if dis <= 200:
    val = dis * 0.5
    print('Sua viagem vai custar R${}'.format(val))
elif dis > 200:
    val2 = dis * 0.45
    print('Sua viagem vai custar R${}'.format(val2))


# =========== EXERCICIO 32 ============

# Faça um programa que leia um ano qualquer e mostre se é um ano BISSEXTO.
from datetime import date
ano = int(input('DIGITE O ANO QUE DESEJA SABER SE E BISSEXTO: ').strip())
if ano == 0;
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} E bissexto!'.format(ano))
else:
    print('O ano NAO e bissexto!')



# =========== EXERCICIO 33 ============

# Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor.

nb1 = int(input('DIGITE O PRIMEIRO VALOR: ').strip())
nb2 = int(input('DIGITE O SEGUNDO VALOR: ').strip())
nb3 = int(input('DIGITE O TERCEIRO VALOR: ').strip())

if nb1 > nb2 > nb3:
    print('O MAIOR valor e {}'.format(nb1))
    print('O MENOR valor e {}'.format(nb3))
elif nb1 > nb3 > nb2:
    print('O MAIOR valor e {}'.format(nb1))
    print('O MENOR valor e {}'.format(nb2))
elif nb2 > nb1 > nb3:
    print('O MAIOR valor e {}'.format(nb2))
    print('O MENOR valor e {}'.format(nb3))
elif nb2 > nb3 > nb1:
    print('O MAIOR valor e {}'.format(nb2))
    print('O MENOR valor e {}'.format(nb1))
elif nb3 > nb1 > nb2:
    print('O MAIOR valor e {}'.format(nb3))
    print('O MENOR valor e {}'.format(nb2))
elif nb3 > nb2 > nb1:
    print('O MAIOR valor e {}'.format(nb3))
    print('O MENOR valor e {}'.format(nb1))
elif nb1 == nb2 == nb3:
    print('OS VALORES SAO TODOS IGUAIS')



# =========== EXERCICIO 34 ============

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.200,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('DIGITE O SEU SALARIO: ').strip())
if sal > 1200:
    sal2 = sal + (sal * (10/100))
    print('Seu novo salario e R${}'.format(sal2))
else:
    sal3 = sal + (sal * (15/100))
    print('Seu novo salario e R${}'.format(sal3))


# =========== EXERCICIO 35 ============

# Desenvolva um programa que leia2
# o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo.

a = float(input('INSIRA A PRIMEIRA RETA: ').strip())
b = float(input('INSIRA A SEGUNDA RETA: ').strip())
c = float(input('INSIRA A TERCEIRA RETA: ').strip())

if (b-c) < a < (b+c) and (a-c) < b < (a+c) and (a-b) < c < (a+b):
    print('SIM! E POSSIVEL criar um triangulo a={}, b={} e c={}'.format(a, b, c))
else:
    print('NAO! E IMPOSSIVEL criar um triangulo a={}, b={} e c={}'.format(a, b, c))
