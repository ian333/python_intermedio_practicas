###Lista de los primeros 100 numeros naturales al cuadrado
def run():
    #numeros_al_cuadrado=[]

    #for i in range (0,101):
    #    if i**2 % 3 != 0:
    #        numeros_al_cuadrado.append(i**2)
    numeros_al_cuadrado=[i for i in range (1,100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0 )]
    
    print ( numeros_al_cuadrado )

if __name__ == '__main__' :
    run()
