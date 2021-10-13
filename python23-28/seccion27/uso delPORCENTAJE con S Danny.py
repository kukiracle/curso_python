# x='patron %s'
# y=x%'cambio'
# print (y)
# z='%s|%s|%s|%s'%('h1','h2','h3','h4')
# print(z)
# # s de strings xd
# #d de decimales :v
# #f de flotantes :3
# w='%d %.10f'%(10.123456,12.987654)
# print(w)
# 
# 
# 
def decorado ( funcionb):  #funcionb es la funcion mensaje()
    def funcionc():
        print('decoradazo')
        funcionb()        
    return funcionc 


@decorado
def mensaje():
    print('hola')
    
mensaje()