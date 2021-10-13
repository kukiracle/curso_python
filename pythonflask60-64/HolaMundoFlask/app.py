from os import abort
from flask import Flask,request,render_template,url_for,jsonify
from werkzeug.utils import redirect #para redireccionar312
from werkzeug.exceptions import abort #313 errores flask

app = Flask(__name__)#objeto de tipo flask

#http://localhost:5000/
@app.route('/') #pagina de inicio
def inicio():
    app.logger.info(f'Entramos al path {request.path}')
    return 'hola mundo desde flask x'

#creamos otro path con string de entrada
@app.route('/saludar/<nombre>')#path que recibiremos string nombre
def saludar(nombre):#metodo sociado enrada nombre
    return f'saludos {nombre}'

#path con int
@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'tu edad es: {edad}'

@app.route('/mostrar/<nombre>', methods=['GET','POST'])#CAMBIAMOS EL TIPO DE PETICION CLIENTE
def mostrar_nombre(nombre):
    return render_template('mostrar.html',nombre_llave=nombre)
#con GET la idea es obtener informacion del servidor
#con POST la idea es insertar informacion al servidor

#312 URL Redirect
@app.route('/redireccionar')#sirve para redireccionar a otro path
def redireccionar():
    return redirect(url_for('mostrar_nombre',nombre='jorge')) #la funcion  inicio que es el index 


#313 manejo errores flask abort
@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html',error_llave=error),404#tupla

#     app.logger.debug('Mensaje nivel debug')
#     app.logger.info('Mensaje nivel info')
#     app.logger.warn('Mensaje nivel warnign')# en modo produccion solo muestra de akia bajo
#     app.logger.error('Mensaje nivel error')

#314-315 JSON Y FLASK
#aplicaiones REST Representational state trasnfer
#responderemos con codigo tipo json que es lo normal y mas comun
#tambien llamado servicios web y estos los consumen frameworkos frontend
#APIconjunto de paths que consumiran las aplicaciones de tipo frontenD
#aplication program interface
@app.route('/api/mostrar/<nombre>', methods=['GET', 'POST'])#recibimos en este path 'nombre'
def mostrar_json(nombre):
    valores={'nombre':nombre,'metodo_http':request.method}#lo guardamos en este diccionario
    return valores #mandamos el diccionario para su conversion en json
    #return jsonify(valores) toma un objeto de python y lo vuelve diccionario

