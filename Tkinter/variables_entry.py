import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Entrada de datos')
ventana.iconbitmap('icono.ico')

# Definimos una variable que podremos modificar posteriormente (set), leer (get)
entrada_var1 = tk.StringVar(value='Valor por defecto')
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL, textvariable=entrada_var1)

entrada1.grid(row=0, column=0)

def enviar():
    # Recuperamos la info a partir de la var asociada a la caja de texto
    boton1.config(text=entrada_var1.get())

    # Para realizar modificaciones utilizamos la variable de texto y el método set
    entrada_var1.set('Cambio...')

    # Recuperamos la info. Dos opciones:
    print(entrada_var1.get())
    print(entrada1.get())

boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()
