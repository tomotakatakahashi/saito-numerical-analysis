import matplotlib.pyplot as plt
import math
import numpy as np

def f(x):
    return (np.cosh(x) * np.cos(x)) - 1

def f_prime(x):
    return np.sinh(x) * np.cos(x) - np.cosh(x) * np.sin(x)

def phi(x):
    return x - f(x)/f_prime(x)

def main():
    x = np.arange(0, 6, 0.1)
    y = f(x)
    plt.plot(x, y)
    plt.show()
    x = np.arange(0.0, 12, 0.1)
    y = f(x)
    plt.plot(x, y)
    plt.show()

    x = 4
    print("x = {}, f(x) = {}".format(x, f(x)))
    for i in range(10):
        x = phi(x)
        print("x = {}, f(x) = {}".format(x, f(x)))


    x = 5
    for i in range(10):
        x = phi(x)
        print("x = {}, f(x) = {}".format(x, f(x)))

if __name__ == "__main__":
    main()
    
