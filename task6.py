class Animal:
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
cat.voice()

hourse = Hourse()
hourse.voice()

dog = Dog()
dog.voice()
