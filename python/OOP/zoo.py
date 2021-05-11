
class animal:
    def __init__(self, name, age, health, happiness):
        self.name
        self.age
        self.health
        self.happiness = 0
        self.especie
        
    def display_info(self):
        print (f'especie: {self.especie}, name: {self.name}, health: {self.health}, happiness: {self.happiness}')

    def give_food(self, val):
        raise NotImplementedError

class Lion(animal):
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        self.especie = 'Lion'
        self.rateHealth = 0.2
        self.rateHappiness = 0.2

    def give_food(self, val):
        print (type(val))
        print (type(self.rateHealth))
        self.health += val * self.rateHealth
        self.happiness += val * self.rateHappiness


class Tiger(animal):
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        self.especie = 'Tiger'
        self.rateHealth = 0.5
        self.rateHappiness = 0.5

    def give_food(self, val):
        self.health += val * self.rateHealth
        self.happiness += val * self.rateHappiness

class Bear(animal):
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        self.especie = 'Bear'
        self.rateHealth = 0.8
        self.rateHappiness = 0.8

    def give_food(self, val):
        self.health += val * self.rateHealth
        self.happiness += val * self.rateHappiness

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name, age, health, happiness):
        self.animals.append( Lion(name, age, health, happiness) )
    def add_tiger(self, name, age, health, happiness):
        self.animals.append( Tiger(name, age, health, happiness) )
    def add_bear(self, name, age, health, happiness):
        self.animals.append( Bear(name, age, health, happiness) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
    def give_food_to_lions(self, val):
        for animal in self.animals:
            if type(animal) is Lion:
                animal.give_food(val)

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 3, 4, 5)
zoo1.add_lion("Simba", 3, 4, 5)
zoo1.add_tiger("Rajah", 3, 4, 5)
zoo1.add_tiger("Shere Khan", 3, 4, 5)
zoo1.add_bear("jogi", 3, 4, 5)
zoo1.add_bear("bubu", 3, 4, 5)
zoo1.print_all_info()
print("-"*30, __name__, "-"*30)
zoo1.give_food_to_lions(2)
zoo1.print_all_info()
