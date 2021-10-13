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
            sentencia='UPDATE persona SET persona_nombre=%s,persona_apellido=%s,persona_email=%s WHERE persona_id=%s'
            valores=(('carlos','mamani','cmamani@gmail.com',2),
                     ('ana ','vicente','avicente@gmail.com',5))
            cursor.executemany(sentencia,valores)#usamos executemany para ejecutar varias veces la sentencia
           
            registros_actualizados=cursor.rowcount   #contara cuantos registros se insertaron
            print(f'Registros Actualizados: {registros_actualizados}')
            
except Exception as e:
    print ( f'ocurrio un error: {e}' )

finally:
    conexion.close ( )
