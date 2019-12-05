from functools import reduce

lista = [1,3,-1,15,9]

#map actua sobre cada uno de los items de entrada
listaDobles = map(lambda x: x*2,lista )
#[2, 6, -2, 30, 18]

#filter nos devuelve solo los items que cumplen la condicion
listaPares = filter(lambda x: x % 2 == 0, lista)

#reduce usa el primer parametro como acumulador y el segundo como siguiente item a acumular
sumatorio = reduce(lambda x, y: x + y, lista) #27
sumatorioDobles = reduce(lambda x, y: x +y*2, lista) #53
suma100 = reduce(lambda x, y: x + y, range(101)) #5050

print(list(listaDobles))
print(sumatorio)
print(sumatorioDobles)
print(suma100)