from logger_base154 import log
from conexion import Conexion
from Persona import Persona
from cursor_del_pool import CursorDelPool
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
        with CursorDelPool() as cursor:  #reducimos un wit gracias a los dunder enter y exit
            cursor.execute(cls._SELECCIONAR) #ejecutamos el atributo que es una consulta
            lista_registros=cursor.fetchall() #jalamos de la bd gracias a cursor.fetchall no son objetos
            lista_personas=[]       #lista vacia de objetos personas vector
            for registro in lista_registros:
                persona =Persona(registro[0],registro[1],registro[2],registro[3]) #creamos objeto persona y metemos cada uno de lalista_registros
                lista_personas.append(persona)#metemos ala listapersonas el objeto persona
            return lista_personas #1ro cada registro en objetos luego lo me metemos lista y return
    
    @classmethod
    def insertar( cls,persona ): #recibimos un objeto
        with CursorDelPool ( ) as cursor:
            valores =(persona.persona_nombre,persona.persona_apellido,persona.persona_email)#tupla de vlores
            cursor.execute(cls._INSERTAR, valores)
            log.debug ( f'Persona a insertada: {persona}')
            return cursor.rowcount
    @classmethod
    def actualizar( cls,persona ):#recibimos un objeto
        with CursorDelPool ( ) as cursor:
            valores =(persona.persona_nombre,persona.persona_apellido,persona.persona_email,persona.persona_id)#tupla de vlore y get
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f'Persona Actualizada {persona}')
            return cursor.rowcount
    @classmethod
    def eliminar( cls,persona ):
        with CursorDelPool ( ) as cursor:
            valores=(persona.persona_id,) #tupla ps hirmanu :v get id
            #cursor trabaja con tuplas pes hermano no lo ovides
            cursor.execute(cls._ELIMINAR,valores)#mandamos al atributoeliminar y los valores
            log.debug(f'Objeto Eliminado:{persona}')
            return cursor.rowcount#numro de personas eliminadas
            
                
                
if __name__=='__main__':
    # insertar un registro
    # p1 = Persona ( persona_nombre = 'alejandra', persona_apellido = 'tellez', persona_email = 'atellez@gmail.com' )
    # personas_insertadas = PersonaDAO.insertar(p1)
    # log.debug ( f'PersonasInsertadas: {personas_insertadas}' )
    
    #actualizar un registro
    # p1 = Persona (19,'juancito','juarez','jjuarez@gmail.com')
    # personas_actualizadas=PersonaDAO.actualizar(p1)
    # log.debug(f'Personas actualizadas: {personas_actualizadas}')
    
    #eliminar un registro
    p1=Persona(persona_id=19)
    personas_eliminadas= PersonaDAO.eliminar(p1)
    log.debug(f'Personas Eliminadas: {personas_eliminadas}')

    # seleccionar
    # personas = PersonaDAO.seleccionar ( )
    # for personita in personas:
    #     log.debug ( personita )
    # 
 
    
    

#responsabilidad de esta clase es
#realizar operaciones sobre la base de datos
#de entidad persona CRUD
#dao= data access object es una clase que usa clase persona
#borrar editara creara objetos y lo takeara en la base de datos

