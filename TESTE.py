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