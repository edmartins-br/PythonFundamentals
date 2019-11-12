# 01 Faca um programa que leia um numero inteiro e mostra na tela o seu sucessor e o seu antecessor
n = float(input('Digite um numero: '))
na = n -1
ns = n+1
print('O valor escolhido foi {}, o antecessor e = {} e o sucessor e {}'.format(n, na, ns))

#  Crie um algoritmo que leia um numero e mostre o dobro, o triplo e a raiz quadrada
n2 = int(input('Digite um numero'))
dbl = n2 * 2
tpl = n2 * 3
root = n2 ** (1/2)
print('O dobro do numero digitado e {}, o triplo e {} e a raiz e {}!'.format(dbl, tpl, root))

# 03 desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media
nt1 = float(input('Digite a NOTA 1'))
nt2 = float(input('Digite a NOTA 2'))
media = (nt1 + nt2) / 2
print('A media do aluno e {}'.format(media))

# 04 Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros mm
met = float(input('Isnira o valor em metros: '))
cm = met * 100
mm = met * 1000
print('{} metro(s) contem {} centimetros ou {} milimetros.'.format(met, cm, mm))


05 Faca um porgrama que leia um numero qualquer e mostra na tela a sua tabuada
num = float(input('Digite um numero para saber sua tabuada completa: '))
# neste caso existem formas melhores, mas resolvi fazer assim para ajudar no entendimento para que nunca estudou outras lnguagens
t1 = num * 1
t2 = num * 2
t3 = num * 3
t4 = num * 4
t5 = num * 5
t6 = num * 6
t7 = num * 7
t8 = num * 8
t9 = num * 9
t10 = num *10
print('Veja abaixo a tabuada do {}:'.format(num))
print('{} x 1 = {} '.format(num, t1))
print('{} x 2 = {} '.format(num, t2))
print('{} x 3 = {} '.format(num, t3))
print('{} x 4 = {} '.format(num, t4))
print('{} x 5 = {} '.format(num, t5))
print('{} x 6 = {} '.format(num, t6))
print('{} x 7 = {} '.format(num, t7))
print('{} x 8 = {} '.format(num, t8))
print('{} x 9 = {} '.format(num, t9))
print('{} x 10 = {} '.format(num, t10))



# 06 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre ma tela, quantos dolares ela pode comprar.
qtd = float(input('Quanto dinheiro voce tem na carteira? '))
dol = qtd / 3.27
print('Com esse valor, voce pode compra {:.2f} dolares. '.format(dol))


#07 Faca um programa que leia a largura e a altura de uma parede e metros, e calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m2
wid = int(input('Qual a largura da parede? '))
hei = int(input('Qual a altura da parede? '))
a = wid * hei
res = a / 2
print('Voce precisara de {} litros de tinta par apintar esta parede! '.format(res))


#08 Faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto.
preco = float(input('Insira o preco do produto: '))
pfinal = preco - (preco * (5/100))
print('O preco final do produto e {} reais.'.format(pfinal))

#09 Faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
sal = float(input('Insira o Salario: '))
sfinal = sal + (sal * (15/100))
print('O preco final do produto e {} reais.'.format(sfinal))