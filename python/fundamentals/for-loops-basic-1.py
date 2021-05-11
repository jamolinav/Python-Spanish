
# 1.- Básico
for i in range(151):
    print(i)

# 2.-  Múltiplos de cinco
for i in range(5, 1001):
    if i % 5 == 0:
        print(i)

# otra forma
for i in range(5, 1001, 5):
    print(i)

# 3.-  Contar, Dojo Way 
for i in range(0, 1001, 5):
    print('Coding')
    if i % 10 == 0:
        print('Coding Dojo')

# 4.- ¡Uf, Eso es bastante grande!
sum = 0
for i in range(0, 500001):
    if i % 2 != 0:
        sum += i
print(sum)

# otra forma
sum = 0
for i in range(1, 500001, 2):
    sum += i
print(sum)


# 5.- Cuenta regresiva por cuatro
for i in range(2018, 0, -4):
    print(i)


# 6.- Contador flexible
lowNum  = 2
highNum = 9
mult    = 3
for i in range(lowNum, highNum+1):
    if i % mult == 0:
        print(i)