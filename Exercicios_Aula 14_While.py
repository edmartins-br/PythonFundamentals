# EXERCICIOS WHILE - MUNDO 2 - LOOPS

# =============== EXERCICIO 57 =================

# Faça um programa que leia o sexo de uma pessoa, mas que só aceite os valores M ou F.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('SEXO [M/F]: ')).upper().strip()[0] # o [0] pega apenas a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Invalido. Digite novamente: ').strip().upper()[0])
print('Sexo registrado com sucesso!')


# =============== EXERCICIO 58 =================

# Melhore o jogo do DESAFIO 028 onde o computador vai "PENSAR"num numero entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

print('-='*30)
print('ADIVINHE O NUMERO: POR EDUARDO')
print('-='*30)
from random import randint
num = 0
pc = randint(1, 11)
cont = 1
while num != pc:
    num = int(input('Digite um numero: '))
    if num == pc:
        print('Voce acertou!')
    else:
        print('Tente novamente!')
        cont += 1
print('Voce tentou {} vezes!'.format(cont))
# -------------------------------------------
print('-='*30)
print('ADIVINHE O NUMERO: POR GUANABARA')
print('-='*30)
from random import randint
computador = randint(0, 10)
print('Sou seu computador...pensei num numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual e o seu melhor palpite? '))
    palpites +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez!')
        elif jogador > computador:
            print('Menos...Tente mais uma vez!')
if palpites <= 3:
    print('PARABENS! Acertou com {} tentativas'.format(palpites))
else:
    print('Voce acertou com {} tentativas. Tente melhorar.'.format(palpites))

# =============== EXERCICIO 59 =================

# Crie um programa que leia 2 valores e mostre em um menu na tela:
# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos números
# [ 5 ] Sair do Programa

# Seu programa deverá realizar a operação solicitado em cada caso.
print('-='*30)
print('INSIRA 2 VALORES E ESCOLHA UMA OPCAO')
print('-='*30)
n1 = 0
n2 = 0
op = 0
res = 0
maior = 0
menor = 0

while op != 5:
    n1 = int(input('Digite o PRIMEIRO valor: '))
    n2 = int(input('Digite o SEGUNDO valor: '))
    op = int(input('''ESCOLHA UMA OPCAO:
                    [ 1 ] SOMAR
                    [ 2 ] MULTIPLICAR
                    [ 3 ] MAIOR VALOR
                    [ 4 ] DIGITAR NOVOS NUMEROS
                    [ 5 ] SAIR
                    Escolha uma opcao: '''))
    if op == 1:
        res = n1 + n2
        print('A soma dos dois valores e igual a {}'.format(res))
        print('-=' * 30)
    elif op == 2:
        res = n1 * n2
        print('A multiplicacao dos dois valores e igual a {}'.format(res))
        print('-=' * 30)
    elif op == 3:
        if n1 > n2:
            maior = n1
            print('O maior valor e {}'.format(maior))
            print('-=' * 30)
        else:
            maior = n2
            print('O maior valor e {}'.format(maior))
            print('-=' * 30)
    elif op == 4:
        n1 = int(input('Digite o PRIMEIRO valor: '))
        n2 = int(input('Digite o SEGUNDO valor: '))
    elif op == 5:
        print('FIM')
    else:
        print('INVALIDO! Tente novamente')
        print('-=' * 30)
print('ACABOU!')
print('-=' * 30)


# =============== EXERCICIO 60 =================

# Faça um programa que leia um número qualquer e mostre o seu FATORIAL.
# EX: 5! = 5x4x3x2x1 = 120

print('-=' * 30)
print('CALCULANDO O FATORIAL!')
print('-=' * 30)

from math import factorial
numero = int(input('Digite o valor para saber o fatorial: '))
fat = factorial(numero)
print('O fatorial de {}! e {}'.format(numero, fat))

# ---------------------------------
print('-=' * 30)
n = int(input('Digite o valor para saber o fatorial: '))
c = n
res = 0
f = 1
print('O fatorial {}! = '.format(n), end='')
while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))


# =============== EXERCICIO 61 =================

# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da PA usando a estrutura WHILE

print('=-' * 20)
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')


#=============== EXERCICIO 62 =================

# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

print('=-' * 20)
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer msotrar a mais? '))
print('Progressao finalizada com {} termos mostrados'.format(total))

'''
print('DEZ TERMOS DE UMA PA')
print('=-' * 20)
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro
cont = 1
qtd = 10
while cont <= qtd:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
    if cont == qtd:
        print('\nGostaria de mostrar mais termos? Quantos? \n')
        add = int(input('Digite aqui: '))
        while cont < (qtd + add):
            if termo != 0:
                termo += razao
                cont += 1
                print('{} -> '.format(termo), end='')
            else:
                print('FIM')
'''


# =============== EXERCICIO 63 =================

# Escreva um programa que leia um número N inteiro qualuqer e mostre na tela os n primeiros elementos de uma sequência de FIBONACCI.

print('-=' * 30)
print('SEQUENCIA DE FIBONACCI')
print('-=' * 30)

qtd = int(input('Quantos termos? ').strip())
cont = 0
f1 = 0
f2 = 1
while cont <= qtd:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print('{} -> '.format(f3), end='')
    cont += 1



#=============== EXERCICIO 64 =================

# Crie um programa que leia vários números inteiros pelo teclado. o programa só vai parar
# quando o valor 999 for digitado, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

cont = 0
s = 0
n = 0
n = int(input('Digite um valor: '))
while n != 999:
    s += n
    cont += 1
    n = int(input('Digite um valor: '))
print('Voce digitou {} numeros e a soma entre eles e {}.'.format(cont, s))


# =============== EXERCICIO 65 =================

# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o MENOR e MAIOR valores lidos.
# O Programa deve perguntar ao usuários se ele quer ou não continuar a digitar valores.

op = ''
m = maior = menor = cont = 0

while op in 'Ss':
    n = int(input('Digite um numero: '))
    cont += 1

    op = str(input('Deseja continuar? [S/N] '))
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
m = (m + n) / cont
print('A media dos valores digitado foi de {}.'.format(m))
print('O MAIOR numero digitado foi {} e o MENOR foi {}.'.format(maior, menor))