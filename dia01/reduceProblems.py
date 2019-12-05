from functools import reduce

#reduce no es capaz de hacer como en estas funciones y comenzar en 0
def SumatorioClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor
    return resultado

def SumatorioDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor *2
    return resultado

def PorductoTotal(l):
    resultado = 1
    for valor in l:
        resultado *= valor
    return resultado


lista = [1,3,-1,15,9]
sumatorio = reduce(lambda x, y: x + y, lista)

# para que reduce no coja el primer item sin aplicar el *2, debemos inicializar la lista en 0 de la siguiente manera
#hago una copia de la lista para no alterar la original
l = lista[:]
#en la posicion 0 pones 0
l.insert(0,0)
sumatorioDobles = reduce(lambda x, y: x +y*2, l)

print(sumatorio)
print(sumatorioDobles)