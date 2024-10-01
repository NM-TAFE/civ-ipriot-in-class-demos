class Cat:
    def __init__(self, name, age,coat_color):
        self.name = name
        self.age = age
        #ex1
        self.coat_color = coat_color

    def meow(self):
        print(f'{self.name} says "Meow"')

    #ex2
    def purr(self):
        print(f'{self.name} purrs')

#ex 3
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #Ex4
    def bark(self):
        print(f'{self.name} barks')










def exercise_1():
    cat1 = Cat("Apples", 20, "ffffff")
    print(cat1.name,
          cat1.age,
          cat1.coat_color)
def exercise_2():
    cat1 = Cat("Apples", 20, "ffffff")
    cat1.purr()
def exercise_3():
    dog1 = Dog("Oranges", 2000)
    print(dog1.name,dog1.age)
def exercise_4():
    dog1 = Dog("Oranges", 2000)
    dog1.bark()

def main():
    exercise_3()
    pass

if __name__ == "__main__":
    main()
