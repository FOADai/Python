from math import sqrt
time = int(input())
L = []
for i in range(time):
    n = int(input())
    L.append(sqrt(n))

for i in L:
    print('%.4f' % i)