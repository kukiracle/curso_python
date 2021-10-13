from logger_base154 import log

#archivo 154 loggin
class Persona:
    def __init__(self,persona_id=None,persona_nombre=None,persona_apellido=None,persona_email=None):
        self._persona_id = persona_id
        self._persona_nombre = persona_nombre
        self._persona_apellido = persona_apellido
        self._persona_email = persona_email
    
    def __str__(self): # es como mostrar pero con el debug 
        return f'''
            ID PERSONA:{self._persona_id},NOMBRE: {self._persona_nombre},
             APELLIDO: {self._persona_apellido},EMAIL: {self._persona_email}

    
                '''
      
    def __add__(self,persona):
        
        return f'{self.persona_nombre} {persona.persona_apellido}'
    
    def __sub__(self, other):
        return self.persona_id-other.persona_id
        
        
        
    @property
    def persona_id( self): #get _persona_id
        return self._persona_id
    @persona_id.setter    #set _persona_id
    def persona_id( self,persona_id ):
        self._persona_id=persona_id
    
    @property
    def persona_nombre( self ): #get persona_nombre
        return  self._persona_nombre
    @persona_nombre.setter
    def persona_nombre( self,persona_nombre ):
        self._persona_nombre=persona_nombre
        
    @property
    def persona_apellido( self ):
        return self._persona_apellido
    @persona_apellido.setter
    def persona_apellido( self,persona_apellido ):
        self._persona_apellido=persona_apellido
        
    @property
    def persona_email( self ):
        return self._persona_email
    @persona_email.setter
    def persona_email( self,persona_email ):
        self._persona_email=persona_email
     
    
if __name__=='__main__':#metodo que indica que solo se use aki losmetodos en esta clase
        p1 = Persona(5,'juan','perez','jperez@gmail.com')
        log.debug(p1)
        #simular un insert sin ID persona_id para ello nos vamos 
        #al constructor y ponemos none por default
        p2 = Persona (2,persona_nombre='will', persona_apellido = 'villegas', persona_email = 'wvilegas@gmail.com' )
        log.debug(p2)
        #simulamos un delete usando persona_id que gozu xd
        # p1= Persona(persona_id = 1)
        # log.debug(p1)
        # dANY EJEMPLOS SUB ADD
        print(p1+p2)
        print(p1-p2)
        
        
