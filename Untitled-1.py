
class Alumno :
# Creamos el constructor y le pasamos los parametros(datos o atributos)
    def __init__ (self, leg, nom, nroDni, date):    
        self.legajo = leg
        self.nombre = nom
        self.dni = nroDni
        self.fecha = date
        
# Creamos el metodo o funcion para ingresar datos      
    def mostrar_datos (self):                      
        self.legajo = int(input(' Ingrese el legajo: '))
        self.nombre = input('Ingrese el nombre: ')
        self.dni = int(input('Ingrese el dni'))
   # print ('datos ingresados correctamente')
    
    def ingreso_notas (self):
        rta = 's'
        while (True):
            if (rta == 's' or rta == 'S'):
                nota = input('ingrese nota: ')
                rta = input('Desea seguir? s/n')
                nota = int(nota)
                self.nota.append(nota)
            else :
                break
        print(self.notas)
        
   # def promedio()
                
                
        
# Usamos encapsulamiento y le pasamos la clase al objeto alu1
alu1 = Alumno()
    
# Llamamos al metodo
alu1.mostrar_datos() 
alu1.ingreso_notas()                               


class Vehiculo : 
    def __init__ (self, marca, modelo, color, transmision):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.transmision = transmision
    
    def arrancar(self):
        print ('Estoy andando')
    
    def frenar(self):
        print('Estoy frenando')
        
    
    
 # herencia 
 
#class Auto(Vehiculo):
#    def arrancar(self):