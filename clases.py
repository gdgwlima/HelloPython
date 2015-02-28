class vehicle:
    wheels = 4    #VARIABLE GLOBAL
    def __init__(self):
        print ("vehicle")
    def calcVelocity(self,x):
        return (3*x+10)

class Car(vehicle):     #Para indicar herencia, pasamos como parametro el nombre de la clase
    def __init__(self):   #Constructor, siempre necesita tener un parámetro
        self.speed = 10     #Para adicionar una variable al objeto
        print ("Constructor de la clase car")
    

examplecar = Car()   #Instancia el objeto y llama al constructor
print (examplecar.speed)
print (examplecar.calcVelocity(20))
print (examplecar.wheels)