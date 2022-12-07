import sys

archivo = open("contador.txt","a+")
archivo.seek(0)

contador = archivo.readline()

if len(contador)==0:
    datos = "0"
    archivo.write(datos)

else:
    try:
        datos = int(contador)
        if len(sys.argv)==2:
            if sys.argv[1]=="inc":
                datos +=1

            elif sys.argv[1]=="dec":
                datos -=1
        archivo = open("contador.txt","w")
        archivo.write(str(datos))

    except IOError:
        print("Error: fichero corrupto.")

archivo.close()



