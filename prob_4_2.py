import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return y*y + g(t)
    
def g(t):
    return -t/np.sqrt(1-t*t) - 1 + t*t

def euler(h):
    u = [1.0]
    u_t = [1.0]
    t = [0]
    step = int(0.99/h)
    for i in range(step):
        t.append(h*(i+1))
        u_t.append(np.sqrt(1-(h*(i+1))**2))
        u.append(u[i] + f(0.99*i/step, u[i])*(0.99/step))
    return np.array(t), np.array(u), np.array(u_t)



def runge(h):
    u = [1.0]
    u_t = [1.0]
    t = [0]
    step = int(0.99/h)
    for i in range(step):
        u_t.append(np.sqrt(1-((i+1)*h)**2))
        k1 = f(t[-1], u[-1])
        k2 = f(t[-1]+h/2, u[-1] + h*k1/2)
        k3 = f(t[-1]+h/2, u[-1] + h*k2/2)
        k4 = f(t[-1]+h, u[-1]+h*k3)
        u.append(u[-1]+h*(k1+2*k2+2*k3+k4)/6)
        t.append((i+1)*h)
    return np.array(t), np.array(u), np.array(u_t)
    
def plot(x, y1, y2):
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.show()
    plt.close()
    
def main():
    t, u, u_t = euler(2*1e-4)
    e1 = np.abs(u-u_t).max()
    t, u, u_t = euler(1e-4)
    e2 = np.abs(u-u_t).max()
    p = np.log(e1/e2)/np.log(2)
    print("Euler p = {}".format(p))
    plot(t, u, u_t)
    
    t, u, u_t = runge(2*1e-4)
    e1 = np.abs(u - u_t).max()
    t, u, u_t = runge(1e-4)
    e2 = np.abs(u-u_t).max()
    p = np.log(e1/e2)/np.log(2)
    print("Runge p = {}".format(p))
    plot(t, u, u_t)
    
if __name__=="__main__" :
    main()
