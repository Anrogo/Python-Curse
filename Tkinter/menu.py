import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de componentes')
ventana.iconbitmap('icono.ico')

entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER)
entrada1.grid(row=0, column=0)

etiqueta1 = tk.Label(ventana, text='Aquí se mostrará el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)


def enviar():
    etiqueta1.config(text=entrada1.get())

    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Mensaje informativo', mensaje1 + ' Informativo')


def salir():
    ventana.quit()
    ventana.destroy()
    print('Salimos..')
    sys.exit()


def crear_menu():
    # Configurar el menú principal
    menu_principal = Menu(ventana)
    menu_principal.configure(background='green', fg='white')
    # tearoff = False. El menú no se separá de nuestra inferfaz. En caso contrario, al pincharlo se abre en otra
    # ventana a parte
    submenu_archivo = Menu(menu_principal, tearoff=0)
    # Añadimos una nueva opción al menú de archivo
    submenu_archivo.add_command(label='Nuevo')
    # Separador entre opciones del menu:
    submenu_archivo.add_separator()
    # Agregamos la opción de salir
    submenu_archivo.add_command(label='Salir', command=salir)
    # Agregamos el submenu al menú principal en forma de cascada
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
    # Submenu ayuda
    submenu_ayuda = Menu(menu_principal, tearoff=0)
    submenu_ayuda.add_command(label='Acerca de', )
    submenu_ayuda.add_command(label='Créditos')
    submenu_ayuda.add_command(label='Obtener actualización')
    menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')

    # Mostrar el menu, con todas las opciones agregadas, en la ventana principal
    ventana.config(menu=menu_principal)


boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

crear_menu()

ventana.mainloop()
