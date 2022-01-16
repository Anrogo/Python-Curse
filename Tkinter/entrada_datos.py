import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Entrada de datos')
ventana.iconbitmap('icono.ico')

# WIDTH es la cantidad de caracteres que ocupa la caja de texto, NO los pixeles
# state=tk.DISABLED deshabilita la caja de texto y no permite mostrar la info. Su valor por defecto es state = tk.NORMAL
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL)
# entrada1 = ttk.Entry(ventana, width = 30, justify=tk.CENTER)
entrada1.grid(row=0, column=0)

# Insert para tener un placeholder
entrada1.insert(0, 'Introduce un texto')
entrada1.insert(tk.END, ':')


# entrada1.config(state='readonly')

def enviar():
    print(entrada1.get())
    boton1.config(text=entrada1.get())
    # Eliminamos el contenido de la caja de texto:
    # entrada1.delete(0, tk.END)
    # Seleccionar el texto de la caja
    entrada1.select_range(0,tk.END)
    # Para hacer efectiva al selección del texto:
    entrada1.focus()

# Creamos un botón
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()
