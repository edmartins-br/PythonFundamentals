import random
import operator

chain = []

for x in range (10):
    link = []
    l = random.randint (0, 50)
    link.append (l)
    s = random.randint (0, 100)
    link.append (s)
    link.append(0)
    chain.append (link)
print (f'Random Chain {chain}.')

print ()

chain.sort(key = operator.itemgetter(0))
print (f'Sort by position {chain}.') 

print ()

chain.sort(key = operator.itemgetter(1))
print (f'Sort the Strength {[link[1] for link in chain]}.')

print ()

print (f'Max Strength {max([link[1] for link in chain])}.')

print ()

print (chain)

print ()

tension = 0
new_tension = 0
count = 0
d = 0
while count < 40:
    for link in chain:
        if link[1] <= tension and link[2] == 0:
            link[2] = 1
            count = 0
        elif link[2] == 0:
            a = link[0]
            c = link[1]
            for link in chain:
                if link[2] == 1:
                    b = link[0]
                    new_tension = abs(a - b) / 10
                    if new_tension < tension:
                        tension = new_tension
                        if tension > c:
                            d = 1                 # find a way to change from the first link
                            count = 0
                            break    
            link[2] = d
    tension += 1
    count += 1
print (chain)

print ()

print (tension, new_tension, count, d, a, b, c)
