import random

class Quicksort:
    def __init__(self,lista):
        self.lista = lista
    
    def mediana_de_tres(self,lista):
        primero = lista[0]
        ultimo = lista [-1]
        medio =lista[len(lista)//2]

        return sorted([primero, medio, ultimo])[1]
    
    def quicksort(self, lista = None):

        if lista is None:
            lista = self.lista
        
        if len(lista) <= 1:
            return lista
           
        pivot = self.mediana_de_tres(lista)

        menores = [x for x in lista if x < pivot]
        iguales = [x for x in lista if x == pivot]
        mayores = [x for x in lista if x > pivot]

        return self.quicksort(menores) + iguales + self.quicksort(mayores)
    
    def sort(self):
        self.lista = self.quicksort(self.lista)
   
    def display(self):
        if self.lista == lista_comparacion:
            print("Si funciona",self.lista,lista_comparacion)
        else:
            print("No funciona")

lista = [random.randint(10000, 99999) for _ in range(500)]
lista_comparacion = sorted(lista)


metodo_iniciar = Quicksort(lista)


metodo_iniciar.sort()

metodo_iniciar.display()

