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
            sentencia= 'INSERT INTO persona(persona_nombre,persona_apellido,persona_email) values(%s,%s,%s)'
            valores=('carlos','lara','clara@gmail.com')
            cursor.execute(sentencia,valores)
            #conexion.commit() este comando ya no es necesario porque el with lo hace automatico
            registros_insertados=cursor.rowcount   #contara cuantos registros se insertaron
            print(f'Registros Insertados: {registros_insertados}')
            
except Exception as e:
    print ( f'ocurrio un error: {e}' )

finally:
    conexion.close ( )
