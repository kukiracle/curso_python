#iterar con una lista

nombres= ["juan","karla","ricardo","maria",0,100,True]
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')
    
    
#preguntar el largo de una lista
print(len(nombres))

#funcion append inserta al final de la LISTA
nombres.append("ultimo")
print(nombres)    

#insertar elemento en un indice especifico y luego se mueven ala derecha

nombres.insert(0,'inicio')
print(nombres)  

#para remover un elemento
print(nombres) 


# remover ultimo elemento agregado al final
nombres.pop()
print(nombres) 

#eliminar un indice indicado
del nombres[0]
print(nombres) 

#eliminar la LISTA 
nombres.clear()
print(nombres)
#borrar lista por completo desde la memoria
del nombres
print(nombres)