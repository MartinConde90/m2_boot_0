#recursividad es que la funcion se llama a su misma
#necesidad de establecer cuando parar el bucle

def retrocontador(e):
    print('{},'.format(e),end='')
    #if e != 0, pero con esto, si le damos un numero negativo, no para
    if e > 0:
     retrocontador(e-1)
    
retrocontador(1)

def sumatorio(n):    
    if n != 0:
      return n + sumatorio(n-1)
    else:
        return 0

print(sumatorio(3))

def factorial(x):
    if x > 0:
        return x * factorial(x-1)
    else:
        return 1    
        

print(factorial(5))



