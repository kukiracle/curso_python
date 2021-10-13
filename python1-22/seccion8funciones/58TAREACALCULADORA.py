#Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
#La función se llama calcular_total()
#La función recibe dos parámetros:
#1. pago_sin_impuesto
#2. impuesto (Ej. Valor de 10, significa 10% de impuesto, Valor de 16 significa el 16% de impuesto)
#La función debe regresar el total del pago incluyendo el porcentaje de impuesto proporcionado.
#Ej. Si llamamos a la función calcular_total(1000, 16) debe retornar el valor 1,160.0
#Los valores los debe proporcionar el usuario y se procesados con la función input, convirtiendolos a tipo float.


def calcular_total(pago_sin_impuesto,impuesto):
      impuesto=pago_sin_impuesto*(impuesto/100)
      total_pagar=impuesto+pago_sin_impuesto
      print(f'PAGO SIN IMPUESTO= {pago_sin_impuesto}, IMPUESTO= {impuesto}, TOTAL PAGAR= {total_pagar}')
      
      
      
calcular_total(1000,16)
calcular_total(1000,16)