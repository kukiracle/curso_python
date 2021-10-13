#orden de inicializacion objetos
class Padre:
    def __init__(self):
        print('inicializador Padre')
        
    def metodo( self ):
        print('metodo padre')
        
# padre1=Padre()
# padre1.metodo()

class hijo(Padre):
    
    def __init__(self): 
        print('iniciando hijo')
        super ( ).__init__ ( )
    
    def metodo( self ):
            print('sobrescrito metodo hijo')

h1=hijo()
h1.metodo()