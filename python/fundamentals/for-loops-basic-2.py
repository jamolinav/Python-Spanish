# 1.- Tamaño grande
def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = 'big'
    return arr
print (biggie_size([- 1, 3, 5, -5]))

# 2.- Contar positivos
def count_positives (arr):
    count = 0
    for var in arr:
        if var > 0:
            count += 1
    arr[len(arr)-1] = count
    return arr
print (count_positives([- 1,1,1,1]))

# 3.- Suma total 
def sum_total (arr):
    sum = 0
    for var in arr:
        sum += var
    return sum
print (sum_total([1,2,3,4]))

# 4.- Promedio
def promedio (arr):
    sum = 0
    for var in arr:
        sum += var
    return sum / len(arr)
print (promedio([1,2,3,4]))

# 5.- Longitud
def longitud (arr):
    return len(arr)
print(longitud ([37,2,1, -9]))
print(longitud ([]))

# 6.- Mínimo
def minimo(arr):
    if len(arr) == 0:
        return False
    min = arr[0]
    for var in arr:
        if min > var:
            min = var
    return min
print (minimo([37,2,1, -9]))
print (minimo([]))


# 7.- Maximo
def maximo(arr):
    if len(arr) == 0:
        return False
    max = arr[0]
    for var in arr:
        if max < var:
            max = var
    return max
print (maximo([37,2,1, -9]))
print (maximo([]))

# 8.- Análisis final
def ultimate_analysis(arr):
    dictionary = {}
    sum = 0
    max = arr[0]
    min = arr[0]
    for var in arr:
        if max < var:
            max = var
        if min > var:
            min = var
        sum += var
    dictionary['totalTotal'] = sum
    dictionary['promedio'] = sum / len(arr)
    dictionary['minimo'] = min
    dictionary['maximo'] = max
    dictionary['longitud'] = len(arr)
    return dictionary
print (ultimate_analysis([37,2,1, -9]))

# 9.- Lista inversa
def reverse_list (arr):
    return arr[::-1]
print (reverse_list([37,2,1, -9]))


