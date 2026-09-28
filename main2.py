from departamento import Departamento

# Creamos una lista inicial con algunos departamentos de prueba
departamentos: list[Departamento] = [
    Departamento(101, "Recursos Humanos", 2),
    Departamento(102, "Informática", 3)
]

def leer_numero(mensaje: str) -> int:
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def imprimir_departamentos() -> None:
    if len(departamentos) == 0:
        print("No hay departamentos registrados.")
    else:
        for dep in departamentos:
            print(dep)
            print("="*20)

def menu() -> int:
    print("="*20)
    print("Menú de opciones:")
    print("="*20)
    print("1. Agregar departamento")
    print("2. Editar departamento")
    print("3. Eliminar un departamento")
    print("4. Mostrar un departamento")
    print("5. Mostrar todos los departamentos")
    print("0. Salir")
    opcion = leer_numero("Ingrese opción: ")
    print("="*20)
    return opcion

def agregar_departamento() -> None:
    id_dep = leer_numero("Ingrese el ID del departamento: ")
    nombre = input("Ingrese el nombre del departamento: ")
    piso = leer_numero("Ingrese el piso del departamento: ")

    nuevo_dep = Departamento(id_dep, nombre, piso)
    departamentos.append(nuevo_dep)
    print("Departamento agregado exitosamente.")
    print(f"Total de departamentos registrados: {len(departamentos)}")

def buscar_departamento() -> Departamento:
    # Ahora buscamos por ID usando leer_numero porque es un int
    id_buscado = leer_numero("Ingrese el ID del departamento a buscar: ")
    for dep in departamentos:
        if dep.id_departamento == id_buscado:
            return dep
    print("Departamento no encontrado.")
    return None

def imprimir_departamento() -> None:
    dep = buscar_departamento()
    if dep:
        print(dep)
    else:
        print("No se encontró el departamento.")

def eliminar_departamento() -> None:
    dep = buscar_departamento()
    if dep:
        departamentos.remove(dep)
        print("El departamento ha sido eliminado correctamente.")
    else:
        print("No se encontró al departamento.")

def editar_departamento() -> None:
    dep = buscar_departamento()
    if dep:
        print(dep)
        print("1.- Editar nombre.")
        print("2.- Editar piso.")
        print("0.- Salir.")
        op = leer_numero("Ingrese una opción: ")
        
        if op == 1:
            nuevo_nombre = input("Ingrese nuevo nombre: ")
            dep.nombre = nuevo_nombre
            print("El nombre del departamento ha sido actualizado correctamente.")
        elif op == 2:
            nuevo_piso = leer_numero("Ingrese nuevo piso: ")
            dep.piso = nuevo_piso
            print("El piso del departamento ha sido actualizado correctamente.")
        elif op == 0:
            print("Cancelando edición...")
        else:
            print("Opción inválida.")
    else:
        print("No se encontró el departamento.")

def main():
    while True:
        opcion = menu()
        if opcion == 1:
            print("--- Agregar departamento ---")
            agregar_departamento()
        elif opcion == 2:
            print("--- Editar departamento ---")
            editar_departamento()
        elif opcion == 3:
            print("--- Eliminar un departamento ---")
            eliminar_departamento()
        elif opcion == 4:
            print("--- Mostrar un departamento ---")
            imprimir_departamento()
        elif opcion == 5:
            print("--- Mostrar todos los departamentos ---")
            imprimir_departamentos()
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.")

if __name__ == "__main__":
    main()