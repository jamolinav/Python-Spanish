# 1.- Cuenta regresiva
def cuentaRegresiva(num):
    arr = []
    for i in range(num+1):
        arr.append(i)
    return arr[::-1]

arr = cuentaRegresiva(15)
print (arr)


# 2.- Imprimir y volver
def print_and_return (arr):
    print (arr[0])
    return arr[1]

print (print_and_return([3,6]))

# 3.- First Plus Length
def first_plus_length(arr):
    return arr[0]+len(arr)
print(first_plus_length([6,2,3,4,5,6]))

# 4.- Valores mayores que el segundo
def values_greater_than_second (arr):
    arr_result = []
    for val in arr:
        print (val)
        if val > arr[1]:
            arr_result.append(val)
    return arr_result
print(values_greater_than_second ([5,2,3,2,1,4]))

# 5.- Esta longitud, ese valor
def length_and_value (size,num):
    arr = []
    for i in range(size):
        arr.append(num)
    return arr
print(length_and_value (4,7))

