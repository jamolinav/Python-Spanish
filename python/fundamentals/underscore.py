import functools

class Underscore:
    def map(self, iterable, callback):
        # tu cÃ³digo aqui
        lista = list(map(callback , iterable))
        return lista
    def find(self, iterable, callback):
        # tu cÃ³digo aqui
        lista = list(map(lambda x: x if callback(x) else None , iterable))
        lista = [i for i in lista if i ]
        return lista[0] if len(lista) > 0 else None
    def filter(self, iterable, callback):
        # tu cÃ³digo aqui
        lista = list(map(lambda x: x if callback(x) else None , iterable))
        lista = [i for i in lista if i]
        return lista
    def reject(self, iterable, callback):
        # tu cÃ³digo 
        lista = list(functools.reduce(callback, iterable))
        return lista
# has creado una libreria con 4 mÃ©todos
# se crea la instancia de la clse
_ = Underscore() # sÃ­, estamos configurando una instancia a una variable que es un guiÃ³n bajo

evens = _.map([1,2,3], lambda x: x*2) # debe retornar [2,4,6]
print (evens)
evens = _.find([1,2,3,4,5,6], lambda x: x>4) # debe retornar el primer valor que es mayor que 4
print (evens)
evens = _.filter([1,2,3,4,5,6], lambda x: x%2==0) # debe retornar [2,4,6]
print (evens)
evens = _.reject([1,2,3,4,5,6], lambda y, x: x%2==0) # debe retornar [1,3,5]
print (evens)
# debe retornar [2, 4, 6] despuÃ©s que termines de implementar el cÃ³digo de arriba