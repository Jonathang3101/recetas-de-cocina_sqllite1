import sqlite3


def crear_tabla():
    conexion = sqlite3.connect("libro_recetas.db")
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recetas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            ingredientes TEXT NOT NULL,
            pasos TEXT NOT NULL
        )
    ''')

    conexion.commit()
    conexion.close()


def agregar_receta():
    nombre = input("Nombre de la receta: ")
    ingredientes = input("Ingredientes : ")
    pasos = input("Pasos de la receta: ")

    conexion = sqlite3.connect("libro_recetas.db")
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO recetas (nombre, ingredientes, pasos) VALUES (?, ?, ?)",
                   (nombre, ingredientes, pasos))

    conexion.commit()
    conexion.close()

    print("Receta agregada con éxito.")


def actualizar_receta():
    id_receta = input("ID de la receta a actualizar: ")
    nombre = input("Nuevo nombre de la receta: ")
    ingredientes = input("Nuevos ingredientes : ")
    pasos = input("Nuevos pasos de la receta: ")

    conexion = sqlite3.connect("libro_recetas.db")
    cursor = conexion.cursor()

    cursor.execute("UPDATE recetas SET nombre=?, ingredientes=?, pasos=? WHERE id=?",
                   (nombre, ingredientes, pasos, id_receta))

    conexion.commit()
    conexion.close()

    print("Receta actualizada con éxito.")


def eliminar_receta():
    id_receta = input("ID de la receta a eliminar: ")

    conexion = sqlite3.connect("libro_recetas.db")
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM recetas WHERE id=?", (id_receta,))

    conexion.commit()
    conexion.close()

    print("Receta eliminada con éxito.")


def ver_recetas():
    conexion = sqlite3.connect("libro_recetas.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM recetas")
    recetas = cursor.fetchall()

    if not recetas:
        print("No hay recetas disponibles.")
    else:
        for receta in recetas:
            print(f"{receta[0]}. {receta[1]}")

    conexion.close()


def buscar_receta():
    keyword = input("Ingrese un ingrediente o paso de receta a buscar: ")

    conexion = sqlite3.connect("libro_recetas.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM recetas WHERE ingredientes LIKE ? OR pasos LIKE ?",
                   (f"%{keyword}%", f"%{keyword}%"))

    resultados = cursor.fetchall()

    if not resultados:
        print("No se encontraron recetas con ese ingrediente o paso.")
    else:
        for receta in resultados:
            print(f"{receta[1]} - Ingredientes: {receta[2]}, Pasos: {receta[3]}")

    conexion.close()


def main():
    crear_tabla()

    while True:
        print("\n--- Menú ---")
        print("a) Agregar nueva receta")
        print("b) Actualizar receta existente")
        print("c) Eliminar receta existente")
        print("d) Ver listado de recetas")
        print("e) Buscar ingredientes y pasos de receta")
        print("f) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "a":
            agregar_receta()
        elif opcion == "b":
            actualizar_receta()
        elif opcion == "c":
            eliminar_receta()
        elif opcion == "d":
            ver_recetas()
        elif opcion == "e":
            buscar_receta()
        elif opcion == "f":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
