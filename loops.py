for c in range(1, 7):
    print(c)
print('FIM')

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('-='*20)

for c in range(6, 0, -1): # o (-1) define o tipo de iteracao, neste caso, decrescente.
    print(c)
print('FIM')

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('-='*20)

for c in range(0, 7, 2): # conta de 2 em 2
    print(c)
print('FIM')

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('-='*20)

n = int(input('Digite um numero'))
for c in range(0, n+1): # Conta ate o valor armazenado em N e soma + 1 pra chegar no valor exato digitado, pois a contagem comeca do 0
    print(c)
print('FIM')

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('-='*20)

i = int(input('Digite um inicio'))
f = int(input('Digite um fim'))
p = int(input('Digite um passo'))

for c in range(i, f+1, p): # Conta ate o valor armazenado em N e soma + 1 pra chegar no valor exato digitado, pois a contagem comeca do 0
    print(c)
print('FIM')

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('-='*20)

s = 0
for c in range(0, 3):
    n = int(input('Digite um numero: '))
    s = s + n # ou s += n
print('A soma dos valores foi {}'.format(s))