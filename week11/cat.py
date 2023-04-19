class Cat:
    def meow(self):
        print("meowwwww")

# create a new instance of a cat from the blueprint

lenny = Cat()

# these are identical
Cat.meow(lenny)
lenny.meow()
# which is clearer?
#####################
kenny = Cat()
lenny.meow()
kenny.meow() # lenny and kenny are identical!
# how to we introduce attributes to these cats?
# Lenny is name=Lenny, breed=Tabby
# Kenny is name=Kenny, breed=Tuxedo*
# *Tuxedo is not a breed it's a colour!
# ** STOP PRESS ** Tabby is also a colour scheme!!

# sillly way
lenny.name = "Lenny"
lenny.breed = "Tabby"
kenny.name = "Kenny"
kenny.pattern = "Tuxedo"
print(lenny.breed)

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"Yum, yummy {food}")


class Cat(Animal):
    def __init__(self,
                 name,
                 breed):
        self.name = name
        self.breed = breed
        self.cute = True

    def meow(self):
        print(f"{self.name} meowwwww")

lenny = Cat("Lenny-roo", "Tabby")
lenny.eat('Tuna')
# print(lenny.name)