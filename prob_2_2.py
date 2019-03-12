import numpy as np
import matplotlib.pyplot as plt



def f(theta, theta_0):
    return 1 / np.sqrt( 1 - np.sin(theta_0 / 2)**2 * np.sin(theta) ** 2)

def simpson(theta_0):
    n = 1000
    theta = np.arange(0, np.pi/2*(1+1/(2*n)), np.pi/2/(2*n))
    y = f(theta, theta_0)
    h = np.pi/2/n
    res = 0
    for i in range(n):
        res += h * (y[2*i]+ 4*y[2*i+1] +y[2*i+2]) / 6
        # print(res)
    return res


def h(theta_0):
    return simpson(theta_0)

def main():
    print("h(pi/12) =", h(np.pi/12))
    print("h(pi/6) = ", h(np.pi/6))
    print("h(pi/4) = ", h(np.pi/4))
    
    x = []
    y = []
    for i in range(10, 1000):
        x.append(1/i)
        y.append(h(1/i) - np.pi/2)
    plt.plot(x, y)
    plt.show()
    print("The graph of x and h(x) - pi/2")


if __name__ == "__main__":
    main()
