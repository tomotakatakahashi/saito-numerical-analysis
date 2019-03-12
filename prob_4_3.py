import numpy as np
import matplotlib.pyplot as plt

def f(t, u):
    return -10*u + t
    
def runge(h):
    u = [10.0]
    u_t = [10.0]
    t = [0]
    step = int(10/h)
    for i in range(step):
        t_now = (i+1)*h
        u_t.append(0.1*t_now - 0.01 + 10.01*np.exp(-10*t_now))
        k1 = f(t[-1], u[-1])
        k2 = f(t[-1]+h/2, u[-1] + h*k1/2)
        k3 = f(t[-1]+h/2, u[-1] + h*k2/2)
        k4 = f(t[-1]+h, u[-1]+h*k3)
        u.append(u[-1]+h*(k1+2*k2+2*k3+k4)/6)
        t.append(t_now)
    return np.array(t), np.array(u), np.array(u_t)
    
def plot(x, y1, y2):
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.show()
    plt.close()

def step(h):
    t, u, u_t = runge(h)
    print("h = {}".format(h))
    plot(t, u, u_t)
            
def main():
    print("Program start.")
    step(1e-2)
    step(1e-1)
    step(0.2)
    step(0.3)
    step(0.5)
    
if __name__=="__main__" :
    main()
