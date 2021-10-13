#argumentos no definidos o infinitos :v
#estos argumentos lo trata como una tupla *nombres
#una tupla nose pued modificar
def listar_nombres(*nombres):
       for nombre in nombres:
          print(nombre)
          
listar_nombres('juan','karla','maria','ernesto')