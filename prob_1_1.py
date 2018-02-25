

def newton(b, x0):
    x = x0
    for i in range(10):
        x = phi(x, b)
        print("i = {}, x = {}".format(i, x))
        

def phi(x, b):
    return x - f(x, b)/f_prime(x, b)

def f(x, b):
    return x**3 - b

def f_prime(x, b):
    return 3*(x**2)


if __name__ == '__main__':
    import sys
    newton(b = float(sys.argv[1]), x0 = float(sys.argv[2]))
    
