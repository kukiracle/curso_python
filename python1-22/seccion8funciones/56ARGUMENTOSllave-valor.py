#recibimos un diccionario key, value 
#**
def listar_terminos(**terminos):
       for llave,valor in terminos.items():
         print(f'{llave}:{valor}')
         
         
listar_terminos(IDE='IntegratedDevelopment',PK='primaryKey')
listar_terminos(CEJO='ColegioEnJo')