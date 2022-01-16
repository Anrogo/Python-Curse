import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de componentes')
ventana.iconbitmap('icono.ico')

entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER)
entrada1.grid(row=0, column=0)

# Etiqueta (Label)
etiqueta1 = tk.Label(ventana, text='Aquí se mostrará el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)


def enviar():
    # Modificamos el texto del label
    etiqueta1.config(text=entrada1.get())

    # Messagebox (cajas con mensajes)
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Mensaje informativo', mensaje1 + ' Informativo')
        messagebox.showwarning('Esto es un posible problema..', mensaje1 + ' Warning')
        messagebox.showerror('Se ha encontrado un error', mensaje1 + ' Error')


boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()
