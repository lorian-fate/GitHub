

def count_V(x):
    return x**(1/2) + x**2 / (x**(1/2))

def count_B(x):
    return x**2

def count_Z(x):
    return (x+x**2) / (x-x**2)

a = list(map(count_V, [29, 32, 16, 23, 87, 36]))

print(a)