x = [5,2,3,10,8,9] 
print (x)
def ordenar(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista
print(ordenar(x))

