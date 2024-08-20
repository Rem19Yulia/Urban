class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'
    
    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return ''.join(file.readlines())
        except FileNotFoundError:
            return 'Файл с товарами не найден.'
    
    def add(self, *products):
        existing_products = self.get_products().splitlines()
        
        for product in products:
            product_name = product.name.strip()
            if any(product_name == line.split(', ')[0] for line in existing_products):
                print(f'Продукт {product_name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')


# Пример работы программы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # Вывод: Spaghetti, 3.4, Groceries

s1.add(p1, p2, p3)

print(s1.get_products())