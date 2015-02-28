file_object = open("file1.txt", "w") #Creando un archivo para escritura
                                     #Si el archivo no existe se creara
phrase = "Esta sera la frase que se escribira en el archivo"

file_object.write(phrase)  #Escribiendo la variable en nuestro archivo
file_object.close()

#######################
file_object2 = open("file1.txt", "r")  #Abriendo el archivo para lectura
frase = file_object2.read()
file_object2.close()
print(frase)

######################
#Almacenando el nombre del usuario
file_object3 = open("username.txt","a")  #A de append 
userName = input("Enter your name")

file_object3.write(userName+"\n")  ### El backslash hace que se concatene
file_object3.close()

file_object4 = open("username.txt","r")
userList = file_object4.read()
print("User List")
print(userList)
#file_object4.close()
