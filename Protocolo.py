
import sys

lineamientos = []
nos = []

while True:
    print("""
=========================
    CREA TU PROTOCOLO 
=========================
""")
    eleccion = input("""
1 - Introducir lineamiento
2 - Mostrar protocolo
3 - Borrar una linea
4 - Borrar el protocolo
5 - Salir
Seleccione: """)
    if eleccion == "1":
        lineamiento = input("Lineamiento: ")
        no = float(input("Número de lineamiento: "))
        lineamientos.append(lineamiento)
        nos.append(no)

    elif eleccion == "2":
        if len(lineamientos) <= 0:
            print("No hay lineamientos en el protocolo")
            continue

        print("+----------------------------------------+----------+")
        print("|Linieamientos del protocolo             |No.       |")
        print("+----------------------------------------+----------+")
        indice = 0
        total = 0
        while indice < len(lineamientos):
            lineamiento = lineamientos[indice]
            no = nos[indice]
            print("|{:<40}|{:>10.2}|".format(
                lineamiento, no ))
            print("+----------------------------------------+----------+")

            indice += 1

    elif eleccion == "3":
        nombre_lineamiento = input("Lineamiento que se elimina: ")
        if nombre_lineamiento in lineamientos:
            indice = lineamientos.index(nombre_lineamiento)
            del lineamientos[indice]
            del nos[indice]
            print(f"Se elimina {nombre_lineamiento}")
        else:
            print("El lineamiento no existe")

    elif eleccion == "4":
        if input("Seguro (s/n): ") == "s":
            lineamientos = []
            nos = []

    elif eleccion == "5":
        if input("Seguro (s/n): ") == "s":
            sys.exit()