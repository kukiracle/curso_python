import logging 
log=logging# con esto cambiamos loggin por log lo acortamos 
#tambien se puede hacer import loggin as log



log.basicConfig(level = log.DEBUG)
#hacia abajo entonces mostrara todos, REVISAR IMAGEN 153
if __name__== '__main__':
    log.debug('mensaje a nivel debug')
    log.info('mensaje a nivel info')
    log.warning('mensaje a nivel warniNg')
    log.error('mensaje a nivel error')
    log.critical('mensaje a nivel critico')


