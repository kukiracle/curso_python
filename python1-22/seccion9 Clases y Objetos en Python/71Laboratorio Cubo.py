#CLASE ARITMETICA

class cubo:
    def __init__(self,base,altura,profundidad):
        self.base = base
        self.altura = altura
        self.profundidad = profundidad
    def volumen(self):
        return self.altura*self.base*self.profundidad
    

b=int(input("Introdusca BASE "))
a=int(input("Introdusca Altura "))
p=int(input("Introdusca Profundidad "))
re1=cubo(a,b,p)


print(f'EL VOLUMEN ES: {re1.volumen()} ')
