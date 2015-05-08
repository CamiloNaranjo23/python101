def suma(a, b):
    return int(a)+int(b)
 
def prueba():
    assert suma(1,0) == 1
    assert suma(0,0) == 0
    assert suma(1,1) == 2
    assert suma(2,3) == 5
    assert suma(134124123,432434) == 134556557
    assert suma('2', '2') == 4
    

prueba()
