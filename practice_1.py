

def count_A(x):
    return [value*value for value in range(0, x)]

def count_V(x):
    return x**(1/2) + x**2 / (x**(1/2))

def count_B(x):
    return x**2

def count_Z(x):
    return (x+x**2) / (x-x**2)

def count_C(x):
    return x**(1/2)*x**2

def count_D(x):
    return [value for value in range(0, x, 2)]

def count_F(x):
    return [value**2 for value in range(0, x, 3)]


a = list(map(count_V, [29, 32, 16, 23, 87, 36]))

print(a)
