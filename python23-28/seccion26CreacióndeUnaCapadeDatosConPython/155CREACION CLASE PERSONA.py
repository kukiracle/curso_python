class Persona:
    def __init__(self,persona_id,persona_nombre,persona_apellido,persona_email):
        self._persona_id = persona_id
        self._persona_nombre = persona_nombre
        self._persona_apellido = persona_apellido
        self._persona_email = persona_email
    
    def __str__(self):
        return f'''
            ID PERSONA:{self._persona_id},NOMBRE: {self._persona_nombre},
             APELLIDO: {self._persona_apellido},EMAIL: {self._persona_email}
        '''
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
     
    
        
    
        
    
        
        
        