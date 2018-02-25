import matplotlib.pyplot as plt
import numpy as np


def f(x):
    L = 160
    return x[0] - 2/x[1]*np.sinh(x[1]*L/2)

def g(x):
    L = 160
    h = 15
    return h - 1/x[1]*(np.cosh(x[1]*L/2)-1)

def f_and_g(x):
    return np.array([f(x), g(x)])


def J_inv(x):
    L = 160
    h = 15
    J = np.array([[1, 4/(x[1]**3)*np.sinh(x[1]*L/2) - L/x[1]*np.cosh(x[1]*L/2)],
                  [0, 1/(x[1]**2)*(np.cosh(x[1]*L/2)-1)-L/2/x[1]*np.sinh(x[1]*L/2)]])
    print(J[0][0],J[0][1])
    print(J[1][0], J[1][1])
    print(1/(x[1]**2)*(np.cosh(x[1]*L/2)-1),L/2/x[1]*np.sinh(x[1]*L/2)) 
    return np.linalg.inv(J)


def phi(x):
    return x - J_inv(x).dot(f_and_g(x))

def newton():
    x = np.array([200, 0.01])
    for i in range(10):
        x = phi(x)
        print("x = {}, f(x) = {}, g(x) = {}".format(x, f(x), g(x)))



def main():
    L = 160
    h = 15
    newton()

if __name__ == "__main__":
    main()
    
