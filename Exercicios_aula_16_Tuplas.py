# =============== EXERCICIO 72 =================

# Crie um programa que crie uam tupla totalmente preenchida com uma contagem por extenso, de ZERO ate VINTE.
# Seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso.
'''
print('Exercício 72')
print('=-'* 30)

num = ''
op = ''
cont = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze',
        'Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove', 'Vinte')


while op in 'Ss':
    num = int(input('Digite um valor: '))
    if num in range(0, 21):
        print(cont[num])
        op = str(input('Deseja Continuar? [S/N]'))
    else:
        print('Tente Novamente com um numero entre 0 e 20!')
print('FINALIZADO!')


# =============== EXERCICIO 73 =================

# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebo.
# na ordem de colocação e depois mostre:

# A) Apenas os 5 primeiros colocados
# B) Os ultimos 4 colocados da tabela
# C) Uma lista com os times em ordem alfabetica
# D) Em que posicao da tabela esta o time da Chapecoense

print('Exercício 73 - BRASILEIRAO')
print('=-' * 30)

times = ('Santos', 'Palmeiras', 'Flamengo', 'Atletico', 'Sao Paulo', 'Corinthians', 'Botafogo', 'Internacional',
         'Ceara SC', 'Bahia', 'Athletico PR', 'Fortaleza', 'Goias', 'Gremio',
         'Vasco da Gama', 'Fluminense', 'Cruzeiro', 'Chapecoense', 'CSA', 'Avai', )

print('OS 5 PRIMEIROS COLOCADOS')
print(times[0:6])

print('OS ULTIMOS 4 COLOCADOS')
print(times[-4:])

print('EM ORDEM ALFABÉTICA')
print(sorted(times))

print(f'O time da Chapecoense esta na {times.index("Chapecoense")+1}a posição: ')


# =============== EXERCICIO 74 =================

# Crie um programa que vai gerar 5 numeros aleatorios e colocar em uma tupla.
# Depois disso mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na tupla.

print('Exercício 74')
print('=-'* 30)
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram: {numeros}')
print(f'O maior numero sorteado foi: {max(numeros)}!')
print(f'O menor número sorteado foi: {min(numeros)}!')



# =============== EXERCICIO 75 =================
#
# # Desenvolva um programa que leia 5 valores pelo teclado e guarde-os em uma tupla. No final Mostre:
#
# # A) Quantas vezes apareceu o valor 9
# # B) Em que posicao foi digitado o primeiro valor 3
# # C) Quais foram os numeros pares.

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
d = int(input('Digite o quarto valor: '))
e = int(input('Digite o quinto valor: '))
parimp = ''
num = (a, b, c, d, e)
print(f'OS VALORES DIGITADOS FORAM: {num}')
print(f'O numero 5 apareceu {num.count(5)} vezes!')
if 3 in num:
    print(f'O numero 3 foi digitado pela primeira vez na posicao {num.index(3)+1}')
elif 3 not in num:
    print('O numero 3 nao foi digitado!')
for c in num:
    if c % 2 == 0:
        print(f'PAR: {c}')
'''

# =============== EXERCICIO 76 =================

# Crie um programa que tenha uma tupla unica com nome de produtos e seus respectivos precos na sequencia.
# No final, mostre uma listagem de precos, organizando os dados em forma tabular.
produtos = ('Caneta', 'R$2,00',
            'Caderno', 'R$7,00',
            'Notebook', 'R$1500,00',
            'Cola', 'R$7,00',
            'Folha Sulfite', 'R$14,00',
            'Borracha', 'R$1,00',
            'Lapiseira de Inox', 'R$23,00',
            'Lapis', 'R$1,75',
            'Pasta', 'R$5,00',
            'Grafite', 'R$3,75')
# mostrar os produtos e preços em forma de tabela
print('-'*40)
print(f'{"LISTA DE PREÇOS":ˆ40}')
print('-'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'Preço: {produtos[pos]:7}')
print('-'*40)

# =============== EXERCICIO 77 =================

# Crie uam programa que tenha uma tupla com varias palavras, (nao usar acentos).
# Depois disso, voce deve mostrar para cada palavra. ausi sao as suas vogais.