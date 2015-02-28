#SINTAX ERROR PARA EL PEDAZO DE CODIGO PARA QUE NO CORRA
#if(1==1)  #sINTAX error

num1 = input("Introduce el numero 1: ")
num2 = input("Introduce el numero 2: ")


try:
    print(int(num1)/int(num2))
except ZeroDivisionError:  #Instrucciones de que hacer si existe un error
    print ("Division entre cero no es permitida")


raise ZeroDivisionError #Es para disparar un error
