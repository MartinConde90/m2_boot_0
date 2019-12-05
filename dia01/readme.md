def sumaTodos(limitTo):
    resultado = 0
    for i in range(0, limitTo+1):
        resultado +=i
        
    return resultado

def sumaTodosLosCuadrados(limitTo):
    contador = 0
    for i in range(limitTo+1):
        contador += i*i
    
    return contador



print(sumaTodos(100))
print(sumaTodosLosCuadrados(5))