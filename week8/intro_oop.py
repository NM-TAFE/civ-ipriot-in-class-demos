# this is an object
"Hello"
# has methods
# has attributes
# e.g. the characters H.e.l.l.o
# length
# type or class
# "kjgkjhgjhgkjhg"
#
#
# [1, 2, 3]

class Feline:
    def __init__(self, name, color=None):
        print("Feline init")
        self.name = name
        self.color = color
        self.age = 42

class DomesticCat(Feline):
    def __init__(self, name, color="Tabby"):
        super().__init__(name, color)
        print("DomesticCat init")
        self.is_cute = True
        self._owner = None


    def assign_owner(self, name):
        self._owner = name

    def meow(self):
        print(f"{self.name} meows")

DomesticCat("Lenny")._owner = "Some psycho "
class Tiger(Feline):
    pass

# tiger = Tiger("RRRRaf")
Tiger
print("Making a cat")
cat1 = DomesticCat("Lenny")
print("Done making a cat")
feline = Feline("FeeFee")
# cat1.eat("cat food")
# print(dir(cat1))
# cat = Cat("Lenny")
# cat2 = Cat("Kenny", "Tuxedo")
# print(type(cat))
# print(type(cat2))
# print(type("hello"))
# print(type(42))
# # cat.name = "Lenny"
# # cat2.name = "Kenny"
# print(cat.name)
# print(cat2.name)
# print(f"{cat.color = }")
# cat3 = Cat("Jenny")
# cat2.meow()
# cat.meow()
# cat3.assign_owner("Raf")
# print(f"{cat3.owner = }")