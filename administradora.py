from particula import Particula #importo la clase "Particula" del archivo "particula.py"
import json
from algoritmos import puntos_mas_cercanos #Importo el metodo "puntos_mas_cercanos" del archivo "algoritmo.py"
#Clase que adiministra las particulas
class Administradora:
    def __init__(self):
        self.__particulas = [] #Lista que contendra las particulas y sus respectivas caracteristicas
        
    def agregar_final(self,particula:Particula):
        self.__particulas.append(particula) #Agregar al final de la lista __particulas una particula
        
    def agregar_inicio(self,particula:Particula):
        self.__particulas.insert(0,particula)#Agregar al inicio de la lista __particulas una particula
        
    def mostrar(self): #Imprimir las particulas que haya en la lista __particulas
        for particula in self.__particulas:
            print(particula)
            
    def __str__(self):
        return "".join(
            str(particula) for particula in self.__particulas 
            ) 

    def __len__(self):
        return (len(self.__particulas))
    
    
    def __iter__(self):
        self.cont = 0
        
        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration

    def guardar(self,ubiacion):
        try:
            with open(ubiacion,'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista,archivo, indent = 5)
            return
        except:
            return 0
             #json.dump()

    def abrir(self,ubicacion):
        try:
            with open(ubicacion,'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula)for particula in lista]
            return 1
        except:
            return 0
        
    def ordenarID(self):
        return self.__particulas.sort(key=lambda particula: particula.id)
    
    
    def ordenarDistancia(self):
        return self.__particulas.sort(key=lambda particula: particula.distancia)
    
    ########################################################################################################
    def PC(self):
        par = [] #lista para guardar puntos
        par2 = [] #lista para guardar puntos
        for particula in self.__particulas:#por cada particula en la lista de particulas
            x1 = particula.origen_x#guardo la coordenada en x del primer punto 
            y1 = particula.origen_y#guardo la coordenada en y del primer punto
            
            x2 = particula.destino_x#guardo la coordenada en x del segundo punto
            y2 = particula.destino_y#guardo la coordenada en y del segundo punto
            
            x = (x1,y1)#guardo en la variable x las coordenadas del primer punto
            y = (x2,y2)#guardo en la variable y las coordenadas del segundo punto
            
            par2.append(y)#agrego el segundo punto a la segunda lista
            par.append(x)#agrego el primer punto a la segunda lista
            
        lista = par2 + par   #junto las lista para que sea una sola lista de puntos
        return puntos_mas_cercanos(lista)#Retorno el resultado de la llama a la funcion de puntos mas cercanos de la lista que contiene todos los puntos
    ###############################################################################################################