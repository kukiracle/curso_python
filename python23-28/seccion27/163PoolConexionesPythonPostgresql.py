#crea altoke objetos conexiones y cursores termina d eusar el
#usuario rapidito lo suelta y le da a otro :v


from idlelib.pyshell import HOST
from logger_base154 import log
import psycopg2 as bd
import sys

from psycopg2 import pool  #esto es clave hermano :V

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'kukiracle'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON=1
    _MAX_CON=5
    _pool=None
    
    @classmethod
    def obtenerPool( cls ):
        if cls._pool is None:
            try:
                cls._pool= pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,
                                                     host=cls._HOST,
                                                     user=cls._USERNAME,
                                                     password=cls._PASSWORD,
                                                     port=cls._DB_PORT,
                                                     database=cls._DATABASE)
                log.debug(f'Creacion Pool Existosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio Un Error obtener el pool {e}')
                sys.exit()
        else:
            return cls._pool
                
                
        
    
    
    
    @classmethod
    def obtenerConexion ( cls ):
        pass
    
    

if __name__ == '__main__':
    pass