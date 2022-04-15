import sqlite3
from sqlite3 import Error

def crearConexion():
    connection = None
    try:
        connection = sqlite3.connect(r"slang_sqlite.db")
        print(sqlite3.version)
    except Error as e:
        print(e)

    return connection

def crearTabla(conn):
    query = """ CREATE TABLE IF NOT EXISTS slang (
            palabra VARCHAR(255) NOT NULL,
            significado VARCHAR(255) NOT NULL,
            PRIMARY KEY (palabra)
        ); """
    cursor = conn.cursor()
    cursor.execute(query)

def agregarPalabra(conn, palabra, significado):
    try:
        query = "INSERT INTO slang VALUES (?, ?)"
        values = (palabra, significado)
        cursor = conn.cursor()
        cursor.execute(query, values)
        print("Palabra agregada!\n")
    except Error as e:
        print(e)

def editarPalabra(conn, palabra, significado):
    try:
        query = "UPDATE slang SET significado = ? WHERE palabra = ?"
        values = (significado, palabra)
        cursor = conn.cursor()
        cursor.execute(query, values)
        print("Palabra actualizada!\n")
    except Error as e:
        print(e)

def eliminarPalabra(conn, palabra):
    try:
        query = "DELETE FROM slang WHERE palabra = ?"
        values = (palabra,)
        cursor = conn.cursor()
        cursor.execute(query, values)
        print("Palabra eliminada!\n")
    except Error as e:
        print(e)

def listarPalabras(conn):
    query = "SELECT * FROM slang ORDER BY palabra ASC"
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print("- " + row[0] + ": " + row[1])

def buscarPalabra(conn, palabra):
    query = "SELECT * FROM slang WHERE palabra = ?"
    values = (palabra)
    cursor = conn.cursor()
    cursor.execute(query, values)
    result = cursor.fetchone()
    print("- " + result[0] + ": " + result[1] + "\n")

conn = crearConexion()
with conn:
    crearTabla(conn)
    while True:
        print("Seleccione una opcion:")
        print("1. Agregar nueva palabra")
        print("2. Editar palabra existente")
        print("3. Eliminar palabra existente")
        print("4. Ver listado de palabras")
        print("5. Buscar significado de palabra")
        print("6. Salir")
        opcion = int(input())

        if opcion == 1:
            print("\nAgregar nueva palabra")
            palabra = input("Nueva palabra: ")
            significado = input("Significado: ")
            agregarPalabra(conn, palabra, significado)
        elif opcion == 2:
            print("\nEditar palabra existente")
            palabra = input("Palabra: ")
            significado = input("Nuevo significado: ")
            editarPalabra(conn, palabra, significado)
        elif opcion == 3:
            print("\nEliminar palabra existente")
            palabra = input("Palabra: ")
            eliminarPalabra(conn, palabra)
        elif opcion == 4:
            print("\nListado de palabras")
            listarPalabras(conn)
            print()
        elif opcion == 5:
            print("\nBuscar significado de palabra")
            palabra = input("Palabra: ")
            buscarPalabra(conn, palabra)
        elif opcion == 6:
            print("\nHasta la proxima!!\n")
            break
        else:
            print("\nOpcion invalida! Intente nuevamente\n")
