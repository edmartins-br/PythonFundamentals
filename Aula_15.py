n = s = 0
while True:
    n = int(input('VALOR: '))
    if n == 999:
        break
    s += n
print(f'Soma vale {s}') # Nova atualizacao chamada F STRING que substitui o .format.

nome = 'Eduardo'
idade = '32'
salario = 5423.32
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}.')

# =============== EXERCICIO 66 =================

# Crie um programa que leia vários números inteiros pelo teclado. o programa só vai parar
# quando o valor 999 for digitado, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

n = cont = soma = 0
while True
    n = int(input('VALOR: '))
    if n == 999:
        break
    else:
        cont += 1
        soma += n
print(f'Voce digitou {cont} numeros e a soma entre eles foi {soma}')
# =============== EXERCICIO 67 =================

# Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
# O programa sera interrompido quando o numero solicitado for negativo.


print('-=' *30)
print('PROGRAMA TABUADA')
print('-=' *30)
mult = 0
op = ''
n = 1
while n > 0:
    n = int(input('Quero saber a tabuado do... '))
    for c in range(1, 11):
        mult = c * n
        print(f'{c} X {n} = {mult}')
print('FIM DA TABUADA!')

# =============== EXERCICIO 68 =================

# Faca um programa para jogar par ou impar com o computador. O jogo sera interrompido quando o jogador PERDER,
# mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

print('-=' * 30)
print('PROGRAMA PAR OU IMPAR!')
print('-=' * 30)

from random import randint
cont = 0
perdeu = True
jogador = ''
numero_jogador = 0
pc = ''
numero_pc = 0
soma = 0


while perdeu:
    numero_jogador = int(input('Digite um numero: '))
    jogador = str(input('Voce quer PAR ou IMPAR? [P/I] ').upper())
    numero_pc = randint(1, 10)
    soma = numero_jogador + numero_pc
    if jogador == 'P':
        pc = 'I'
    elif jogador == 'I':
        pc = 'P'

    if soma % 2 == 0 and jogador == 'P':
        print('VOCE VENCEU VENCEU!')
        cont += 1
        perdeu = True
    elif soma % 2 != 0 and jogador == 'I':
        print('VOCE VENCEU VENCEU!')
        cont += 1
        perdeu = True
    else:
        perdeu = False

print('Voce perdeu!!!')
print(f'Voce teve {cont} vitorias')


# =============== EXERCICIO 69 =================

# Crie um programa que leia a idade e o sexo de varias pessoas.
# A cada pessoa cadastrada o programa devera perguntar se usuario que continuar ou nao.
# No final mostre:

# A) Quantas pessoas tem menos de 18 anos.
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos

print('-=' * 30)
print('CADASTRO!')
print('-=' * 30)

idade = 0
sexo = ''
cont_masc = 0
cont18 = 0
contm20 = 0
op = ''

while op in 'Ss':
    idade = int(input('IDADE: ').strip())
    sexo = str(input('SEXO [M/F]: ').upper().strip())
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ').upper().strip())

    if idade < 20 and sexo == 'F':
        contm20 += 1
    if idade < 18:
        cont18 += 1
    if sexo == 'M':
        cont_masc += 1
    op = str(input('Deseja continuar cadastrando? [S/N]'))
print(f'A) Existem {cont18} pessoas com menos de 18 anos.')
print((f'B) Existem {cont_masc} homens cadastrados.'))
print(f'C) Existem {contm20} mulheres com menos de 20 anos.')


print('-=' * 30)
print('CADASTRO! POR GUANABARA')
print('-=' * 30)



# =============== EXERCICIO 70 =================

# Crie um programa que leia o nome e o preco de varios produtos. O programa devera perguntar se o usuario vai continuar.
# No final, mostre:

# A) Qual o total gasto na compra
# B) Quantos produtos custam mais de R$1000,00
# C) Qual o nome do dprduto masi barato

print('-=' * 30)
print('BARATAO SUPERMERCADAO!')
print('-=' * 30)

menor_produto = ''
cont = 0
menor_preco = 0
cont_prod = 0
total = 0
op = ''

while op in 'Ss':
    ent_produto = str(input('PRODUTO: ').strip())
    ent_preco = float(input('PRECO: ').strip())
    cont += 1
    if cont == 1:
        menor_preco = ent_preco
    if ent_preco > 1000:
        cont_prod += 1
    elif ent_preco < menor_preco:
        menor_produto = ent_produto
        menor_preco = ent_preco
    total += ent_preco
    op = str(input('Quer continuar cadastrando? [S/N]').strip().upper()[0])
print(f'Voce gastou um total de R${total}.')
print(f'Sua lista possui {cont_prod} itens que custam mais de R$1.000,00.')
print(f'O produto mais barato foi o item {menor_produto}, no valor de R${menor_preco}')


# =============== EXERCICIO 71 =================

# Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e
# o programa vai informar quantas cedulas de cada valor serao entregues.

# OBS: Considere que o caixa possui cedulas de R$50,00, R$20,00, R$10,00 e R$1,00
