import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid 2')
ventana.iconbitmap('icono.ico')

# Configurar el grid
ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

# Métodos de los eventos
def evento():
    boton1.config(text="Botón presionado")

def evento4():
    # Cambios que se pueden realizar en botones creados con tk
    boton4.config(text='Botón 4 presionado', background='blue', fg='white', relief=tk.GROOVE)

# Definimos los botones
boton1 = ttk.Button(ventana, text='Boton 1', command=evento)
boton1.grid(row=0,column=0,sticky='NSWE', padx=40, pady=20, ipadx=20, ipady=10, columnspan=2)
# boton1.grid(row=0,column=0,sticky='NSWE', padx=40, pady=20, ipadx=20, ipady=10, columnspan=2, rowspan=2)

# Sticky funciona como las coordenadas: N(Arriba), E(derecha), S(abajo), W(izquierdda)
boton2 = ttk.Button(ventana, text='Boton 2')
boton2.grid(row=1,column=0,sticky='NSWE')

# boton3 = ttk.Button(ventana, text='Boton 3')
# boton3.grid(row=0,column=1,sticky='NSWE')

boton4 = tk.Button(ventana, text='Boton 4', command=evento4)
boton4.grid(row=1,column=1,sticky='NSWE', padx=40, pady=20)

ventana.mainloop()
