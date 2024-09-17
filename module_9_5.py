class StepValueError(ValueError):
pass

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start 
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
            
        current = self.pointer
        self.pointer += self.step 
        return current

     try:
    iterator1 = Iterator(1, 10, 2)
    for num in iterator1:
        print(num)

    iterator2 = Iterator(10, 1, -2)
    for num in iterator2:
        print(num) 

    iterator3 = Iterator(0, 5, 0)
except StepValueError as e:
    print(f'Ошибка: {e}')