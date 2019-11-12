# ================== EXERCICIOS =========================

# 22)
# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiusculas
# O nome com todas minusculas
# Quantas letras aotodo sem considerar espacos
# Quantas letras tem o primeiro nome

print('========== EXERCICIO 22 ==========')
nome = str(input('Digite sue nome Completo')).strip()
up = nome.upper()
print(up)

lo = nome.lower()
print(lo)

nn = int(len(nome) - nome.count(' '))
print(nn)

pn = nome.split()
print(pn[0])

nnum = nome.find(' ')
print(nnum)

# =========================================================

#23) Faca um progama que leia um nomero de 0 a 9999 e msotra na tela cada um dos digitos separasos
#exemplo:

#Digite um numero: 1834

#unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1

print('========== EXERCICIO 23 ==========')
num = input('Digite um valor entre 0 e 9999: ')
print('Unidade {}, Dezena {}, Centena {} e Milhar {}.'.format(num[3],num[2], num[1], num[0]))

# =========================================================

# 24)
# Crie um programa que leia o nome da sua cidade e diga se ela comeca ou nao com a palavra "Santo"

print('========== EXERCICIO 24 ==========')
cid = str(input('Digite o nome da sua Cidade: ')).upper().strip()
nc = cid.split()
if nc[0] == 'SANTO':
   print('O nome comeca com SANTO')
else:
   print('O nome nao comeca com SANTO')

# ==========================================================

# 25)
# Crie um program que leia o nome de uma pessoa e diga se ela tem silva no nome.

print('========== EXERCICIO 25 ==========')
name = str(input('Digite o seu nome completo: ')).upper()
nc = name.find('SILVA')
if nc == -1:
    print("Nao existe SILVA no nome")
else:
    print('existe SILVA no nome')

# ==========================================================

# 26) Um programa que leia uma frase e:

# Quantas vezes aparece a letra "A"
# Em que posicao ela aparece pela primeira vez
# Em que posicao ela aparece pela ultiam vez

print('========== EXERCICIO 26 ==========')
frase = input('Digite uma frase: ').strip()
fc = frase.count('a')
print(fc)

ff = frase.find('a')
print(ff)

ff2 = frase.rfind('a')
print(ff2)

# ==========================================================

# 27)
# Faca um programa que leia o nome completo de uma pessoa e em seguida mostre o primeiro e ultimo nome separadamente

print('========== EXERCICIO 27 ==========')
name = str(input('Digite seu nome completo: ')).strip()
n = name.split()
nc = len(n)
print(n[0])
print(n[nc-1])