#importaremos el modulo de psycopg2 en python
import psycopg2

conexion = psycopg2.connect(
	user='postgres',   #usuario qu pusimos o deafult
	password='kukiracle',  #password que pusimos al instalar
	host='127.0.0.1',   #esto es igual a local host
	port='5432',     #puerto con el que creamos
	database='test_db'#nombre base ddatos
)
try:
	with conexion:
		with conexion.cursor() as cursor:
			sentencia='SELECT * FROM persona WHERE persona_id=%s' #simple string con la consulta sql
			persona_id = input("introdusca id a buscar")
			cursor.execute(sentencia,(persona_id,))# ponemos al final una , para decir que es una tupla
			
			registros=cursor.fetchone()#recupera un registro fetchone ()
					# en formato listay dentro una tupla comando fetchall()stodo
					#lista con tuplas
					#[(1, 'juan', 'perez', 'jperez@gmail.com\n'), (2, 'karla', 'gomez', 'kgomez@gmail.com')]
			print(registros)

except Exception as e:
	print(f'ocurrio un error: {e}')

finally:
	conexion.close()
	
