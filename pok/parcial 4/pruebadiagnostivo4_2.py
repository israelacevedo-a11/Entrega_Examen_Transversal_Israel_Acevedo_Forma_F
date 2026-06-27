# ==========================================
# FUNCIONES DE MENÚ
# ==========================================

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar empleado")
    print("2. Buscar empleado")
    print("3. Eliminar empleado")
    print("4. Actualizar estado")
    print("5. Mostrar empleados")
    print("6. Salir")
    print("=====================================")

def obtener_opcion():
    try:
        opcion = int(input("Ingrese una opción (1-6): "))
        return opcion
    except ValueError:
        return 0

# ==========================================
# FUNCIONES DE VALIDACIÓN
# ==========================================

def validar_nombre(nombre):
    # Verificamos que al quitar los espacios quede algo
    if len(nombre.strip()) > 0:
        return True
    else:
        return False

def validar_edad(edad):
    try:
        valor = int(edad)
        if valor > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def validar_salario(salario):
    try:
        valor = float(salario)
        if valor > 0:
            return True
        else:
            return False
    except ValueError:
        return False

# ==========================================
# FUNCIONES PRINCIPALES
# ==========================================

def agregar_empleado(lista):
    print("\n--- AGREGAR EMPLEADO ---")
    nombre = input("Ingrese el nombre completo: ")
    edad = input("Ingrese la edad: ")
    salario = input("Ingrese el salario mensual: ")

    es_valido_nombre = validar_nombre(nombre)
    es_valido_edad = validar_edad(edad)
    es_valido_salario = validar_salario(salario)

    if es_valido_nombre == False:
        print("Error: El nombre no puede estar vacío ni contener solo espacios.")
    
    if es_valido_edad == False:
        print("Error: La edad debe ser un número entero mayor que cero.")
    
    if es_valido_salario == False:
        print("Error: El salario debe ser un número decimal mayor que cero.")

    if es_valido_nombre == True and es_valido_edad == True and es_valido_salario == True:
        # Creamos el diccionario del empleado
        nuevo_empleado = {
            "nombre": nombre.strip(),
            "edad": int(edad),
            "salario": float(salario),
            "activo": False
        }
        # Lo agregamos a la lista
        lista.append(nuevo_empleado)
        print("¡Empleado agregado con éxito!")

def buscar_empleado(lista, nombre):
    # Recorremos la lista por posiciones
    for i in range(len(lista)):
        # Si el nombre coincide exactamente
        if lista[i]["nombre"] == nombre:
            return i
    # Si termina el ciclo y no lo encuentra, retorna -1
    return -1

def actualizar_estado(lista):
    for empleado in lista:
        if empleado["edad"] >= 18:
            empleado["activo"] = True
        else:
            empleado["inactivo"] = False
    print("Estados de los empleados actualizados correctamente.")

def mostrar_empleados(lista):
    if len(lista) == 0:
        print("\nNo hay empleados registrados para mostrar.")
        return

    # Primero actualizamos los estados como pide el enunciado
    actualizar_estado(lista)
    
    print("\n=== LISTA DE EMPLEADOS ===")
    for empleado in lista:
        print("Nombre:", empleado["nombre"])
        print("Edad:", empleado["edad"])
        print("Salario:", empleado["salario"])
        
        if empleado["activo"] == True:
            print("Estado: ACTIVO")
        else:
            print("Estado: INACTIVO")
            
        print("********************************************")


# ==========================================
# FLUJO PRINCIPAL DEL PROGRAMA (Sin main)
# ==========================================

empleados = [] 

while True:
    mostrar_menu()
    opcion_elegida = obtener_opcion()

    if opcion_elegida == 1:
        agregar_empleado(empleados)
        
    elif opcion_elegida == 2:
        print("\n--- BUSCAR EMPLEADO ---")
        nombre_buscar = input("Ingrese el nombre exacto del empleado a buscar: ")
        posicion = buscar_empleado(empleados, nombre_buscar)
        
        if posicion != -1:
            emp = empleados[posicion]
            print("\nEmpleado encontrado en la posición", posicion, ":")
            print("Nombre:", emp["nombre"], "| Edad:", emp["edad"], "| Salario:", emp["salario"], "| Activo:", emp["activo"])
        else:
            print("El empleado no se encuentra registrado.")
            
    elif opcion_elegida == 3:
        print("\n--- ELIMINAR EMPLEADO ---")
        nombre_eliminar = input("Ingrese el nombre exacto del empleado a eliminar: ")
        
        posicion = buscar_empleado(empleados, nombre_eliminar)
        
        if posicion != -1:
            empleados.pop(posicion)
            print("Empleado eliminado exitosamente.")
        else:
            # Usando comas en vez de f-strings
            print("El empleado", nombre_eliminar, "no se encuentra registrado.")
            
    elif opcion_elegida == 4:
        print("\n--- ACTUALIZAR ESTADO ---")
        actualizar_estado(empleados)
        
    elif opcion_elegida == 5:
        mostrar_empleados(empleados)
        
    elif opcion_elegida == 6:
        print("\nGracias por usar el sistema. Vuelva Pronto")
        break
        
    else:
        print("\nOpción inválida. Por favor, intente nuevamente.")