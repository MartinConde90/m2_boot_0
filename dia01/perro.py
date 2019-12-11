class Dog(): #ésta clase es como las siguintes, pero teniendo que meter los atributos de uno en uno
    def __init__(self):
        self.nombre = ''
        self.edad = None
        self.peso = None
        
    def ladrar(self):
        if self.peso == None:
            print('Soy un fantasma')
            return
        
        if self.peso >=8:
            print('GUAU, GUAU')
        else:
            print('Guau, guau')
    
class Perro(): #clase
    def __init__(self, n, e, p): #constructor
        self.nombre = n #atributos
        self.edad = e
        self.peso = p
    
    def ladrar(self): #el self se rellena solo
        if self.peso >=8:
            print('GUAU, GUAU')
        else:
            print('Guau, guau')
            
    def __str__(self):
        return 'Perro {}, e: {}, p: {}'.format(self.nombre, self.edad, self.peso)
        
class PerroAsistencia(Perro): #con esto, python ya sabe que uno hereda del otro
    def __init__(self,nombre,edad,peso,amo):
        Perro.__init__(self,nombre,edad,peso)
        self.amo = amo
        self.__trabajando = False
        
    def __str__(self): #cuando se repite una de la anterior, hace primero en la que está, va por jerarquia
        return 'Perro de asistencia de {}'.format(self.amo)
    
    def pasear(self):
        print('{} ayudo a mi dueño, {} a pasear'.format(self.nombre, self.amo))

    def ladrar(self):
        if self.trabajando:
            print('shhhh, no puedo ladar')
        else:
            Perro.ladrar(self)
    
    def trabajando(self, valor = None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor

rantanplan = PerroAsistencia('RanTanPlan', 4, 7, 'Lucky Luck')
brandon = Perro('Brandon', 6,21)
miko = Dog()

miko.edad = 10
miko.peso = 1
miko.nombre = 'Miko'
print(miko.nombre, miko.ladrar())

print(brandon.nombre)
print(brandon.peso)
print(brandon.edad)
brandon.peso = 21.5 #para cambiar un dato
print(brandon.peso)
print(brandon.ladrar())
print(brandon)

rantanplan.trabajando = True
print(rantanplan.ladrar())
print(rantanplan)
print(rantanplan.pasear())