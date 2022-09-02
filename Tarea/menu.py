class principal:
    def __init__(self):
        pass
    def menu(self,opciones,titulo):
        print(titulo)
        for opcion in opciones:
            print(opcion)
        opc = input("Elija opcion[1...{}] : " .format(len(opciones)))
        return opc