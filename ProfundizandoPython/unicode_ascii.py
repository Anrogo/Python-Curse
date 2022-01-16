# Juego de caracteres unicode:
# Espacio en blanco: \u0020
print('Hola\u0020Mundo')
# La notación habitual
print('Notación simple:', '\u0041')
# Una forma más larga de expresar lo mismo
print('Notación extendidda:','\U00000041')
# Hexadecimal \x:
print('Notación hexadecimal:','\x41')

print('Corazón:','\u2665')
print('Cara sonriendo','\U0001f600')
print('Serpiente:','\U0001F40D')

# Juego de caracteres ASCII
caracter = chr(65)
print('A mayúscula:',caracter)
caracter = chr(64)
print('Símbolo @:',caracter)
caracter = chr(97)
print('A minúscula:',caracter)