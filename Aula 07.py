# nome = input('Qual o seu nome?')
# print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Primeiro valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma [e {} o produto e {} e a divisap e {:.3f}'.format(s, m, d), end=' ')
print('Divisao inteira {} e potencia {}'.format(di, e))