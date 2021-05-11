class Underscore:
    def filter(self, iterable, callback):
        lista = list(filter(callback, iterable))
        return lista
_ = Underscore()
evens = _.filter([1,2,3,4,5,6], lambda x: x%2==0) # debe retornar [2,4,6]
print (evens)
