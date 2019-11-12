# EXERCICIOS MUNDO 2 AULA 13

# =============== EXERCICIO 46 =================

# Faca um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0,
# com uma pausa de 1 seg entre elas.

from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('BOOOOOMMMMM!!!!!')


# =============== EXERCICIO 47 =================

# Crie um programa que mostre na tela todos os numeros pares que estao no intervalo entre 1 e 50.

#from time import sleep
print('=-'*30)
for c in range (2, 50+2, 2):
    print(c)
    #sleep(0.2)
print('Estes sao todos os números pares de 1 a 50')


# =============== EXERCICIO 48 =================

# Faca um programa que calcule a soma entre todos os numeros impares que sao multiplos de 3 e que se encontram no intervalo de 1 ate 500.
print('=-'*30)
soma = 0
cont = 0
for c in range(1, 501, 2):
    if  c % 3 == 0:
    soma += c
    cont += 1
    print(c)
print('A soma de todos os {} valores solicitados é: {}'.format(cont, soma)



# =============== EXERCICIO 49 =================

# Refaca o DESAFIO 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laco FOR.

n = float(input('Digite um número para saber sua tabuada: '))
# Inseri float para poder fazer a tabuada de numeros com casas decimais
for c in range (1, 10+1):
    res = n * c
    print(n, 'X', c, '=', res)
print('FIM')



# =============== EXERCICIO 50 =================

# Desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for IMPAR, desconsidere-o.

s = 0
for c in range(0, 6):
    n = int(input('Digite um valor:'))
    if n % 2 == 0:
        s += n
print('A soma dos valores pares é: {}'.format(s))
print('FIM')



# =============== EXERCICIO 51 =================

# Desenvolva um programa que leia o primeiro termo e a razao de uma PA.
# No final, mostre os 10 primeiros termos dessa progressao.

t1 = int(input('Digite o primeiro termo da PA: '))
r1 = int(input('Digite a razão da PA: '))
res = t1
for c in range (0, 10):
    res = (res + r1)
    print('[', res, ']')
print('Fim da Progressão Aritimética')

print('RESOLVIDO PELO GUANABARA')

primeiro = int(input(''rimeiro termo: '')
razao = int(input('Razao: '))
decimo = primeiro + (10-1) * razao
for c in range (primeiro, decimo + razao, razao)
    print('{} '.format(c), end = '- ')
print('ACABOU!')



# =============== EXERCICIO 52 =================

# Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.

num = int(input('Digite um número inteiro para saber se ele é Primo: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='') # COR AMARELA
        tot += 1
    else:
        print('\033[31m', end='') # COR VERMELHA
    print('{} '. format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes!'.format(num, tot))
if tot == 2:
    print('E por isso ele É primo!')
else:
    print('E por isso ele NÃO é primo!')



# =============== EXERCICIO 53 =================

# Crie um programa que leia uma frase qualquer e diga se ela e um palindromo, desconsiderando os espacos.
# exemplos:
    # APOS A SOPA
    # A SACADA DA CASA
    # A TORRE DA DERROTA
    # O LOBO AMA O BOLO
    # ANOTARAM A DATA DA MARATONA

print('=-'*30)
frase = str(input('Digite uam frase: ').strip().upper())
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print(('Temos um palíndromo!'))
else:
    print('A frase digitada não é um palíndromo')

print('=-'*30)
print('EXERCICIO SEM UTILIZAR FOR')

frase = str(input('Digite uam frase: ').strip().upper())
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print(('Temos um palíndromo!'))
else:
    print('A frase digitada não é um palíndromo')


# =============== EXERCICIO 54 =================

# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.

print('=-'*30)
from datetime import date
ma = 0
me = 0
for c in range(0, 7):
    nsc = int(input('Digite a data de Nascimento: '))
    ida = date.today().year - nsc
    if ida > 18:
        ma = ma + 1
    else:
        me = me + 1
print('{} pessoas ja são maiores de idade.'.format(ma))
print('{} pessoas ainda são menores de idade.'.format(me))



# =============== EXERCICIO 55 =================

# Faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print('=-'*30)
maior = 0
menor = 0
for p in range(1, 6):
    pes = float(input('Digite o peso da {}a pessoa: '.format(p)))
    if p == 1:
        maior = pes
        menor = pes
    else:
        if pes > maior:
            maior = pes
        if pes < menor:
            menor = pes
print('O maior peso registrado foi {}Kg e o menor foi {}Kg'.format(maior, menor))


# =============== EXERCICIO 56 =================

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:

    #A media de didade do grupo
    # Qual e o nome do homem mais velho
    # Quantas mulheres tem menos de 20 anos

print('=-'*30)

idade = 0 # soma das idades

menor = 0 # valor da MENOR idade registrada
maior = 0 # valor da MAIOR idade registrada

nom_menor = '' # Nome da pessoa com a MENOR idade registrada
nom_maior = '' # Nome da pessoa com MAIOR idade registrada

sex_menor = 0 # Quantidade de mulheres do Sexo feminino ABAIXO de 20 anos
sex_maior = 0 # Quantidade de mulheres do Sexo feminino ACIMA de 20 anos


for p in range(1, 5):
    print('============ {} PESSOA ============'.format(p))
    nome = str(input('NOME: ')) # Le o nome da pessoa
    ida = int(input('IDADE: ')) # le a idade da pessoa
    sex = str(input('SEXO (M) ou (F): ').strip().upper()) # le o sexo da pessoa, retira espaços a diretira e esquerda e coloca em Caixa Alta
    idade += ida # Soma todas as idades registradas
    med = idade / p # Calcula a média das idades registradas baseado na quantidade de iterações do FOR
    if p == 1:
        maior = ida # registra maior idade e menor idade ao mesmo tempo, pois aidna é o primeiro registro (p == 1)
        menor = ida
    else:
        if ida > maior: # Armazena a maior idade registrada e o nome atrelado a ela
            maior = ida
            nom_maior = nome
        if ida < menor: # Armazena a menor idade e o nome atrelado a ela
            menor = ida
            nom_menor = nome
        if ida > 20 and sex == 'F': # Verifica se é MAIOR de 20 anos e armazena uam contagem na quantidade e pessoas do sexo FEM
            sex_maior += 1
        if ida < 20 and sex == 'F': # Verifica se é MENOR de 20 anos e armazena uam contagem na quantidade e pessoas do sexo FEM
            sex_menor += 1
print('A média de idade deste grupo é {}.'.format(med))
print('{} tem a MAIOR idade cadastrada: {}.'.format(nom_maior, maior))
print('Existem {} MULHERES com menos de 20 anos.'.format(sex_menor))
print('Existem {} MULHERES com mais de 20 anos.'.format(sex_maior))
