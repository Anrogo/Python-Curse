import tkinter as tk
from tkinter import ttk, messagebox

# Ventana  principal
ventana = tk.Tk()
ventana.geometry('300x130')
ventana.title('Login')
ventana.iconbitmap('../icono.ico')
ventana.resizable(0, 0)


# Configuración del grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

userLabel = tk.Label(ventana, text='Usuario:')
userLabel.grid(row=0, column=0, sticky=tk.E, padx=5, pady=15)
passLabel = tk.Label(ventana, text='Password:')
passLabel.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

userCampo = ttk.Entry(ventana, width=30)
userCampo.grid(row=0, column=1, sticky=tk.W, padx=5, pady=15)
passCampo = ttk.Entry(ventana, width=30, show='*')
passCampo.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)


def login():
    usuario = userCampo.get()
    password = passCampo.get()
    if usuario and password:
        messagebox.showinfo('Datos Login', f'Usuario: {usuario}, Password: {password}')
    else:
        messagebox.showwarning('Datos Login', 'Completa los campos de usuario y contraseña para poder acceder, gracias.')


loginBtn = ttk.Button(ventana, text='Login', command=login)
loginBtn.grid(row=3, column=0, columnspan=2, sticky=tk.S, pady=10)

ventana.mainloop()
