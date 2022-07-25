import tkinter as tk
from tkinter import messagebox


class Calculadora(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('320x330+120+600')
        self.resizable(0, 0)
        self.title('Calculadora')
        self.iconbitmap('../calculadora.ico')

        # Atributos de clase
        self.expresion = ''

        # Caja de texto (input)
        self.entrada = None

        # StringVar que utilizamos para obtener o actualizar el valor del input
        self.entrada_texto = tk.StringVar()

        # Método para crear los componentes
        self._creacion_componentes()

    # Métodos de clase
    # 1 - Método para crear los componentes
    def _creacion_componentes(self):
        # Creamos un frame para la caja de texto
        entrada_frame = tk.Frame(self, width=310, height=50)
        entrada_frame.pack(side=tk.TOP)

        # Caja de texto
        entrada = tk.Entry(entrada_frame,
                           font=('arial', 18, 'bold'),
                           textvariable=self.entrada_texto,
                           width=24,
                           justify=tk.RIGHT)
        entrada.grid(row=0, column=0, sticky=tk.W, ipady=10)

        # Creamos otro frame para la parte inferior
        botones_frame = tk.Frame(self, width=310, height=450, bg='#8F8F8F')
        botones_frame.pack()

        # Primer renglón
        # Botón limpiar
        boton_limpiar = tk.Button(botones_frame,
                                  text='C',
                                  width=32,
                                  height=3,
                                  bd=0,
                                  bg='#E8E8E8',
                                  cursor='hand2',
                                  command=self._evento_limpiar)
        boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        # Botón división
        tk.Button(botones_frame,
                  text='/',
                  width=10,
                  height=3,
                  bd=0,
                  bg='#E8E8E8',
                  cursor='hand2',
                  command=lambda: self._evento_click('/')) \
            .grid(row=0,
                  column=3,
                  padx=1,
                  pady=1)

        # Segundo renglón
        # Botón 7
        tk.Button(botones_frame,
                  text='7',
                  width=10,
                  height=3,
                  bd=0,
                  bg='#FFF',
                  cursor='hand2',
                  command=lambda: self._evento_click(7)) \
            .grid(row=1,
                  column=0,
                  padx=1,
                  pady=1)

        # Botón 8
        tk.Button(botones_frame,
                  text='8',
                  width=10,
                  height=3,
                  bd=0,
                  bg='#FFF',
                  cursor='hand2',
                  command=lambda: self._evento_click(8)) \
            .grid(row=1,
                  column=1,
                  padx=1,
                  pady=1)

        # Botón 9
        tk.Button(botones_frame,
                  text='9',
                  width=10,
                  height=3,
                  bd=0,
                  bg='#FFF',
                  cursor='hand2',
                  command=lambda: self._evento_click(9)) \
            .grid(row=1,
                  column=2,
                  padx=1,
                  pady=1)
        # Botón X
        tk.Button(botones_frame,
                  text='X',
                  width=10,
                  height=3,
                  bd=0,
                  bg='#E8E8E8',
                  cursor='hand2',
                  command=lambda: self._evento_click('*')) \
            .grid(row=1,
                  column=3,
                  padx=1,
                  pady=1)
        # Tercer renglón
        # Botón 4
        tk.Button(botones_frame,
                  text='4',
                  width=10,
                  height=3,
                  bd=0,
                  bg='#FFF',
                  cursor='hand2',
                  command=lambda: self._evento_click(4)) \
            .grid(row=2,
                  column=0,
                  padx=1,
                  pady=1)

        # Botón 5
        tk.Button(botones_frame,
                  text='5',
                  width=10,
                  height=3,
                  bd=0,
                  bg='#FFF',
                  cursor='hand2',
                  command=lambda: self._evento_click(5)) \
            .grid(row=2,
                  column=1,
                  padx=1,
                  pady=1)

        # Botón 6
        tk.Button(botones_frame,
                  text='6',
                  width=10,
                  height=3,
                  bd=0,
                  bg='#FFF',
                  cursor='hand2',
                  command=lambda: self._evento_click(6)) \
            .grid(row=2,
                  column=2,
                  padx=1,
                  pady=1)

        # Botón -
        tk.Button(botones_frame,
                  text='-',
                  width=10,
                  height=3,
                  bd=0,
                  bg='#E8E8E8',
                  cursor='hand2',
                  command=lambda: self._evento_click('-')) \
            .grid(row=2,
                  column=3,
                  padx=1,
                  pady=1)

        # Cuarto renglón
        # Botón 1
        tk.Button(botones_frame,
                  text='1',
                  width=10,
                  height=3,
                  bd=0,
                  bg='#FFF',
                  cursor='hand2',
                  command=lambda: self._evento_click(1)) \
            .grid(row=3,
                  column=0,
                  padx=1,
                  pady=1)

        # Botón 2
        tk.Button(botones_frame,
                  text='2',
                  width=10,
                  height=3,
                  bd=0,
                  bg='#FFF',
                  cursor='hand2',
                  command=lambda: self._evento_click(2)) \
            .grid(row=3,
                  column=1,
                  padx=1,
                  pady=1)

        # Botón 3
        tk.Button(botones_frame,
                  text='3',
                  width=10,
                  height=3,
                  bd=0,
                  bg='#FFF',
                  cursor='hand2',
                  command=lambda: self._evento_click(3)) \
            .grid(row=3,
                  column=2,
                  padx=1,
                  pady=1)

        # Quinto renglón
        # Botón +
        tk.Button(botones_frame,
                  text='+',
                  width=10,
                  height=3,
                  bd=0,
                  bg='#E8E8E8',
                  cursor='hand2',
                  command=lambda: self._evento_click('+')) \
            .grid(row=3,
                  column=3,
                  padx=1,
                  pady=1)

        # Botón 0
        tk.Button(botones_frame,
                  text='0',
                  width=21,
                  height=3,
                  bd=0,
                  bg='#FFF',
                  cursor='hand2',
                  command=lambda: self._evento_click(0)) \
            .grid(row=4,
                  column=0,
                  columnspan=2,
                  padx=1,
                  pady=1)

        # Botón punto
        tk.Button(botones_frame,
                  text='.',
                  width=10,
                  height=3,
                  bd=0,
                  bg='#E8E8E8',
                  cursor='hand2',
                  command=lambda: self._evento_click('.')) \
            .grid(row=4,
                  column=2,
                  padx=1,
                  pady=1)

        # Botón =
        tk.Button(botones_frame,
                  text='=',
                  width=10,
                  height=3,
                  bd=0,
                  bg='#E8E8E8',
                  cursor='hand2',
                  command=self._evento_evaluar) \
            .grid(row=4,
                  column=3,
                  padx=1,
                  pady=1)

    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def _evento_click(self, elemento):
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)

    def _evento_evaluar(self):
        # eval evalúa la expresión str como una expresión aritmética
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrió un error: {e}')
            self.entrada_texto.set('')
        if self.entrada_texto:
            self.expresion = self.entrada_texto.get()
        else:
            self.expresion = ''


if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()
