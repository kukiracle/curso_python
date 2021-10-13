from logger_base154 import log
from Conexion import Conexion
from Persona import Persona

class PersonaDAO:
    '''
    DAO (Data Access Object
    CRUD(Create-Read-Update-Delete)
    '''
    _SELECCIONAR='SELECT * FROM persona ORDER BY persona_id'
    _INSERTAR='INSERT INTO persona (persona_nombre,persona_apellido,persona_email) VALUES(%s,%s,%s)'
    _ACTUALIZAR='UPDATE persona SET persona_nombre=%s,persona_apellido=%s,persona_email=%s WHERE persona_id=%s'
    _ELIMINAR='DELETE FROM persona WHERE persona_id=%s'
    
    @classmethod
    def seleccionar( cls ):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._SELECCIONAR) #ejecutamos el atributo que es una consulta
            lista_registros=cursor.fetchall() #jalamos de la bd gracias a cursor.fetchall no son objetos
            lista_personas=[]       #lista vacia de objetos personas vector
            for registro in lista_registros:
                persona =Persona(registro[0],registro[1],registro[2],registro[3]) #creamos objeto persona y metemos cada uno de lalista_registros
                lista_personas.append(persona)#metemos ala listapersonas el objeto persona
            return lista_personas
    
    @classmethod
    def insertar( cls,persona ): #recibimos un objeto
        with Conexion.obtenerConexion() as conexion: 
            with conexion.cursor() as cursor:
                
                valores =(persona.persona_nombre,persona.persona_apellido,persona.persona_email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug ( f'Persona a insertada: {persona}')
                return cursor.rowcount
            
                
            





if __name__=='__main__':
    # insertar un registro
    p1 = Persona ( persona_nombre = 'pedro', persona_apellido = 'najera', persona_email = 'pnajera@gmail.com' )
    personas_insertadas = PersonaDAO.insertar(p1)
    log.debug ( f'PersonasInsertadas: {personas_insertadas}' )
    # seleccionar
    personas = PersonaDAO.seleccionar ( )
    for personita in personas:
        log.debug ( personita )
    
 
    
    

#responsabilidad de esta clase es
#realizar operaciones sobre la base de datos
#de entidad persona CRUD
#dao= data access object es una clase que usa clase persona
#borrar editara creara objetos y lo takeara en la base de datos

