
def validar_titulo(titulo):
    if titulo == "":
        return False
    letras_reales = 0
    for caracter in titulo:
        if caracter != " ":
            letras_reales = letras_reales + 1
    if letras_reales == 0:
        return False
    return True


def validar_duracion(duracion):
        try:
            valor = int(duracion)
            if valor > 0 :
                return True
            else: 
                return False
        except ValueError:
            return False



def validar_calificacion(calificacion):
    try:
        valor = float(calificacion)
        if valor >= 0.0 and valor <= 10.0:
            return True
        else:
            return False
    except ValueError:
        return False


def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    opcion_texto = input("Seleccione una opcion: ")
    comprobando = True
    while comprobando:
        try:
            opcion_numero = int(opcion_texto)
            if opcion_numero >= 1 and opcion_numero <= 6:
                return opcion_numero
            else:
                print("Opcion invalida. Debe ingresar un numero entre 1 y 6.")
                opcion_texto = input("Seleccione una opcion: ")
        except ValueError:
            print("Opcion invalida. Debe ingresar un numero entre 1 y 6.")
            opcion_texto = input("Seleccione una opcion: ")


def agregar_pelicula(peliculas):
    titulo = input("Ingrese el titulo de la pelicula: ")
    if not validar_titulo(titulo):
        print("Error: el titulo no puede estar vacio ni contener solo espacios.")
        return

    duracion = input("Ingrese la duracion en minutos: ")
    if not validar_duracion(duracion):
        print("Error: la duracion debe ser un numero entero mayor que cero.")
        return

    calificacion = input("Ingrese la calificacion (0.0 a 10.0): ")
    if not validar_calificacion(calificacion):
        print("Error: la calificacion debe ser un numero decimal entre 0.0 y 10.0.")
        return

    nueva_pelicula = {
        "titulo": titulo,
        "duracion": int(duracion),
        "calificacion": float(calificacion),
        "disponible": False
    }
    peliculas.append(nueva_pelicula)
    print("Pelicula agregada correctamente.")


def buscar_pelicula(peliculas, titulo_buscado):
    for i in range(len(peliculas)):
        if peliculas[i]["titulo"] == titulo_buscado:
            return i
    return -1


def opcion_buscar(peliculas):
    titulo = input("Ingrese el titulo de la pelicula a buscar: ")
    posicion = buscar_pelicula(peliculas, titulo)
    if posicion == -1:
        print("Película no encontrada o no existe.")
    else:
        pelicula = peliculas[posicion]
        print("Pelicula encontrada en la posicion", posicion)
        print("Titulo:", pelicula["titulo"])
        print("Duracion:", pelicula["duracion"])
        print("Calificacion:", pelicula["calificacion"])
        print("Disponible:", pelicula["disponible"])


def eliminar_pelicula(peliculas):
    titulo = input("Ingrese el titulo de la pelicula a eliminar: ")
    posicion = buscar_pelicula(peliculas, titulo)
    if posicion == -1:
        print("La película '", titulo, "' no se encuentra registrada.")
    else:
        peliculas.pop(posicion)
        print("Pelicula eliminada correctamente.")


def actualizar_disponibilidad(peliculas):
    for pelicula in peliculas:
        if pelicula["calificacion"] >= 7.0:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False


def mostrar_peliculas(peliculas):
    actualizar_disponibilidad(peliculas)
    print("\n=== LISTA DE PELICULAS ===")
    if len(peliculas) == 0:
        print("No hay peliculas registradas.")
        return
    for pelicula in peliculas:
        if pelicula["disponible"]:
            estado = "DISPONIBLE"
        else:
            estado = "NO RECOMENDADA"
        print("Título:", pelicula["titulo"])
        print("Duración:", pelicula["duracion"])
        print("Calificación:", pelicula["calificacion"])
        print("Estado:", estado)
        print("********************************************")


peliculas = []

opcion = 0
while opcion != 6:
    mostrar_menu()
    opcion = leer_opcion()
    
    if opcion == 1:
        agregar_pelicula(peliculas)
    elif opcion == 2:
        opcion_buscar(peliculas)
    elif opcion == 3:
        eliminar_pelicula(peliculas)
    elif opcion == 4:
        actualizar_disponibilidad(peliculas)
    elif opcion == 5:
        mostrar_peliculas(peliculas)
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")