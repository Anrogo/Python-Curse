import tkinter as tk
from tkinter import ttk, messagebox

class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()

        # Ventana  principal
        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('../icono.ico')
        self.resizable(0, 0)

        # Configuración del grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self._crear_componentes()

    def _crear_componentes(self):

        # Usuario
        userLabel = tk.Label(self, text='Usuario:')
        userLabel.grid(row=0, column=0, sticky=tk.E, padx=5, pady=15)
        self.userCampo = ttk.Entry(self, width=30)
        self.userCampo.grid(row=0, column=1, sticky=tk.W, padx=5, pady=15)
        # Password
        passLabel = tk.Label(self, text='Password:')
        passLabel.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.passCampo = ttk.Entry(self, width=30, show='*')
        self.passCampo.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        # Btn Login
        loginBtn = ttk.Button(self, text='Login', command=self._login)
        loginBtn.grid(row=3, column=0, columnspan=2, sticky=tk.S, pady=10)


    def _login(self):
        usuario = self.userCampo.get()
        password = self.passCampo.get()
        if usuario and password:
            messagebox.showinfo('Datos Login', f'Usuario: {usuario}, Password: {password}')
        else:
            messagebox.showwarning('Datos Login', 'Completa los campos de usuario y contraseña para poder acceder, gracias.')



# Ejecutamos el código únicamente desde este mismo archivo/clase:
if __name__ == '__main__':
    login_ventana = LoginVentana()
    login_ventana.mainloop()

