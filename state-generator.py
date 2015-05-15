from random import randint

while True:
    n = raw_input('height (1 - 500): ')

    try:
        n = int(n)
        assert(1 <= n and n <= 500)
    except:
        print 'height must be an integer between 1 and 500.'
    else:
        break

while True:
    m = raw_input('width (1 - 500): ')

    try:
        m = int(m)
        assert(1 <= m and m <= 500)
    except:
        print 'width must be an integer between 1 and 500.'
    else:
        break

while True:
    rho = raw_input('density (0.0 - 1.0): ')

    try:
        rho = float(rho)
        assert(0.0 <= rho and rho <= 1.0)
    except:
        print 'density must be a float between 0.0 and 1.0.'
    else:
        break

print 'generating configuration...'
with open('initial-state.in', 'w') as g:
    for i in range(0, n):
        g.write('%s\n' % ''.join(['.#'[randint(1, 100) <= 100*rho] for j in range(0, m)]))

