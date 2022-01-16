import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de componentes')
ventana.iconbitmap('icono.ico')

entrada_var1 = tk.StringVar(value='Valor por defecto')
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)

# Etiqueta (Label)
etiqueta1 = tk.Label(ventana, text='Aquí se mostrará el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)


def enviar():
    # Modificamos el texto del label
    etiqueta1.config(text=entrada_var1.get())

boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)



ventana.mainloop()