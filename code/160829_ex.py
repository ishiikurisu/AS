import numpy as np
import matplotlib.pylab as mpl

def ex1():
    global m
    m = np.array([[1, 2, 3.2],
                  [4, 5, 2.3],
                  [1, 2, 5]])
    return 'det M = %s' % (np.linalg.det(m))

def ex2():
    v = np.linspace(1, 100, 200)
    f = 'primeiro item: %s\tultimo item: %s\tTamanho:%s'
    ans = f % (v[0], v[-1], len(v))
    return ans

def ex3():
    global m
    n = np.ones_like(m)
    return np.dot(m, n)

def ex4():
    global m
    return np.linalg.inv(m)

def ex5():
    x = np.array([3, 5, 6.7])
    y = np.array([2, 3, 4.6])
    return np.cross(x, y)

def ex6():
    x = np.zeros([5, 5])

    for j in xrange(5):
        for i in xrange(5):
            x[j][i] = (i+1) + (j+1)
    
    return x

if __name__ == '__main__':
    exs = [ex1, ex2, ex3, ex4, ex5, ex6]
    for i, ex in enumerate(exs):
        print '# Exercicio %d' % (i+1)
        print ex()
        print ''
