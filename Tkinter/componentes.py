import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Componentes')
ventana.iconbitmap('icono.ico')

def crear_componentes_tab1(tabulador):
    # Agregar una etiqueta
    etiqueta1 = ttk.Label(tabulador, text='Nombre:')
    etiqueta1.grid(row=0, column=0, sticky=tk.E)
    entrada1 = ttk.Entry(tabulador, width=30)
    entrada1.grid(row=0, column=1, padx=5, pady=5)

    # Agregamos un botón
    def enviar():
        if entrada1.get():
            messagebox.showinfo('Mensaje', f'Nombre: {entrada1.get()}')

    boton1 = ttk.Button(tabulador, text='Enviar', command=enviar)
    boton1.grid(row=1, column=0, columnspan=2)

def crear_componentes_tab2(tabulador):
    contenido = 'Este es mi texto con el contenido'
    # Creamos el componente de scroll
    scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD)
    scroll.insert(tk.INSERT, contenido)
    # Mostramos el contenido
    scroll.grid(row=0, column=0, padx=5, pady=5)

def crear_componentes_tab3(tabulador):
    # Creamos una lista usando data list comprehensions
    datos = [x+1 for x in range(100,110)]
    combobox = ttk.Combobox(tabulador, width=15, values=datos)
    combobox.grid(row=0,column=0, padx=10, pady=10)

    # Seleccionamos un elemento por default a mostrar
    combobox.current(0)

    # Agregamos un botón para saber que opción seleccionó el usuario
    def mostrar_valor():
        messagebox.showinfo('Valor seleccionado', f'Valor seleccionado: {combobox.get()}')
    boton1 = ttk.Button(tabulador, text='Mostrar valor seleccionado', command=mostrar_valor)
    boton1.grid(row=0, column=1)

def crear_componentes_tab4(tabulador):
    imagen = tk.PhotoImage(file='python-logo.png')
    def mostrar_titulo():
        messagebox.showinfo('Más info imagen', f'Nombre imagen: {imagen.cget("file")}')
    boton_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)
    boton_imagen.grid(row=0,column=0, padx=5)

def crear_tabs():
    # Creamos un tab control, para ello usamos la clase Notebook
    control_tabulador = ttk.Notebook(ventana)

    # Agregamos un marco (o frame) para insertar dentro del tabulador y organizar sus elementos
    tabulador1 = ttk.Frame(control_tabulador)

    # Agregamos el tabulador al control de tabuladores
    control_tabulador.add(tabulador1, text='Tabulador 1')
    # Para mostrar el tabulador y darle el relleno:
    control_tabulador.pack(fill='both')

    # Creamos los componentes del tabulador 1
    crear_componentes_tab1(tabulador1)

    # Creamos un segundo tabulador. Que gracias a LabelFrame tiene un título al entrar
    tabulador2 = ttk.LabelFrame(control_tabulador, text='Contenido')
    control_tabulador.add(tabulador2, text='Tabulador 2')
    
    # Creamos los componentes del segundo tabulador
    crear_componentes_tab2(tabulador2)

    # Crear tercer tabulador:
    tabulador3 = ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador3, text='Tabulador 3')

    crear_componentes_tab3(tabulador3)

    # Tabulador 4
    tabulador4 = ttk.LabelFrame(control_tabulador, text='Imagen')
    control_tabulador.add(tabulador4, text='Tabulador 4')

    crear_componentes_tab4(tabulador4)

crear_tabs()

ventana.mainloop()