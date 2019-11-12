
# ESTRUTURA CONDICIONAL ANINHADA
nome = str(input('Qual e o seu nome?').strip())
if nome == 'Eduardo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome e bem popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome e bem normal.')
print('Tenha um bom dia, {}!'.format(nome))


# DESAFIOS AULA 12

# =============== EXERCICIO 36 =================
 # Escreva um programa para aprovar o emprestimo bancario para uma compra de uma casa. O programa vai perguntar
 # o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
 # Calcule o valor da prestacao mensal, sabendo que ela nao pode excceder 30% do salario ou entao o emprestimo sera negado.

print('==_'*20)
valor = int(input('\033[1;33mQUAL O VALOR DA CASA? R$\033[m'))
sal = int(input('\033[1;33mQUAL O SEU SALARIO? R$\033[m'))
temp = int(input('\033[1;33mDIGITE EM QUANTOS ANOS VOCE PRETENDE PAGAR: \033[m'))
meses = (temp * 12)
men = (valor / meses)
if men >= (sal * 30/100):
        print('Infelizmente voce NAO FOI APROVADO para a compra da casa.')
elif men < (sal * (30/100)):
        print('PARABENS! Voce foi aprovado para a compra da casa! Entre em contato com um consultor')
print('Para uma casa no valor de R${} e tempo de pagamento de {} meses, a sua mensalidade sera de R${:.2f}.'.format(valor, meses, men))


