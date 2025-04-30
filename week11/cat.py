import random

class Cat:
    # short for initialise
    def __init__(self, name, is_cute, age, coat):
      self.name = name
      self.is_cute = is_cute
      self.age = age
      self.coat = coat
      self.call = random.choice(["meow", "purr", "nyaa", "miaow", "mraoow"])

    def speak(self):
        print(self.call)

    def eat(self):
        print("gobble gobble snarf food")

# class Example():
#     def something(self):
#         print("hello")

if __name__ == "__main__":
    # ex = Example()
    ex.something()
    rafs_cat = Cat("Lenny", True, 2, "Tabby")
    paras_cat = Cat("Imaginary", True, 0, "Iridescent")
    print(rafs_cat.name)
    rafs_cat.speak()
    rafs_cat.speak()
    rafs_cat.eat()
    print(paras_cat.name)
    paras_cat.speak()
    paras_cat.speak()
