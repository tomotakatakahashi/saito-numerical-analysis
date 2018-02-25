import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return sum(x*x) - 3

def g(x):
    return x[0]*x[1] - 1

def f_g(x):
    return np.array([f(x), g(x)])

def J_inv(x):
    J = np.array([[2*x[0], 2*x[1]], [x[1], x[0]]])
    return np.linalg.inv(J)

def newton(x0):
    x = x0
    for i in range(10):
        x = x - J_inv(x).dot(f_g(x))
        print("x = {}, f(x) = {}, g(x) = {}".format(x, f(x), g(x)))


def f_1var(x):
    return x**2 + x**(-2) - 3

def f_1var_prime(x):
    return 2*x - 2 * ( x**(-3))

def phi(x):
    return x - f_1var(x)/f_1var_prime(x)
        
def newton_1var():
    x = 0.5
    for i in range(10):
        x = phi(x)
        print("x = {}, y = {}, f(x) = {}".format(x, 1/x, f_1var(x)))
        
def main():
    newton(x0 = np.array([2, 1]))
    print("----------------------------")
    newton_1var()
    


if __name__ == "__main__":
    main()
    
