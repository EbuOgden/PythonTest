class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("{} is eating a/an {}".format(self.name, food))

class Dog(Animal):

    def a(self):
        print("a")

a = Dog("Bark")
a.eat("beef")
a.a()
