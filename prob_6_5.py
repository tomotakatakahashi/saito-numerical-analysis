import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return 3*y - 4 * np.exp(-t)

def euler():
    u = [1.0]
    u_t = [1.0]
    t = [0]
    T = 5
    for i in range(step):
        t.append(T*(i+1)/step)
        u_t.append(np.exp(-t[-1]))
        u.append(u[i] + f(T*i/step, u[i])*(T/step))
    plt.plot(t, u)
    plt.plot(t, u_t)
    plt.show()



def runge():
    u = [1.0]
    u_t = [1.0]
    t = [0]
    T = 5
    h = T/step
    for i in range(step):
        u_t.append(np.exp(-t[-1]))
        k1 = f(t[-1], u[-1])
        k2 = f(t[-1]+h/2, u[-1] + h*k1/2)
        k3 = f(t[-1]+h/2, u[-1] + h*k2/2)
        k4 = f(t[-1]+h, u[-1]+h*k3)
        t.append(T*(i+1)/step)
        u.append(u[-1]+h*(k1+2*k2+2*k3+k4)/6)
    plt.plot(t, u)
    plt.plot(t, u_t)
    plt.show()
    
def main():
    euler()
    runge()


    
    
    
if __name__=="__main__" :
    step = 100000
    print(0)
    main()
