#leer archivo json
#json=javascript object notation
import json
import urllib.request

respuesta=urllib.request.urlopen('https://globalmentoring.com.mx/api/personas.json')
print(respuesta)  #pedimos de internet el archivo json

cuerpo_respuesta=respuesta.read() #convertimos a cuerpo la respuesta de la pagina

print(f'tipo binario {cuerpo_respuesta}') #nos devuelve los datos del Json en cadena tipo BINARIO/hex

#pero asi no sirve asi que para que sea util en python hay que procesar:

json_respuesta=json.loads(cuerpo_respuesta.decode('utf-8')) #lo decodificamos en formato json

print(f'tipo json con cotejamiento decode(utf-8 ){json_respuesta}')
#una vez convertido a json ya son caracteres con los cual podemos trabajar

#------------------para recuperar
#imprirmir solo nombres de las personas ejemplo
#JSON se comvierte a listas y diccionarios en phyton

#recorremos json_respuesta y mostramos sus datos
for i in json_respuesta['personas']:
    print(f'persona: {i["nombre"]} {i["edad"]}')
#ahora accedemos alas variables independientes total y mensaje que estan nivel raiz:
print(f' TOTAL PERSONAS: {json_respuesta["total"]}')
print(f'MENSAJE: {json_respuesta["mensaje"]}')






