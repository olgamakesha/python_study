class Animal:
    instances_count = 0

    def __init__(self):
        Animal.instances_count = Animal.instances_count + 1

    @staticmethod
    def getInstancesCount():
        print(Animal.instances_count)

    def voice(self):
        pass


class Cat(Animal):
    def voice(self):
        print("i am a cat")


class Hourse(Animal):
    def voice(self):
        print("I am a hourse")


class Dog(Animal):
    def voice(self):
        print("I am a dog")


cat = Cat()

hourse = Hourse()

dog = Dog()

Animal.getInstancesCount()