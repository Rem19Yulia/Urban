
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True 