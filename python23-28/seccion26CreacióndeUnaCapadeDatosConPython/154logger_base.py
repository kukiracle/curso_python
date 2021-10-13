import logging as log
# con esto cambiamos loggin por log lo acortamos log=logging
#tambien se puede hacer import loggin as log



log.basicConfig(level = log.DEBUG,
                format ='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('mensaje a nivel debug')
    log.info('mensaje a nivel info')
    log.warning('mensaje a nivel warniNg')
    log.error('mensaje a nivel error')
    log.critical('mensaje a nivel critico')


#%asctime= hora lanzo error,%level al que pertenece,%y el nombre del archivo,%linea error,%message
#todos estos estan en la pagina de python howtologging