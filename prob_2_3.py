import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.absolute(np.sin(np.pi*x-np.pi/4))
    

def mid(n):
    x = np.arange(0, 1+1/(2*n),1/(2*n))
    y = f(x)
    h = 1/n
    res = 0
    for i in range(n):
        res += h * y[2*i+1]
    return res
    
def main():
    x = []
    y = []
    x_2 = []
    y_true = mid(1000000)
    for i in range(1, 1000):
        x.append(1/i)
        y.append(mid(i))
        x_2.append(2/i)
    plt.plot(x, y - y_true)
    plt.plot(x, x_2)
    plt.show()
    print("blue line: 中点則の誤差, green line: 不等式が与える誤差の上限")
    
    
if __name__ == "__main__":
    main()
    
