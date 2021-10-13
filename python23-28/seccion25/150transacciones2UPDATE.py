# importaremos el modulo de psycopg2 en python
# este video usaremos executemany
import psycopg2

conexion = psycopg2.connect (
    user = 'postgres',  # usuario qu pusimos o deafult
    password = 'kukiracle',  # password que pusimos al instalar
    host = '127.0.0.1',  # esto es igual a local host
    port = '5432',  # puerto con el que creamos
    database = 'test_db'  # nombre base datos
)
try:
    conexion.autocommit = False #con false no envia nada pormas que este bien la sentencia
    cursor = conexion.cursor() #OBJETO CURSOR
    
    sentencia = 'INSERT INTO persona(persona_nombre,persona_apellido,persona_email) VALUES (%s,%s,%s)'
    valorestupla = ('many', 'mamani', 'mmamani@gmail.com')
    cursor.execute(sentencia, valorestupla)
    
    sentencia='UPDATE persona SET persona_nombre=%s,persona_apellido=%s,persona_email=%s WHERE persona_id=%s'
    valorestupla=('juan carlos', 'juarez', 'jcjuarez@gmail.com', '7')
    cursor.execute(sentencia, valorestupla)
    
    print('termina la transaccion, se hizo commit')
    conexion.commit() #commit cambiado true indicando el envio ,es esto o with tu eliges muchacho :v
except Exception as e:
    conexion.rollback()  #vuelve  a un estado anterior la bd a esta transaccion fallida
    print ( f'ocurrio un error: , se hizo rollback de la transaccion {e}' )

finally:
    conexion.close ( )
