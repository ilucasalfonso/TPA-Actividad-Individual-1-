import sys
correo = str(input('Introduzca su correo electrónico: '))
contra = str(input('Introduzca su contraseña: '))

def menu():
    print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
    print("Ignacio Lucas Alfonso")
    print("         **********MENÚ**********")
    print("             A: Ejercicio A")
    print("             B: Ejercicio B")
    print("             C: Ejercicio C")
    print("             D: Ejercicio D")
    print("             E: Ejercicio E")
    print("             F: Ejercicio F")
    print("             G: Ejercicio G")
    print("             H: Ejercicio H")
    print("             S: Salir")

def A():
    print("Ha seleccionado el ejercicio A, calcular la complejidad de los siguientes fragmentos:")
    while True:
        frag = str(input('¿Qué fragmento quiere? ¿A1? ¿A2? ¿A3? o Salir ')) 
        if frag=='A1' or frag=='a1':
            print ("La complejidad del fragmento A1 es: "'\n')
        elif frag=='A2' or frag=='a2':
            print ("La complejidad del fragmento A2 es: "'\n')
        elif frag=='A3' or frag=='a3':
            print ("La complejidad del fragmento A3 es: O(n)"'\n')
        else:
            break

def B():
    print("Ha seleccionado el ejercicio B, codificar una función que determine si su número de expediente es un número primo y calular su complejidad")
    num=int(input("Dame un número mayor que 1(ej:21829349):   "))
    if num<=1:
        print("El número tiene que ser mayor que 1")
        print()
        B()
    divisor = int(1)
    nd= int(0)
    while num>divisor:
        if num%divisor==0:
            nd=nd+1
        divisor=divisor+1
    if nd<2:
        print("El numero SÍ es primo, tiene ",nd,"divisores")
    else:
        print("El número NO es primo tiene ",nd,"divisores")
    
    if input('Introduzca 1 si quiere repetir, para salir y ver la complejidad escriba cualquier otra cosa.  ')=='1':
        B()
    print ("La complejidad de la función para saber si un número es primo es O(n)." '\n''\n')

def C():
    print("Ha seleccionado el ejercicio C, ")

def D():
    num=str(input("Introduce el número para comprobar si es capicúa:  "))
    lon = int(len(num))
    i=int(0)
    j=int(lon-1)
    res=int
    while int(lon/2)>i:
        if num[i]!=num[j]:
            res=0
        i=i+1
        j=j-1
    if res==0:
        print("NO es capicúa")
    else:
        print("SÍ es capicúa")

    if input('Introduzca 1 si quiere repetir, para salir y ver la complejidad escriba cualquier otra cosa.  ')=='1':
        D()
    print ("La complejidad de la función para saber si un número es capicúa es O()." '\n''\n')

def E():
    print("Ha seleccionado el ejercicio E, Construir una función recursiva que calcule la suma de dos matrices cuadradas de números enteros de orden n. Calcular su complejidad de forma razonada.")
    i=int(0)
    j=int(0)
    j
    n=int(input("Introduzca la dimension de la matriz:  "))
    m1=[n][n]
    m2=[n][n]
    resultado=[n][n]
    while n>i:
        while n>j:
            m1[i][j]=1
            m2[i][j]=1
            j=j+1
        i=i+1
        j=0
    i=0

    print(m2[n][n])


def F():
    print("Ha seleccionado el ejercicio F, ")

def G():
    print("Ha seleccionado el ejercicio G, ")

def H():
    print("Ha seleccionado el ejercicio H, ")
    arr = [0,0,0,0,0,0,0,0] 
    c=int(0)
    print("Introcuce cifra por cifra el número de expediente  ")
    while c<8:
        arr[c]=int(input())
        c=c+1

    for i in range(1, len(arr)): 

        key = arr[i] 

        j = i-1
        while j >= 0 and key < arr[j] : 
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = key 

    for i in range(len(arr)): 
        print ("% d" % arr[i])

    if input('Introduzca 1 si quiere repetir, para salir y ver la complejidad escriba cualquier otra cosa.  ')=='1':
        H()
    print ("La complejidad de la función para ordenar un número por insertion short es O(n^2)." '\n''\n')

def S():
    print("Ha seleccionado la opción salir")
    sys.exit()

while True:
    if correo=='ilucasalfonso@hotmail.com' and contra=='21829349':
        print("Autorizado")
        menu()
        opc = str(input('¿Qué opción quiere?   '))
        if opc=='a' or opc=='A':
            A()
        elif opc=='b' or opc=='B':
            B()
        elif opc=='c' or opc=='C':
            C()
        elif opc=='d' or opc=='D':
            D()
        elif opc=='e' or opc=='E':
            E()
        elif opc=='f' or opc=='F':
            F()
        elif opc=='g' or opc=='G':
            G()
        elif opc=='h' or opc=='H':
            H()
        else :
            S()
        pass
    else:
        print("No autorizado")
        sys.exit()
        pass
