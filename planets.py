def contar_lineas(archivo):
    """Contador de lineas usando read()
    """
    return 0


def prueba():
    cuenta_esperada = 1920
    cuenta = contar_lineas('planets.csv')
    msg = "Esperaba %s lineas y obtuve %s" % (cuenta_esperada, cuenta)
    assert cuenta == cuenta_esperada, msg

prueba()
