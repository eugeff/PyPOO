print('Ejercicio Nº1')

def utilizarnumero(numero):
    n=0
    inserto = numero 
    while n<5:
        n += 1
        if numero<2: 
              print('Es menor que 2')
              numero += 3
        elif numero==2:
             print ('Es igual a 2')
             numero += 1
        else:
              print ('Es mayor que 2') 
              numero -=3
    print(inserto)       

utilizarnumero(5)       

