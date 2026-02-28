# prueba-notas
Momento 1 de Nuevas Tecnologías

## Descripción

Aplicación de consola para gestionar notas de estudiantes. Permite registrar estudiantes, registrar sus notas, calcular promedios y visualizar la lista de estudiantes registrados.

## Funcionalidades

- **Registrar estudiante**: Agrega un nuevo estudiante al sistema.
- **Registrar nota**: Añade una nota (0.0 - 5.0) a un estudiante registrado.
- **Ver promedio**: Calcula y muestra el promedio de notas de un estudiante.
- **Mostrar lista de estudiantes**: Displays all registered students.
- **Salir**: Cierra la aplicación.

## Requisitos

- Python 3.x

## Cómo usar

1. Ejecutar el archivo `app.py`:
   ```bash
   python app.py
   ```

2. Seleccionar una opción del menú ingresando el número correspondiente:
   - `1` - Registrar un nuevo estudiante
   - `2` - Registrar una nota para un estudiante
   - `3` - Ver el promedio de un estudiante
   - `4` - Mostrar lista de estudiantes registrados
   - `5` - Salir del programa

## Rango de notas

Las notas válidas oscilan entre **0.0 y 5.0**. Si ingresa una nota fuera de este rango, la aplicación mostrará un mensaje de error.

## Notas técnicas

- Los datos se almacenan en un diccionario durante la ejecución del programa.
- El promedio se calcula con dos decimales de precisión.
- Validación de entrada para garantizar valores numéricos correctos.
