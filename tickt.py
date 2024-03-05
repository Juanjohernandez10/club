#elaborar programa en python que permita establecer el cobro de un tickt aereo teniendo en cuenta lo siguiente.

#valor de tickt

#1.vip -5%
#2.turista - 10%
#3.economico - 15%

#presupuesto 

#calcular el valor total del cliente 
import os
os.system ('cls')
nombreStr = input('nombre -> ')
edadInt = int ( input('edad -> '))
valor_TicketsFloat = float(input('Valor del ticket -> '))
cons_tickt_vip = 0.05
cons_tickt_turismo = 0.10
cons_tickt_economico = 0.15


opcion = int(input('\n. \n1. vip \n2.turismo \n3. economico \n4.factura \n opción -> '))

    
if opcion == 1:
    valor_total= valor_TicketsFloat * cons_tickt_vip
    valor_pagar = valor_TicketsFloat -  valor_total
    print('su valor a pagar es:',valor_pagar)
if opcion == 2:
    valor_total = valor_TicketsFloat * cons_tickt_turismo
    valor_pagar = valor_TicketsFloat - valor_total
    print('su valor a pagar es:' ,valor_pagar )    
if opcion == 3 :
    valor_total = valor_TicketsFloat * cons_tickt_economico
    valor_pagar = valor_TicketsFloat - valor_total
    print('valor a pagar es:', valor_pagar)

if opcion == 4:
    print('-----FACTURA-----')
    print(f'Nombre: {nombreStr}')
    print(f'Edad: {edadInt}')
    print(f'Tipo de ticket: {["VIP", "Turismo", "Económico"][opcion-1]}')
    print(f'Valor del ticket: {valor_TicketsFloat}')
    print(f'Descuento: {["5%", "10%", "15%"][opcion-1]}')
    print(f'Valor a pagar: {valor_pagar}')
    print('------------------')


    

    
