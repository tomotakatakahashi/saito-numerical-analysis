import numpy as np
import matplotlib.pyplot as plt


def g(t):
    return 2*t*t*np.cos(t*t)
    
def simpson(n):
    s = 0
    interval = np.arange(0, np.sqrt(np.pi)*(1+1/(2*n)), np.sqrt(np.pi)/(2*n))
    values = g(interval)
    h = np.sqrt(np.pi)/n
    for i in range(n):
        s += h * (values[2*i]+4*values[2*i+1]+values[2*i+2])/6
    # print("h = {}, s = {}".format(h, s))
    return s, h
    
def main():
    x = np.arange(0, np.sqrt(np.pi)+10**(-5), 10**(-5))
    y = g(x)
    plt.plot(x, y)
    plt.show()
    plt.figure()
    s_true, _ = simpson(10**6)
    h = []
    s = []
    for n in range(10, 100):
        s_, h_ = simpson(n)
        h.append(h_)
        s.append(s_)
    plt.plot(h, s_true-s)
    plt.show()
    plt.figure()
    plt.plot(np.log(h), np.log(np.abs(s_true-s)))
    plt.show()
    print((np.log(s-s_true)[-1]-np.log(s-s_true)[-2])/(np.log(h)[-1]-np.log(h)[-2]))
    




if __name__ == "__main__":
    main()
    
