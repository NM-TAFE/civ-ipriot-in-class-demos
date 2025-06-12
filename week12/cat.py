from abc import ABC, abstractmethod

class Pet:
    def show_loyalty(self):
        print("I love you")



class Animal(ABC):
    def __init__(self, name, coat):
        self.name = name
        self.coat = coat
        self.age = 0

    @abstractmethod
    def speak(self):
        ...



class Cat(Animal):
    def __init__(self, name, coat):
        super().__init__(name, coat)
        self._lives = 9


    # polymorphism

    def speak(self):
        print(f"{self.name} meow")

class Dog(Animal, Pet):

    def speak(self):
        print(f"{self.name} woof woofs")

class Mouse(Animal):
    ...

c = Cat("Lenny", "Tabby")
d = Dog("Timmy", "spotty")
c.speak()
d.speak()
# a = Animal("Monster", "Fungus")
# a.speak()
m = Mouse("a", "b")