import numpy as np



def f(z):
    return z*z*z + (1+1j)*z*z + (-3+2j)*z + (9-3j)

def f_prime(z):
    res = []
    for j in range(len(z)):
        buf = 1
        for l in range(len(z)):
            if l != j:
                buf *= z[j]-z[l]
        res.append(buf)
    return np.array(res)

def phi(z):
    return z - f(z)/f_prime(z)

def prt(z):
    for j in range(len(z)):
        print("z[{}] = {}, f(z[{}]) = {}".format(j, z[j], j, f(z[j])))
    print()

def main():
    R = 5
    beta = -(1+1j)/3
    theta = 2j * np.arange(0, 3, 1) * np.pi / 3
    z = R * np.exp(theta) + beta
    prt(z)
    for i in range(20):
        z = phi(z)
        prt(z)


if __name__ == "__main__":
    main()
