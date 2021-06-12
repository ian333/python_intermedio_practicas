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

import os,random,time


def presentacion_juego():

    pass


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

def menu_inicial():
    for i in range(7):
        time.sleep(0.2)
        Imagenes_del_ahorcado(i)
    pass


def run():
    """
    Esta funcion abrira el data.txt 
    """
    contador_intentos_fallidos = 0
    menu_inicial()

    with open("./archivos/data.txt","r", encoding="utf-8") as f:
        words=[i.replace("\n","") for i in f]

    while contador_intentos_fallidos <= 6:
        print(words[random.randint(0,len(words))])

        try:
            letra = int(input("Ingresa un numero"))
        except ValueError:
            print("Debes ingresar un numero")

        Imagenes_del_ahorcado(contador_intentos_fallidos)
        contador_intentos_fallidos += 1


if __name__ == "__main__":

    run()
    pass
