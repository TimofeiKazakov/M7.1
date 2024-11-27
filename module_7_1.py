class Product:
    __file_name = 'products.txt'

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop(Product):

    def __init__(self, name, weight, category, __file_name='products.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        product_str = file.read()
        file.close()
        return product_str

    def add(self, *products):
        for i in products:
            product = (str(i))
            file = open(self.__file_name, 'r')
            products = file.read()
            file.close()
            if product in products:
                print(f'Продукт {product} уже есть в магазине')
            else:
                _file = open(self.__file_name, 'a')
                _file.write(f'\n{product}')
                _file.close()


s1 = Shop(' ', 0, ' ')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())