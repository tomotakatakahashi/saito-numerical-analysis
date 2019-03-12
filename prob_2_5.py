import matplotlib.pyplot as plt
import numpy as np

def f_gc(x):
    return 5 * np.sqrt(1-x*x) / (1+25*x*x)

def gauss_chebyshev(n):
    W = np.pi/(n+1)
    x = np.cos(( np.arange(0, n+1) + 0.5 ) * np.pi / (n + 1))
    return W * np.sum(f_gc(x))

def f_sm(x):
    return 5 / (1 + 25 * x * x)

def simpson(n):
    h = 2 / n
    x = np.arange(-1, 1+(2/n/2), 2/n/2)
    y = f_sm(x)
    res = 0
    for i in range(0, n):
        res += (y[2*i] + 4*y[2*i+1] + y[2*i+2]) / 6 * h
    return res


def main():
    y_true = gauss_chebyshev(100000)
    h_array = []
    y_array = []
    for n in range(10, 100):
        h = 2 / n
        y = gauss_chebyshev(n)
        h_array.append(h)
        y_array.append(y)
    plt.plot(h_array, y_array - y_true)
    print(3*np.pi/8)
    
    h_array = []
    y_array = []
    for n in range(10, 100):
        h = 2/n
        y = simpson(n)
        h_array.append(h)
        y_array.append(y)
    plt.plot(h_array, y_array-y_true)
    plt.show()
    print("plot of error")
    print("blue line: gauss chebyshev, green line: simpson")


if __name__ == "__main__":
    main()
    
