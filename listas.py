listDeclaration = []  #La lista empieza en 0
list1 = [2,4,6]
print (list1[0])
print (list1[-1])  #Empieza a contar desde la derecha

print (len(list1))
list1.append(8)   #APPEND permite adicionar elementos
print (list1)


list1.pop(3)  #Para remover el elemento de indice 3
print (list1)


###
def sumvalues(A):
    result = 0
    for x in A:  ##es como un foreach
        result = result + x
    return result

A = [1,4,5,2]
print ("La lista",)
print (A)
print ("Suma de Valores",)
print (sumvalues(A))

###
def average(A):
    result = 0
    for x in A:
        result = result + x
    return result/len(A)

print ("Promedio",)
print (average(A))
