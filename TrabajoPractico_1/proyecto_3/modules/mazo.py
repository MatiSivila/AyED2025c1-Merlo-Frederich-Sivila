from modules.LDE import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada



class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada()
        self.mazo = self
    
    def __len__(self):
        "Devuelve la cantidad de cartas que hay en el mazo"
        return self.cartas.tamanio
    
    def poner_carta_arriba(self, Carta):
        """Añade una carta al inicio del mazo."""
        self.cartas.agregar_al_inicio(Carta)

    def poner_carta_abajo(self, carta):
        """Añade una carta al final del mazo."""
        self.cartas.agregar_al_final(carta)
   
    def sacar_carta_arriba(self, mostrar=False):
        """Saca la carta del inicio del mazo (parte superior)."""
        if self.cartas.esta_vacia():
            raise DequeEmptyError("El mazo está vacío")
        carta = self.cartas.extraer(0) #Extrae la carta de la posición 0 (parte superior)
        
        if mostrar:
            carta.visible = True #Mostrar la carta si su argumento es True
        return carta

    def sacar_carta_abajo(self):
        """Saca la carta del final del mazo (parte inferior)."""
        if self.cartas.esta_vacia():
            raise DequeEmptyError("El mazo está vacío")
        return self.cartas.extraer() #Extrae la carta del final del mazo
    
    def esta_vacio(self):
        """Verifica si el mazo está vacío y devuelve True en caso de ques si."""
        return self.cartas.esta_vacia()

    def __str__(self):
        return ' '.join(str(carta) for carta in self.cartas)

    @property
    def cabeza(self):
        """Devuelve la carta de la parte superior del mazo."""
        if self.cartas.cabeza:
            return self.cartas.cabeza.dato
        return None
    
    @property
    def cola(self):
        return self.cartas.cola
    
            
     

