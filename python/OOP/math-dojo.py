class MathDojo:
    def __init__(self):
    	self.result = 0
    def add(self, num, *nums):
    	# tu código aquí
        self.result += num
        for i in nums:
            self.result += i
        return self
    def subtract(self, num, *nums):
    	# tu código aquí
        self.result -= num
        for i in nums:
            self.result -= i
        return self
# crear una instruccion:
md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!



