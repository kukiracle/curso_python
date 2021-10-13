# importaremos el modulo de psycopg2 en python
 #este video usaremos executemany
import psycopg2

conexion = psycopg2.connect (
    user = 'postgres',  # usuario qu pusimos o deafult
    password = 'kukiracle',  # password que pusimos al instalar
    host = '127.0.0.1',  # esto es igual a local host
    port = '5432',  # puerto con el que creamos
    database = 'test_db'  # nombre base datos
)
try:
    with conexion:
        with conexion.cursor ( ) as cursor:
            sentencia='DELETE FROM persona WHERE persona_id IN %s'
            entrada=input("proporciona el id Persona a eliminar (separados por coma) ")
            valores=(tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)#usamos executemany para ejecutar varias veces la sentencia
            registros_eliminados=cursor.rowcount   #contara cuantos registros se insertaron
            print(f'Registros Eliminados: {registros_eliminados}')
            
except Exception as e:                 
    print ( f'ocurrio un error: {e}' )

finally:
    conexion.close ( )
