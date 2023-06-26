def cargar_alumno(nom,apell,dni,notas):
    n1,n2,n3,n4,n5,n6=notas
    prom=sum(notas)/6
    datos=open("lista.csv","a")
    datos.write(f'{nom};{apell};{dni};{n1};{n2};{n3};{n4};{n5};{n6};{prom}\n')
    datos.close()

def mostrar_alumnos():
    datos=open("lista.csv","r")
    texto=datos.read()
    print(texto)
    datos.close()

def buscar_alumno(nombre):
    datos=open("lista.csv","r")
    items=datos.readline()
    c=0
    for linea in datos.readlines():
        if nombre in linea:
            c+=1
    datos.close()
    if c==0:
        print(f'El alumno no forma parte de la lista')
    else:
        datos=open("lista.csv","r")
        items=datos.readline()
        for linea in datos.readlines():
            if nombre in linea:
                datos_separados=linea.split(";")
                print("DATOS ALUMNO: ")
                print(f'Nombre y apellido: {datos_separados[0]}, {datos_separados[1]}')
                print(f'DNI: {datos_separados[2]}')
                notas=datos_separados[3:9]
                n=1
                for x in notas:
                    print(f'Nota N°{n}= {x}')
                print(f'Promedio: {datos_separados[9]}')
        datos.close()

def aprobado():
    datos=open('lista.csv','r')
    _=datos.readline()
    for linea in datos.readlines():
        datos_separados=linea.split(";")
        nombre=datos_separados[0]
        apellido=datos_separados[1]
        promedio=float(datos_separados[9])
        if promedio>=6:
            print(f'{nombre} {apellido}: APROBADO')
        else:
            print(f'{nombre} {apellido}: DESAPROBADO')

datos=open("lista.csv","r")
_=datos.readline()
c=0
while True:
    print("1--> Cargar un estudiante a la base de datos")
    print("2--> Mostrar la lista de estudiantes")
    print("3--> Mostrar los estudiantes aprobados/desaprobados")
    print("4--> Buscar a un estudiante en la lista")
    print("5--> SALIR\n")
    opc=int(input("Ingrese la opcion: "))
    print("\n")
    if opc==1:
        nombre=input("Nombre del alumno: ")
        apellido=input("Apellido del alumno: ")
        docu=int(input("DNI: "))
        docu=str(docu)
        repite=0
        for linea in datos.readlines():
            if docu in linea:
                repite=1
        if repite==0:
            lista_notas=[]
            for x in range(6):
                nota=int(input(f'Nota N°{x+1}: '))
                lista_notas.append(nota)
            cargar_alumno(nombre,apellido,docu,lista_notas)
            c=1
        else:
            print(f'ERROR EL DNI {docu} YA FUE CARGADO EN LA LISTA')
        print("\n")
    elif opc==2:
        if c==1:
            mostrar_alumnos()
        else:
            print("TODAVIA NO SE HAN CARGADO ALUMNOS")
        print("\n")
    elif opc==3:
        aprobado()
        print("\n")
    elif opc==4:
        while True:
            print("1--> Buscar por nombre")
            print("2--> Buscar por apellido")
            print("3--> Buscar por DNI")
            print("4--> CANCELAR BUSQUEDA\n")
            opci=int(input("Ingrese la opcion de busqueda: "))
            print("\n")
            if opci==1:
                nombre=input("Ingrese el nombre del alumno: ")
                buscar_alumno(nombre)
                print("\n")
                break
            elif opci==2:
                apellido=input("Ingrese el apellido del alumno: ")
                buscar_alumno(apellido)
                print("\n")
                break
            elif opci==3:
                dni=input("Ingrese el DNI: ")
                print("\n")
                buscar_alumno(dni)
                print("\n")
                break
            elif opci==4:
                break
            else:
                print("OPCION NO VALIDA\n")
        print("\n")
    elif opc==5:
        break
    else:
        print("Opcion no valida\n")
datos.close()