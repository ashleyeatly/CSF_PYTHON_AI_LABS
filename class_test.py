class SomeClass:
    def __init__(self):
        print("Instanciated")
        print(SomeClass())


# abc = SomeClass()
# print(abc)

class DemoClass:
    num = 101

    # parameterized constructor
    def __init__(self, data):
        self.num = data

    # a method
    def read_number(self):
        print(self.num)


# creating object of the class
# this will invoke parameterized constructor
obj = DemoClass(55)

# calling the instance method using the object obj
obj.read_number()

# creating another object of the class
obj2 = DemoClass(66)

# calling the instance method using the object obj
obj2.read_number()


print("The itsy bitsy spider\n  climbed up the waterspout.")
print()
print("Down came the rain\n and washed the spider out.")

print("My name is", "Python.", end=" ")

print("Monty Python.")
print("My", "name", "is", "Monty", "Python.", sep="-")
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print("Programming","Essentials","in",sep="***",end="")
print("...","Python",sep="")

class MyClass:
    x = 5
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return((self.height) * (self.width))

    def perimeter(self):
        return((self.height * 2) + (self.width * 2))

xyz = Rectangle(12, 11)
print(xyz.area())
print(xyz.perimeter())

class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

class ElectricCar(Car):

    def __init__(self, make, model, year, color, battery_life):
        super().__init__(make, model, year, color)
        self.battery_life = battery_life

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def balance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

abc = BankAccount(1000)
print(abc.balance())
print(abc.withdraw(10))
print(abc.deposit(20))


