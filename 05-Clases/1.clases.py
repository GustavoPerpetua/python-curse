class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"{self.name} says: Miau ! ")


my_cat = Cat("kiki", 5)
print(my_cat.name)
my_cat.talk()
