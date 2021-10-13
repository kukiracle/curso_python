#nombre delibro , id libro int, precio float, si es gratituito true or false, y luego mostrar


nombrelibro= input(f'introdusca nombre del libro')
id_libro=int(input(f'id de libro'))
precio_libro=float(input(f'precio del libro'))
print(f'es gratuito? si o no')
gratuito=input()
if gratuito=="si":
    gratuito=True
else:
    gratuito=False


print(f'nombre libro {nombrelibro}')
print(f' idlibro {id_libro}')
print(f' precio {precio_libro}')
print(f' es gratuioto {gratuito}')
