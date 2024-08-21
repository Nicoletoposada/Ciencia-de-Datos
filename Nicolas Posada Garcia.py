import mysql.connector

#Configuración de la conexión a la base de datos
config = {
    'user': 'studentsucundi',
    'password': 'mami_prende_la_radi0',
    'host': '18.188.124.77',
    'database': 'employees',  #Nombre de la base de datos
    'port': 3306
}

#Conexión a la base de datos
connection = mysql.connector.connect(**config)

#Crear un cursor para ejecutar las consultas
cursor = connection.cursor()

#CREAR TABLA
def create_record(nombre, apellido):
    query = "INSERT INTO `1` (nombre, apellido) VALUES (%s, %s)"
    values = (nombre, apellido)
    cursor.execute(query, values)
    connection.commit()
    print(f"Registro creado: {nombre} {apellido}")

#Consultar la tabla `1`
def consultar_1():
    query = "SELECT * FROM `1` LIMIT 50"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)

#Ejecución de creación
create_record('Lo', 'Logré')

#Ejecución de la consulta
consultar_1()

#Cerrar la conexión
cursor.close()
connection.close()
