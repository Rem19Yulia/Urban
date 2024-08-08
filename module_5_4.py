class House:
    houses_history = []

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.__class__.new(name)
    
    @classmethod
    def new(cls, *args):
        cls.houses_history.append(args[0])

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")
    
    def __len__(self):
        return self.number_of_floors
    
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

