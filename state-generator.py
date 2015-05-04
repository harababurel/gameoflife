from random import randint

n = 50
m = 50

for i in range(0, n):
    print ' '.join([str(randint(2, 4)%2) for j in range(0, m)])
