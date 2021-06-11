def read():
    """
    esta es la funcion para leer
    """
    number = []

    with open("./archivos/archivo.txt","r" ,encoding="utf-8" ) as f:
        for line in f:
            number.append(int(line))
    
    print(number)
        
    

def write():
    """
    esta es la funcion para escribir
    """
    names = ["Facundo","Cesar","Rocío"]
    with open("./archivos/names.txt","a") as f:
        for name in names:
            f.write(name)
            f.write(" \n")

        print()

def run():
    """
    esta es la funcion principal 
    """
    
    write()


if __name__ == "__main__":
    run()

