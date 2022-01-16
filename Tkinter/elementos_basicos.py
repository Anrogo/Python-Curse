# GUI - Graphical User Interface
# Tkinter - TK Interface
# Importamos el módulo de tkinter
import tkinter as tk
# Importamos el módulo del tema también
from tkinter import ttk

# Creamos un objeto usando la clase Tk
ventana = tk.Tk()

# Modificamos el tamaño de la ventana (píxeles ancho por alto)
ventana.geometry('800x600')

# Cambiamos el nombre de la ventana
ventana.title('Hola Mundo')

# Configuramos el icono de la app
ventana.iconbitmap('icono.ico')

# Métodos eventos botones
def evento_click():
    # Cambiamos el texto del botón dinámicamente:
    boton1.config(text='botón presionado')
    print('Ejecución del evento click')

    # Creamos u nuevo botón y lo mostramos
    boton2 = ttk.Button(ventana, text='Nuevo botón')
    boton2.pack()
    
# Creamos un botón (widget), el objeto padre es la ventana
boton1 = ttk.Button(ventana, text='Dar click', command=evento_click)

# Utilizamos el pack layout manager para mostrar los botones y demás elementos
boton1.pack()

# Iniciamos la ventana (esta línea la ejecutamos al final)
ventana.mainloop()
