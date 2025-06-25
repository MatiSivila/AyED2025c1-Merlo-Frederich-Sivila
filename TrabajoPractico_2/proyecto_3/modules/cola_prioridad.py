from monticulo_binario import MonticuloBinario

class ColaPrioridad:
    def __init__(self):
        self.__monticulo = MonticuloBinario()

    def insertar(self, elemento):
        self.__monticulo.insertar(elemento)

    def atender(self):
        if not self.esta_vacia():
            return self.__monticulo.eliminar_min()
        return None

    def esta_vacia(self):
        return self.__monticulo.esta_vacio()

    def tamano(self):
        return self.__monticulo.tamano