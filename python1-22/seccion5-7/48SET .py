# un set es como una lista pero no hay orden
#un set tampoco puede mantener duplicados
# un set no pude modificar elementos 
# si se puede eliminar elementos para

planetas={'marte','jupiter','venus'}
print(planetas)
#largo
print(len(planetas))
#revisar si un elemento esta presente
print('marte' in planetas)

#agregar un elemento 
planetas.add('tierra')
print(planetas)

#no permite duplicados
planetas.add('tierra')
print(planetas)
#eliminar elementos con mensaje de error
planetas.remove('tierra')
print(planetas)
#eliminar elementos sin mensaje de error
planetas.discard('tierras')
print(planetas)

#limpiar set
planetas.clear()
print(planetas)

#eliminar SET desde memoria
del planetas
print(planetas)




