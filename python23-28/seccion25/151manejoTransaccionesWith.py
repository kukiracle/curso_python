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
#siempre mejor usar with porque tiene el rollback integrado y commit integrado automatico
try:
    with conexion:
        with conexion.cursor() as cursor:
    
            sentencia = 'INSERT INTO persona(persona_nombre,persona_apellido,persona_email) VALUES (%s,%s,%s)'
            valorestupla = ('weymar', 'condori', 'wcondori@gmail.com')
            cursor.execute(sentencia, valorestupla)
            
            sentencia='UPDATE persona SET persona_nombre=%s,persona_apellido=%s,persona_email=%s WHERE persona_id=%s'
            valorestupla=('dayana', 'apaza', 'dapaza@gmail.com', 7)
            cursor.execute(sentencia, valorestupla)
           
except Exception as e:
    
    print ( f'ocurrio un error: , se hizo rollback de la transaccion {e}' )

finally:
    conexion.close ( )
    print ( 'termina la transaccion, se hizo commit' )
