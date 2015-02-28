x = 20
#usamos def = define nombre de funcion: [ indentado ]
def calculate():
    print(x/10)

calculate()
x = 30
calculate()
x = 85
calculate()

###### PARAMETROS #######
# SCOPE: las variables dentro de las funciones, solo existen dentro de las funciones, no fuera
def tri_area(base, height):
    area = (base * height)/2
    return area

print(tri_area(4,5))
print(tri_area(14,56))

### scope
#ERRORES
#def func():
#   x = x+1
#print x+1
#y = 20
#def func2():
#   print y = y+1
#
