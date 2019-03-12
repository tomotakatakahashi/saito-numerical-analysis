import numpy as np
import matplotlib.pyplot as plt

def f(t, u):
    return np.cos(u)
    
def kutta3(h):
    u = [0]
    u_t = [0]
    t = [0]
    step = int(1/h)
    for i in range(step):
        k1 = f(t[-1], u[-1])
        k2 = f(t[-1]+h/2, u[-1] + h*k1/2)
        k3 = f(t[-1]+h, u[-1] + h*(-k1+2*k2))
        u.append(u[-1]+h*(k1+4*k2+k3)/6)
        t.append((i+1)*h)
        u_t.append(np.arcsin((np.exp(2*t[-1]) - 1)/(np.exp(2*t[-1]) +1)))
    return np.array(t), np.array(u), np.array(u_t)

def heun3(h):
    u = [0]
    u_t = [0]
    t = [0]
    step = int(1/h)
    for i in range(step):
        k1 = f(t[-1], u[-1])
        k2 = f(t[-1] + h/4, u[-1] + h*k1/4)
        k3 = f(t[-1] + 2*h/3, u[-1] + h*(-2*k1+8*k2)/9)
        u.append(u[-1] + h*(k1+3*k3)/4)
        t.append((i+1)*h)
        u_t.append(np.arcsin((np.exp(2*t[-1]) - 1)/ (np.exp(2*t[-1]) + 1)))
    return np.array(t), np.array(u), np.array(u_t)

def plot(x, y1, y2):
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.show()
    plt.close()

def main():
    print("Program start.")
    h_list = [1e-2, 5e-3, 1e-3, 5e-4, 1e-4]
    p_heun = []
    p_kutta = []
    
    for h in h_list:
        t, u, u_t = heun3(h)
        e = np.abs(u-u_t).max()
        p_heun.append(e)
        t, u, u_t = kutta3(h)
        e = np.abs(u-u_t).max()
        p_kutta.append(e)
    plt.loglog(h_list, p_heun)
    plt.loglog(h_list, p_kutta)
    plt.show()

    
if __name__=="__main__" :
    main()
