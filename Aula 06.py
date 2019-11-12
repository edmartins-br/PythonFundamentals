# n = input('Digite algo: ')
# print(n.isnumeric()) # e numerico?
# print(n.isalpha()) # e alfa?
# print(n.isalnum()) # e alfanumerico?
# print(n.isupper()) # e caixa alta?

# Faca um porgrama que leia dois numeros e realize a soma entre ele mostrando o resultado
# Faca um porgrama que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
s = n1+n2

print('A soma entre {} e {} ]e igal a {}'.format(n1, n2, s))

print('AGORA VAMOS AVALIAR AS PROPRIEDADES DO TEXTO DIGITADO')

tx = input('Digite algo: ')
print('O texto e numerico? = ', tx.isnumeric())
print('O texto e CAIXA ALTA? = ', tx.isupper())
print('O texto e alfa numerico? = ', tx.isalnum())
print('O texto e alfabetico? = ', tx.isalpha())

