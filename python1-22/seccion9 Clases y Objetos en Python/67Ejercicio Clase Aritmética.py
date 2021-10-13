#CLASE ARITMETICA



class Aritmetica:
    def __init__(self,operandoA,operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    def sumar(self):
        return self.operandoA + self.operandoB
    

a1=Aritmetica(2,3)
print( a1.sumar())
   
   
   
