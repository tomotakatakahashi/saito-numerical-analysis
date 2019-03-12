import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (1 - x * x)**2

def gauss_chebyshev(n):
    W = np.pi/(n+1)
    #print("W = {}".format(W))
    x = np.cos(( np.arange(0, n+1) + 0.5 ) * np.pi / (n + 1))
    #print("x = {}".format(x))
    #print("f(x) = {}".format(f(x)))
    #print("sum(f(x)) = {}".format(np.sum(f(x))))
    return W * np.sum(f(x))


def main():
    h_array = []
    y_array = []
    for n in range(1, 100):
        h = 2 / n
        y = gauss_chebyshev(n)
        h_array.append(h)
        y_array.append(y)
        #print(h, y)
        #print(h, y)
    plt.plot(h_array, y_array)
    plt.show()
    print(3*np.pi/8)


if __name__ == "__main__":
    main()
    
