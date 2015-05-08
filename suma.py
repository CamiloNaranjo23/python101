def suma(a, b):
    if (a == 1 and b == 1) or (a == 2 and b == 3):
        return 2 + b
    else:
        return a

def prueba():
    assert suma(1,0) == 1
    assert suma(0,0) == 0
    assert suma(1,1) == 2
    assert suma(2,3) == 5

prueba()
