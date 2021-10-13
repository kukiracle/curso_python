# importaremos el modulo de psycopg2 en python
import psycopg2

conexion = psycopg2.connect (
    user = 'postgres',  # usuario qu pusimos o deafult
    password = 'kukiracle',  # password que pusimos al instalar
    host = '127.0.0.1',  # esto es igual a local host
    port = '5432',  # puerto con el que creamos
    database = 'test_db'  # nombre base ddatos
)
try:
    with conexion:
        with conexion.cursor ( ) as cursor:
            sentencia = 'SELECT * FROM persona WHERE persona_id IN %s'  # simple string con la consulta sql
            
            entrada = input ( 'proporciona los id\'s a buscar: (separado por comas): ' )
            # convirtiendo variable entrada a tupla
            llaves_primarias = (tuple ( entrada.split ( ',' ) ),)  # kitando las comas con split
            # y con la coma final se vuelve tupla de tuplas
            
            cursor.execute ( sentencia, llaves_primarias )  # execute solo acepta tuplas (sentencia,(tupla1,))
            registros = cursor.fetchall ( )  # recupera un registro fetchone ()uno
            # en formato listay dentro una tupla comando fetchall()todos
            # lista con tuplas
            # [(1, 'juan', 'perez', 'jperez@gmail.com\n'), (2, 'karla', 'gomez', 'kgomez@gmail.com')]
            for i in registros:
                print ( i )

except Exception as e:
    print ( f'ocurrio un error: {e}' )

finally:
    conexion.close ( )
