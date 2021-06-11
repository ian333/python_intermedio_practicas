# El juego debe implementar list_comprehesions
# manejo de errores
# manejo de archivos
# Ayudas y pistas
# investiga la funcion enumerate
# el metodo get de los diccionarios
# la sentencia os.system ("cls") windows o os.system ("clear")
# Añade un sistema de puntos
# mejora la interfaz
# dibuja al ahorcado en cada jugada con codigo ascii
#

import os

def Imagenes_del_ahorcado(intento):
    """
    Esta funcion muestra al ahorcado en codigo ascii
    """
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    
    os.system("clear")
    print(HANGMANPICS[intento])



def run():
    """
    docstring
    """
    contador_intentos_fallidos=0
    while contador_intentos_fallidos<=5:
       
        letra = int(input("Ingresa un numero"))
        Imagenes_del_ahorcado(contador_intentos_fallidos)
        contador_intentos_fallidos+=1


if __name__ == "__main__":

    run()
    pass
