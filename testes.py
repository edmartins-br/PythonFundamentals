# =============== EXERCICIO 71 =================

# Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e
# o programa vai informar quantas cedulas de cada valor serao entregues.

# OBS: Considere que o caixa possui cedulas de R$50,00, R$20,00, R$10,00 e R$1,00

valor = 0
cd50 = cd20 = cd10 = cd1 = 0

while op in 'Ss':
    valor = int(input('Digite o valor do saque: ').strip())
    cd50 = valor // 50
    cd20 = valor //


    op = str(input('Deseja fazer masi um saque? [S/N] ').strip().upper()[0])
