import sqlite3

db_name = 'Clientes.db'

def consultas(query, parameters):

    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
        if 'SELECT' in query:
            return cursor.fetchone()
    return result

def consultar_registro(nombre_completo):
    
    query = "SELECT * FROM consumers WHERE consumer_full_name = ?"
    
    fila = consultas(query, (nombre_completo, ))
    print(fila)
    print("Registro consultado con exito")

def crear_registro(nombre_completo, correo, grado):
    
    query = "INSERT INTO consumers VALUES(NULL, ?, ?, ?)"
    parameters = (nombre_completo, correo, grado)
    consultas(query, parameters)
    print("Registro añadido con exito")

def eliminar_registro(nombre_completo):
    
    query = "DELETE FROM consumers WHERE consumer_full_name = ?"
    
    consultas(query, (nombre_completo, ))
    print("Registro eliminado con exito")
    
def editar_registro(nombre_antig, correo_antig, grado_antig, nuevo_nombre, nuevo_correo, nuevo_grado):
    
    query = "UPDATE consumers SET consumer_full_name = ?, consumer_email = ?, consumer_grade = ? WHERE consumer_full_name = ? AND consumer_email = ? AND consumer_grade = ?"
    parameters = (nuevo_nombre, nuevo_correo, nuevo_grado, nombre_antig, correo_antig, grado_antig)
    consultas(query, parameters)
    print("Registro editado con exito")

opcion = int(input("Digite 1 para añadir, 2 para editar, 3 para borrar o 4 para consultar:"))
if opcion == 1:
    nombre = input("Ingrese el nombre completo: ")
    correo = input("Ingrese el correo: ")
    grado = input("Ingrese el grado: ")
    crear_registro(nombre, correo, grado)
elif opcion == 2:
    nombre_antig = input("Ingrese el nombre actual: ")
    correo_antig = input("Ingrese el correo actual: ")
    grado_antig = input("Ingrese el grado actual: ")
    nombre_nuevo = input("Ingrese el nombre completo: ")
    correo_nuevo = input("Ingrese el correo: ")
    grado_nuevo = input("Ingrese el grado: ")
    editar_registro(nombre_antig, correo_antig, grado_antig, nombre_nuevo, correo_nuevo, grado_nuevo)
elif opcion == 3:
    nombre = input("Ingrese el nombre completo: ")
    eliminar_registro(nombre)
elif opcion == 4:
    nombre = input("Ingrese el nombre completo: ")
    consultar_registro(nombre)
else:
    print("mondongo")