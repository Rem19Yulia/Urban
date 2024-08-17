class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


# Создаем объект класса Pegasus
pegasus = Pegasus()

# Проверяем все методы
pegasus.run(10)  # Лошадь пробегает 10 единиц
pegasus.fly(20)  # Орел поднимается на 20 единиц
pegasus.move(5, 15)  # Пегас движется с изменением

# Получаем текущее положение
print("Текущее положение пегаса:", pegasus.get_pos())

# Проверяем звук
print("Звук пегаса:", end=' ')
pegasus.voice()