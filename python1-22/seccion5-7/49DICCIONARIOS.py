# UN DICCIONARIO TIENE (KEY, VALUE)como un diccionario
#es como un jason :V
#para entrar a los elementos con la key'IDE'

diccionario={
    'IDE':'integrated develoment eviroment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
    
}

print(diccionario)

#largo
print(len(diccionario))

#para acceder a un elemento usamos su (KEY)
print(diccionario['IDE'])
#OTRA forma de recuperar elementos 
print(diccionario.get('OOP'))

#MODIFICAR ELEMENTOS 

diccionario['IDE']='INTEGRATEDDEVELOMENTEVIROMENT'
print(diccionario)
