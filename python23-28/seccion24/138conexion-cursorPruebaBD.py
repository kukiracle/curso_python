#importaremos el modulo de psycopg2 en python
import psycopg2

#paso 2 creamos el objeto conexion en la variable conexion con psycopg2
#esta en formato diccionario y tiene lo sisguientes valores

conexion = psycopg2.connect(
	user='postgres',   #usuario qu pusimos o deafult
	password='kukiracle',  #password que pusimos al instalar
	host='127.0.0.1',   #esto es igual a local host
	port='5432',     #puerto con el que creamos
	database='test_db'#nombre base ddatos
)

#print(conexion)  para ver si se creo el objeto y la conexion

#paso 3 ahora creamos el cursor que sirve para ejecutar las sentencias SQL
#objeto cursor en base a conexion
cursor=conexion.cursor()
#simple string con la consulta sql
sentencia='SELECT * FROM persona'
# con el objeto cursor usaremos el comando execute y mandamos el sql
cursor.execute(sentencia)
#recupera todos los registros de la sentencia en formato listay dentro una tupla comando fetchall()
registros=cursor.fetchall()
#lista con tuplas
#[(1, 'juan', 'perez', 'jperez@gmail.com\n'), (2, 'karla', 'gomez', 'kgomez@gmail.com')]
print(registros)

cursor.close()  #cerramos el objeto cursor
conexion.close()#cerramos el objeto conexion