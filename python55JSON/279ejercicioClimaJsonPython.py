import json
import urllib.request

respuesta=urllib.request.urlopen('https://globalmentoring.com.mx/api/clima.json')
print(respuesta)

#convirtiendo a cuerpo binario
cuerpo_respuesta=respuesta.read()
print(f'binario: {cuerpo_respuesta}')

#convirtiendo a json con cotejamiento -utf8
json_respuesta=json.loads(cuerpo_respuesta.decode('-utf8'))
print(f'JSON: {json_respuesta}')
print(type(json_respuesta)) #se convirtio en dictionario que gozu :v


#recuperando datos del archivo json
#imprimimos el clima 0 1er clima xd

for i in json_respuesta['clima']:
    print ( f'arrayclima  -->principal:{i [ "principal" ]} descripcion: {i [ "descripcion" ]}' )
    

print(f'principal: {json_respuesta["principal"]}') #si json con llaves{}"" el objeto se respeta y el vector []'' igual
print(f'id: {json_respuesta["id"]}')


#ejercicio1 acceder ala descripcion del clima 2 soluciones:
#description_clima=json_respuesta.get('clima')[0].get('descripcion')
description_clima=json_respuesta['clima'][0]['descripcion']

#ejercicio2 mostrar la temperatura minima y maxima

temp_min=json_respuesta.get('principal').get('temp_min')#ya es dictionario ahcemos lo que qureamos xd
print(f'temperatura minima: {temp_min}')
temp_max=json_respuesta.get('principal').get('temp_max')
print(f'temperatura maxima: {temp_max}')

