def contar_lineas(archivo):
    return sum(1 for line in open(archivo))-1
    
def prueba():
    cuenta_esperada = 1919
    cuenta = contar_lineas('planets.csv')
    msg = "Esperaba %s lineas y obtuve %s" % (cuenta_esperada, cuenta)
    assert cuenta == cuenta_esperada, msg

prueba()
