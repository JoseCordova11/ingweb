#archivo para conexcion base de datos
import pymysql 

conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='universidad',
    port=3306

)

def consultar_modalidades():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM modalidad')
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila[1])

def insertar_carrera():
    cursor = conn.cursor()
    cursor.execute('INSERT INTO carrera(codigo, nombre, modalidad) VALUES("Comp_01", "Computacion", 1)')
    conn.commit()  # Confirmar la inserción en la base de datos

def consultar_carreras():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM carrera')
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila[0], '-',fila[1], '-',fila[2])

# Ejecutar las funciones
insertar_carrera()
consultar_carreras()
consultar_modalidades()

# Cerrar conexión a la base de datos
conn.close()#Cerramos conexion a la base de datos



