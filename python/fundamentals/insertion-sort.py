x = [5,2,0,10,8,9,1,1,7,6,6]
def ordenar(lista):
    for i in range(1, len(lista)):
        for j in range(i, 0, -1):
            if lista[j] < lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
    return lista
print(ordenar(x))
