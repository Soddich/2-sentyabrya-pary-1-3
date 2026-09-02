class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age
cat1 = Cat("британец", "Барсик", 3)
cat2 = Cat("сиамский", "Мурзик", 5)
cat3 = Cat("мейн-кун", "Лео", 2)
print(cat1.name, cat1.breed, cat1.age)
print(cat2.name, cat2.breed, cat2.age)
print(cat3.name, cat3.breed, cat3.age)