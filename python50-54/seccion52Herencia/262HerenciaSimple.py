#ejemplo herencia simple

class LitaSimple:
    def __init__(self,elementos):
        self._elementos=list(elementos)
    
    def agregar( self,elemento ):
        self._elementos.append(elemento) #append agregar elemento push
    
    def __getitem__(self, indice):
        return self._elementos[indice]
     
    def ordenar( self ):
        self._elementos.sort()
        
        
    def __len__(self):          #tamaño del elemnto lista
        return len(self._elementos)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos})'
    
    

# lis1.ordenar()
# print(lis1)

class ListaOrdenada(LitaSimple):
    def __init__(self,elementos=[]):
        super().__init__(elementos)
        #ordenamos siempre los elementos de maner asc una vez incializados
        self.ordenar()
    def agregar( self,elemento ):
        super().agregar(elemento)
        #siempre ordenamos
        self.ordenar()
 
 
        
lis1=LitaSimple([3,4,1,2])
print(lis1)
hija1=ListaOrdenada(lis1)
hija1.agregar(7)
print(hija1)