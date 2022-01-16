class ConvertidorTemperatura:

    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 213

    @classmethod
    def c_f(cls, celsius):
        if celsius > cls.MAX_CELSIUS:
            raise ValueError(f'Temperatura C demasiado alta: {celsius}ºC')
        return celsius * 9/5 + 32

    @classmethod
    def f_c(cls, fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f'Temperatura F demasiado alta: {fahrenheit}ºF')
        return (fahrenheit-32) * 5/9

if __name__ == '__main__':
    # Celsius a Fahrenheit
    resultado = ConvertidorTemperatura.c_f(15)
    print(f'15 C a F: {resultado:.2f}')

    # Fahrenheit a Celsius
    resultado = ConvertidorTemperatura.f_c(89)
    print(f'89 F a C: {resultado:.2f}')

    # Si superamos el límite marcado por nuestra constante..
    # Aparece como un error de python, puesto que hemos usado ValueError
    resultado = ConvertidorTemperatura.f_c(220)
    print(f'{resultado}')