# =============== EXERCICIO 37 =================
# Escreva um programa que leia um numero inteiro qualquer e peca para usuario escolher qual sera a base de conversao
# - 1 para binario
# - 2 para octal
# - 3 para hexagonal
print('==_'*20)
num = int(input('DIGITE UM NUMERO INTEIRO: '))
print(''' Escolha uma das bases para conversao:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Sua opcao: '))

if op == 1:
    print('{} convertido para BINARIO e igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para OCTAL e igual a {}'.format(num, oct(num)[2:])) # [2:] ---> isso significa que so voa aparecer caracteres da 2 casa em diante
elif op == 3:
    print('{} convertido para HEXADECIMAL e igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opcao INVALIDA! Tente novamente!')


# =============== EXERCICIO 38 =================
# Escreva um programa que leia 2 numeros inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor e maior
# - O segundo valor e maior
# - Nao existe valor maior, os dois sao iguais.

print('==_'*20)
v1 = int(input('\033[1;33mDIGITE O PRIMEIRO VALOR: \033[m'))
v2 = int(input('\033[1;33mDIGITE O SEGUNDO VALOR: \033[m'))
if v1 > v2:
    print('O \033[1;33mprimeiro\033[m valor e o maior.')
elif v2 > v1:
    print('O \033[1;33msegundo\033[m valor e o maior.')
elif v1 == v2:
    print('\033[1;33mVALORES IGUAIS\033[m')

# =============== EXERCICIO 39 =================
#Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar no servico militar
# - Se e a hora de se alistar
# - Se ja passou do tempo do alistamento
# Seu programa tamb[em dever[a msotrar o tempo que falta ou que passou o prazo.

print('==_'*20)
from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
idade = (date.today().year - ano)
resta = 18 - idade
passou = idade - 18

if idade < 18:
    print('Voce aidna ira se alistar no servico militar. Faltam {} anos.'.format(resta))
elif idade == 18:
    print('Esta na hora de voce se alistar no servico militar.')
elif idade > 18:
    print('Voce ja se alistou no servico militar {} anos atras'.format(passou))


# =============== EXERCICIO 40 =================

# Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com
# a media atingida:

# - Media abaixo de 5: REPROVADO
# - Media entre 5 e 6.9: RECUPERACAO
# - Media 7.0 ou superior: APROVADO
print('==_'*20)
n1 = float(input('\033[1;33mDIGITE SUA PRIMEIRA NOTA: \033[m'))
n2 = float(input('\033[1;33mDIGITE SUA SEGUNDA NOTA: \033[m'))
media = float((n1 + n2) / 2)
if media < 5.0:
    print('\033[1;30;41mREPROVADO\033[m')
    print('Sua media foi {}'.format(media))
elif 7 > media >= 5:
    print('\033[1;31;43mRECUPERACAO\033[m')
    print('Sua media foi {}'.format(media))
elif media >= 7.0:
    print('\033[1;30;42mAPROVADO\033[m')
    print('Sua media foi {}'.format(media))

# =============== EXERCICIO 41 =================

# A confederacao nacional de natacao precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:

# Ate 9 anos: MIRIM
# Ate 14 anos: INFANTIL
# Ate 19 anos: JUNIOR
# Ate 20 anos: SENIOR
# Acima:MASTER
print('==_'*20)
from datetime import date
nasc = int(input('QUAL O ANO DE NASCIMENTO DO NADADOR?'))
atual = date.today().year
ida = atual - nasc

if ida <9:
    print('O atleta tem {} anos.'.format(ida))
    print('Classificacao: MIRIM')
elif ida >=9 and ida < 14:
    print('O atleta tem {} anos.'.format(ida))
    print('Classificacao: INFANTIL')
elif ida >= 14 and ida < 19:
    print('O atleta tem {} anos.'.format(ida))
    print('Classificacao: JUNIOR')
elif ida >= 19 and ida < 20:
    print('O atleta tem {} anos.'.format(ida))
    print('Classificacao: SENIOR')
elif ida > 20:
    print('O atleta tem {} anos.'.format(ida))
    print('Classificacao: MASTER')

# =============== EXERCICIO 42 =================

# Reforca o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado.
# Equilatero: todos os lados iguais
# Isosceles: dois lados iguais
# Escaleno: todos os lados diferentes
print('==_'*20)
r1 = float(input('INSIRA O PRIMEIRO SEGMENTO: ').strip())
r2 = float(input('INSIRA O SEGUNDO SEGMENTO: ').strip())
r3 = float(input('INSIRA O TERCEIRO SEGMENTO: ').strip())

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmento PODEM FORMAR um triangulo ', end = ' ')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos acima NAO PODEM FORMAR um triangulo')

#if (b-c) < a < (b+c) and (a-c) < b < (a+c) and (a-b) < c < (a+b):
#    print('SIM! E POSSIVEL criar um triangulo a={}, b={} e c={}'.format(a, b, c))
#else:
#    print('NAO! E IMPOSSIVEL criar um triangulo a={}, b={} e c={}'.format(a, b, c))


#if a == b == c and ((b-c) < a < (b+c) and (a-c) < b < (a+c) and (a-b) < c < (a+b)):
#    print('O TRIANGULO E EQUILATERO!')
#elif a == b or a == c or b == c and ((b-c) < a < (b+c) and (a-c) < b < (a+c) and (a-b) < c < (a+b)):
#    print('O TRIANGULO E ISOSCELES!')
#elif a != b != c and ((b-c) < a < (b+c) and (a-c) < b < (a+c) and (a-b) < c < (a+b)):
#    print('O TRIANGULO E ESCALENO')

# =============== EXERCICIO 43 =================

# Desenvolva uma logica que leia o peso e a altura de uam pessoa, calcule seu IMC e msotre seus status,
# de acordo com a tabela abaixo.

# Abaixo de 18.5: ABAIXO DO PESO
# Entre 18.5 e 25: PESO IDEAL
# De 25 a 30: SOBREPESO
# De 30 a 40: Obesidade
# Acima de 40: OBESIDADE MORBIDA
print('==_'*20)
peso = float(input('DIGITE O SEU PESO: '))
alt = float(input('DIGITE SUA ALTURA: '))
res = (peso / (alt**2))

if res < 18.5:
    print('Seu IMC e {:.2f}'.format(res))
    print('Voce esta abaixo do peso normal, alimente-se melhor.')
elif 18.5 <= res <= 25:
    print('Seu IMC e {:.2f}'.format(res))
    print('PARABENS! Voce esta no peso ideal.')
elif 25 <= res <= 30:
    print('Seu IMC e {:.2f}'.format(res))
    print('Voce esta com SOBREPESO.')
elif 30 <= res <= 40:
    print('Seu IMC e {:.2f}'.format(res))
    print('Voce esta classificado com OBESIDADE, precisar emagrecer!')
elif res >= 40:
    print('Seu IMC e {:.2f}'.format(res))
    print('Voce esta com OBESIDADE MORBIDA, procure um medico IMEDIATAMENTE!')

# =============== EXERCICIO 44 =================

# Elabore um programa que calcule o valor a ser pago por um produto, considerando
# o seu preco normal e condicao de pagamento.

# A vista dinheiro ou cheque: 10% de desconto
# A vista no cartao: 5% de desconto
# Em ate 2x no cartao: preco normal
# 3x ou mais no cartao: 20% de juros

print('==_'*20)
pdt = float(input('QUAL O VALOR DO PRODUTO? '))
pgt = int(input('QUAL A FORMA DE PAGAMENTO? \n'
                '[ 1 ] Para pagar a vista no CHEQUE ou DINHEIRO.\n'
                '[ 2 ] Para pagar a vista no CARTAO.\n'
                '[ 3 ] Para pagar em ate 2X no CARTAO.\n'
                '[ 4 ] Para pagar em 3X ou mais no CARTAO.'
                'Qual sua opcao? '))
avdc = pdt - (pdt*10/100)
avc = pdt - (pdt*5/100)
xx = pdt
xxx = pdt + (pdt*20/100)

if pgt == 1:
    print('Voce teve 10% de desconto e o valor final e R${}'.format(avdc))
elif pgt == 2:
    print('Voce teve 5% de desconto e o valor final e R${}'.format(avc))
elif pgt == 3:
    print('Voce NAO teve desconto e o valor final e R${}'.format(xx))
elif pgt == 4:
    print('Voce ira pagar 20% de JUROS e o valor final e R${:.2f}'.format(xxx))

# =============== EXERCICIO 45 =================

# Crie um programa que faca o computador jogar JOKENPO com voce
print('==_'*20)
from random import randint
from time import sleep
print('JOKENPO GAME')
print('''Instrucoes: Para jogar comigo voce devera escolher:
        [ 1 ] PEDRA
        [ 2 ] PAPEL
        [ 3 ] TESOURA''')

res = int(input('Qual vai ser sua jogada? '))
print('-='*20)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('-='*20)
pc = randint(1, 3)

# pedra ganha de tesoura
# Papel ganha de pedra
# tesoura ganha de papel
# papel com papel empata
# pedra com pedra empata
# tesoura com tesoura empata

# 1 > 3         #PEDRA  = 1
# 2 > 1         #PAPEL = 2
# 3 > 2         #TESOURA = 3
# 2 == 2
# 1 == 1
# 3 == 3

if res == 1 and pc == 3:
    print('PC: TESOURA || JOGADOR: PEDRA, voce GANHOU!')
elif res == 2 and pc == 1:
    print('PC: PEDRA || JOGADOR: PAPEL, voce GANHOU!')
elif res == 3 and pc == 2:
    print('PC: PAPEL || JOGADOR: TESOURA, voce GANHOU!')
elif res == 3 and pc == 1:
    print('PC: TESOURA || JOGADOR: PAPEL, voce PERDEU!')
elif res == 1 and pc == 2:
    print('PC: PAPEL || JOGADOR: PEDRA, voce PERDEU!')
elif res == 2 and pc == 3:
    print('PC: TESOURA || JOGADOR: PAPEL, voce PERDEU!')
elif res == 2 and pc == 2:
    print('PC: PAPEL || JOGADOR: PAPEL. Hmm...Empatamos!')
elif res == 1 and pc == 1:
    print('PC: PEDRA || JOGADOR: PEDRA. Hmm...Empatamos!')
elif res == 3 and pc == 3:
    print('PC: TESOURA || JOGADOR: TESOURA. Hmm...Empatamos!')
elif res != 1 and res != 2 and res != 3:
    print('DIGITE UM NUMERO ENTRE 1 E 3')
