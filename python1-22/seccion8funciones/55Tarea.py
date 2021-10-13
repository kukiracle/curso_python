#argumentos no definidos o infinitos :v
#estos argumentos lo trata como una tupla *nombres
#una tupla nose pued modificar

#FUNCION CON ARGUMENTOS VARIABLES PARA SUMAR TODO LO RECIBIDO
def listar_numeros(*numeros):
   total=0
   for i in numeros:
       for i in numeros:
         total=total+i
         print(i)
   
   return total

suma=listar_numeros(2,3,2,3,5)
print(f'la suma total es:  {suma}')

              
                  
          

