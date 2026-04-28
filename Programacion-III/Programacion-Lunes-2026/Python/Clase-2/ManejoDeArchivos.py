# Ejercicios de Manejo de Archivos
# Declaramos una variable

try:
    archivo = open('prueba.txt', 'w', encoding='utf8') # La W es de write, que significa escribir en inglés
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt. \n')
    archivo.write('Los acentos son importantes para las palabras,\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('Las letras son:\nr read leer, \na apped anexa, \nw write escribe, \nx crea un archivo')
    archivo.write('\nt esta es para texto o text, \nb archivos binarios, \nw+ lee y escribe son iguales r+\n')
    archivo.write('Con esto terminamos.')
except Exception as e:
    print(e)
finally: # Siempre se ejecuta
    archivo.close() # Con esto se cierra el archivo

# archivo.write('Todo quedó perfecto.'): este es un error
