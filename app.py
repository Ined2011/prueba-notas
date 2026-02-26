# Diccionario donde:
# clave = nombre del estudiante
# valor = lista de notas
estudiantes = {}

def registrar_ingreso():
    nombre = input("Ingrese el nombre del estudiante: ")

    if nombre in estudiantes:
        print("El estudiante ya está registrado.")
    else:
        estudiantes[nombre] = []
        print("Estudiante registrado correctamente.")


def registrar_nota():
    nombre = input("Ingrese el nombre del estudiante: ")

    if nombre in estudiantes:
        try:
            nota = float(input("Ingrese la nota (0.0 - 5.0): "))
            if 0.0 <= nota <= 5.0:
                estudiantes[nombre].append(nota)
                print("Nota registrada correctamente.")
            else:
                print("La nota debe estar entre 0.0 y 5.0")
        except ValueError:
            print("Debe ingresar un número válido.")
    else:
        print("El estudiante no está registrado.")


def ver_promedio():
    nombre = input("Ingrese el nombre del estudiante: ")

    if nombre in estudiantes:
        if len(estudiantes[nombre]) > 0:
            promedio = sum(estudiantes[nombre]) / len(estudiantes[nombre])
            print(f"El promedio de {nombre} es: {round(promedio,2)}")
        else:
            print("El estudiante no tiene notas registradas.")
    else:
        print("El estudiante no existe.")


def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        print("Lista de estudiantes:")
        for nombre in estudiantes:
            print("-", nombre)

