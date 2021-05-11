print("Hola Mundo")

name = "Juan"
print("Hola", name)
print("Hola " + name)

num = 7
print("Hola", num)
print("Hola " + str(num))

food_one = "pastas"
food_two = "pescados"
print("Me gusta comer {} y {}".format(food_one, food_two))
print(f"Me gusta comer {food_one} y {food_two}")


# Bonificacion NINJA

nombre = "Juan"
edad = 46
print("Mi nombre es", nombre, "y tengo", edad, "años")

nombre = "Juan"
edad = 46
print("Mi nombre es" + nombre + "y tengo" + str(edad) + "años")

print(f"Mi nombre es {nombre} y tengo {edad} años")

print("Mi nombre es {} y tengo {} años".format(nombre, edad))
print("Mi nombre es {name} y tengo {age} años".format(name = nombre, age = edad))

print("Mi nombre es %s y tengo %d años" % (nombre, edad))