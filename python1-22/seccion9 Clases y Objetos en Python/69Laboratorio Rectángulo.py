#CLASE ARITMETICA

class rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.altura*self.base
    
re1=rectangulo(2,4)


print(f'EL AREA ES: {re1.area()} ')
