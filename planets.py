def contar_lineas(archivo):
    Archivo = open("planets.csv","r")
    suma = 0
    
    for i in Archivo.xreadlines():
        SUMA = SUMA + len(i)
    print SUMA
    Archivo.close()


def prueba():
    cuenta_esperada = 1919
    cuenta = contar_lineas('planets.csv')
    msg = "Esperaba %s lineas y obtuve %s" % (cuenta_esperada, cuenta)
    assert cuenta == cuenta_esperada, msg

prueba()
