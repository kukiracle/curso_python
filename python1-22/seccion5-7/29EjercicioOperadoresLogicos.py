#edad 20 o 30s saber si esta en ese rango con logicos

edad= int(input("Introdusca edad"))
veintes= edad>=20 and edad <30
print(veintes)
treintas = edad>=30 and edad< 40
print(treintas)

if veintes:
    print(f'la edad {edad} esta en el rango de veintes')
else:
    if(treintas):
        print(f'la edad {edad} esta en el rango de treintas')
    else:
        print(f'la edad {edad}no esta en el rango')
        