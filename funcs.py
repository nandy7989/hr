def add_up(x, y):
    return x+y

def subtract(x, y):
    return x-y

print(subtract)

def calculate(f, x, y):
    return f(x,y)

print(calculate(add_up, 10,11))
print(calculate(subtract ,10,11))
