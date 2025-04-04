# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
import random
class burbuja:
    def __init__(self,lista):
        self.lista = lista
    
    def sort(self):
        n = len(self.lista)
        for i in range (0,n -1):
             for j in range (n - 1 - i):
                 if self.lista[j] > self.lista[j + 1]:
                     self.lista[j],self.lista[j + 1] = self.lista[j + 1],self.lista[j]
        return self.lista
  
    def display(self):
        if self.lista == lista_comparacion:
            print("El metodo funciona correctamente")
        else:
            print("No anda")

#Lista y Lista ordenada se generaran y seran iguales para comparar si con un sorted se ordenan correctamente o no 
lista = [random.randint(10000, 99999) for _ in range(500)]
lista_comparacion = sorted(lista)

ord_burbuja = burbuja(lista)

ord_burbuja.sort()

ord_burbuja.display()




