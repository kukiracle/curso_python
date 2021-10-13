from logger_base154 import log#archivo y clase
from conexion import Conexion #archivo y clase
class CursorDelPool:
    def __init__( self ):
        self._conexion=None
        self._cursor=None
        
    def __enter__(self):  #se encarga de obtener una conexion
        log.debug('Inicio del metodo with __enter__')
        self._conexion=Conexion.obtenerConexion()
        self._cursor=self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('se ejecuta metodo __exit__')
        if valor_excepcion:  #algun error de envio de querys
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion: {valor_excepcion}{tipo_excepcion}{detalle_excepcion}')
        else:
            self._conexion.commit() #guardamos todos los cambios que hicimos con los querys
            log.debug('Commit de la transaccion')
            
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)
       