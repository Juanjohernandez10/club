
porcentaje_creditoFlt = 0.60
nombreStr = input('nombre -> ')
salarioFlt = float(input('salario -> '))
montoflt =float(input ( 'monto->' ))
plazoInt = int(input ('plazo en meses -> ')) 

cap_descuntoFlt = salarioFlt * porcentaje_creditoFlt
cuotaFlt= montoflt/plazoInt
if cap_descuntoFlt >= cuotaFlt:
    print(nombreStr,'su credito ha sido aprobado ')
                   