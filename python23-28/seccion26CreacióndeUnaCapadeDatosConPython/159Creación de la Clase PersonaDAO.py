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
            cursor.execute(cls._SELECCIONAR)
            lista_registros=cursor.fetchall() #jalados de la bd gracias a cursor.fetchall no son objetos
            lista_personas=[]       #lista vacia de objetos personas vector
            for registro in lista_registros:
                persona =Persona(registro[0],registro[1],registro[2],registro[3]) #creamos objeto persona y metemos cada uno de lalista_registros
                lista_personas.append(persona)#metemos ala listapersonas el objeto persona
            return lista_personas
 

if __name__=='__main__':
    personas=PersonaDAO.seleccionar()
    for personita in personas:
        log.debug(personita)
    
        
            
       




#responsabilidad de esta clase es
#realizar operaciones sobre la base de datos
#de entidad persona CRUD
#dao= data access object es una clase que usa clase persona
#borrar editara creara objetos y lo takeara en la base de datos

