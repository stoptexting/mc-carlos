from codecs import xmlcharrefreplace_errors
import matplotlib.pyplot as plt
import numpy as np
from random import uniform

def f(t):
    s1 = np.cos(2*np.pi*t)
    e1 = np.exp(-t)
    return s1 * e1

def genPoints(min, max, n):
    x = 0
    y = 0

    puntos = []
    above = []
    below = []

    i = 0
    while i < n:
        x = uniform(0, 1.5)
        y = uniform(int(min), int(max))

        if ([x, y] not in puntos):

            if (y >= np.cos(x)):
                above.append([x, y])
            else:
                below.append([x, y])
            i += 1
    return above, below

def main():
    x = np.arange(0, 1.5, 0.1)
    y = np.cos(x)

    fig, axs = plt.subplots()
    axs.plot(x, y)
    
    axs.set_xlabel('x')
    axs.set_ylabel('y = f(x)')
    axs.fill_between(x, y, color='C0', alpha=0.2)
    axs.axis([min(x), max(x), min(y), max(y)])
    n = 10000
    puntos = genPoints(0, 1.5, n)


    above = puntos[0]
    below = puntos[1]

    for i in above:
        plt.scatter(i[0] , i[1], color='red')

    for i in below:
        plt.scatter(i[0] , i[1], color='blue')

    title = '{} % of the points are below the line'.format((len(below)/(len(above)+len(below))*100))    
    axs.set_title(title)
    plt.show()

if __name__ == '__main__':
    main()