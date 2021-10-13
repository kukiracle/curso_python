# UN DICCIONARIO TIENE (KEY, VALUE)como un diccionario
#es como un jason :V
#para entrar a los elementos con la key'IDE'

diccionario={
    'IDE':'integrated develoment eviroment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
    
}


#RECCORER LOS ELEMENTOS

for termino,valor in diccionario.items():
    print(termino,valor)
    
    # solo los KEYS terminos
for termino in diccionario.keys():
    print(termino)
    
#solo valores value
for valor in diccionario.values():
    print(valor)
    
#comprobar si existe elemento en DICCIONARIO
print('IDE' in diccionario)

#agregar elementos de

diccionario['PK']='primary key'
print(diccionario)

#remover elementos con pop
diccionario.pop('DBMS')
print(diccionario)

#limpiar los elementos del diccionario
diccionario.clear()
#eliminar diccionario por completo deswde la memoria

del diccionario
print(diccionario)