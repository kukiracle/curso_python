# UNA TUPLA MANTIENE EL ORDEN DE LA LISTA EN QU ELOS AGREGAMOS
# ES UNA LISTA QUE NO SE PUEDE CAMBIAR INMUTABLE
#no podemos eliminar elemntos de la tupla
#DEFINIMOS TUPLA FRUTA con parentesis()

frutas= ('Naranja','Platano','Guayaba')
print(len(frutas))
print(frutas)

#mostrar sin salto de linea que viene por defecto con end=' '
for fruta in frutas:
    print(fruta, end=' ')
    
    

print(" -")
listafrutas=list(frutas)

listafrutas[0]='pera'
print(listafrutas)

del frutas

    