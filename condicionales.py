num1 = input("Enter a number")

if int(num1) < 10:
    print("Numero menor a 10")
else:
    print("Numero Mayor a 10")
    
### ejemplo de una funcion con formula

def funcionejemplo(a,b):
    if b > 0:
        result = (a+b)/b
        return result
    else:
        print("error no division by 0")
        

print(funcionejemplo(4,0))
print("result2")
print(funcionejemplo(5,3))
