# ALUMNA: Marta Martínez Delgado
# TAREA: “Adivina el número”

# Librerías necesarias:
#  1. openpyxl (gestión del Excel)
#  2. matplotlib (gráficos de estadísticas)

# Si fuera necesario instalarlas: pip install openpyxl matplotlib

# Archivos utilizados:
#  1. JuegoPrincipal.py (este archivo) → programa principal del juego
#  2. ModuloJuego.py  → módulo con las funciones del juego
#  3. Estadisticas.xlsx → aquí se almacenan los datos del juego

# Ruta utilizada para el fichero Excel (tengo macOS) es: ./Estadisticas.xlsx 
# El fichero se crea automáticamente si no existe

import ModuloJuego as A

print("¡Bienvenido a Adivina el Número!")

while True:
    print("\n--- MENÚ ---")
    print("1. Partida modo solitario")
    print("2. Partida 2 jugadores")
    print("3. Estadística")
    print("4. Salir")

    try:
        opcion = int(input("Elige opción: "))
    except ValueError:
        print("Introduce un número válido")
        continue

    if opcion == 1:
        dificultad = A.elegir_dificultad()
        numero, maximo, intentos = A.generar_numero(dificultad, "solitario")
        ganado, intentos_usados = A.adivinar(numero, maximo, intentos)
        nombre = input("Introduce tu nombre: ")
        resultado = "Ganado" if ganado else "Perdido"
        A.guardar_resultado(nombre, resultado, dificultad, "Solitario", intentos_usados)

    elif opcion == 2:
        dificultad = A.elegir_dificultad()
        numero, maximo, intentos = A.generar_numero(dificultad, "2jugadores")
        ganado, intentos_usados = A.adivinar(numero, maximo, intentos)
        nombre = input("Introduce el nombre del Jugador 2: ")
        resultado = "Ganado" if ganado else "Perdido"
        A.guardar_resultado(nombre, resultado, dificultad, "2 jugadores", intentos_usados)

    elif opcion == 3:
        while True:
            print("\n--- ESTADÍSTICAS ---")
            print("1. Ver resultados en consola")
            print("2. Ver gráfico de resultados")
            print("3. Ver gráfico de dificultades")
            print("4. Volver al menú principal")
            try:
                graf = int(input("Elige opción: "))
            except ValueError:
                print("Introduce un número válido")
                continue

            if graf == 1:
                A.crear_excel()
                workbook = A.load_workbook(A.EXCEL_PATH)
                hoja = workbook["Estadísticas"]
                for fila in hoja.iter_rows(min_row=1, values_only=True):
                    print(fila)
            elif graf == 2:
                A.grafico_resultados()
            elif graf == 3:
                A.grafico_dificultades()
            elif graf == 4:
                break
            else:
                print("Opción no válida")

    elif opcion == 4:
        print("¡Gracias por jugar!")
        break

    else:
        print("Opción no válida")
