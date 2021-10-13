#celsius a fahrenheit es: celsius * 9/5 + 32 
#fahrenheit a celsius es:  (fahrenheit-32) * 5/9

def cs_a_fah(celsius):
      fahren=celsius*9/5+32
      print(f' FAREN= {fahren}')
      
      
def fa_a_cs(fa):
      celsius=(fa-32)*5/9+32
      print(f' CELSIUS= {celsius}')
      


cel=float(input('Introdusca grados celsius:  '))

cs_a_fah(cel)

fa=float(input('Introdusca grados fahrenheit:  '))

fa_a_cs(fa)