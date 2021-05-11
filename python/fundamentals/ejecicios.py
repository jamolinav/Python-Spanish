
def imp_arr(row,col):
    for var in list(range(row)):
        print ('*' * col)

def fac(num):
    factorial = 1
    for i in range(2,num+1):
        factorial *= i
    print (factorial)

def esPalindromo(palabra):
    reves = palabra[::-1]
    i = 0
    for letra in palabra:
        if letra != reves[i:i+1]:
            print ('No es palindromo')
            return
        i += 1
    print ('Es palindromo')

imp_arr(4,5)
fac(3)
esPalindromo('somosed')