#### FUNCIONA EN PYTHON 2, No funciona en Python3 ###
#TKINTER
#Setup Main loop Shutdown
import Tkinter as tk

window = tk.Tk()   #Class constructor for a window object

def saveText():
    cadena1 = textBox.get()
    fx = open("fileForm.txt", "w")
    fx.write(cadena1)
    fx.close()


#Widget Entry, Button, Label
#Declaramos los objetos que queremos en el form
textBox = tk.Entry(window)
button1 = tk.Button(window, text = "Guardar", command = saveText)   #command indica la funcion que se ejecutará al hacer clic en el boton

#Los dibujamos en la aplicación
textBox.pack()  #para adicionar el metodo en la ventana
button1.pack()

window.mainloop()


##Funciones importantes
# Entry.get()
# Entry.delete()
#Parameters Font, width
# Boton
#Parameters
# Text, Width, Command