class Animal:

    def sound(self):
     pass


class Dog(Animal):

    def sound(self):
        return "Bark"

x0 = Animal()
print(x0.sound())
x1 = Dog()
print(x1.sound())


