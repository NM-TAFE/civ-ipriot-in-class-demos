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

# sillly way:
lenny.name = "Lenny"
lenny.breed = "Tabby"
kenny.name = "Kenny"
kenny.pattern = "Tuxedo"
print(lenny.breed)
# it's silly because the whole point of a blueprint is consistency:
#       breed? pattern? ooops, forgot a name...

# All animals are equal in these ways:
class Animal:
    def __init__(self, name, diet="Vegan"):
        self.name = name
        self.diet = diet
        self._is_hungry = False # indicate an attribute or method is intended
        # to be private with a single underscore prefix
        # generally avoid double underscores


    def eat(self, food):
        if self._is_hungry:
            print(f"Yum, yummy {food}")
        else:
            print(f"No thank you!")

    def make_hungry(self):
        self._is_hungry = True


class Cat(Animal):
    def __init__(self,
                 name,
                 breed):

        super().__init__(name, diet='Carnivore') # without super() we
        # completely ignore
        # the
        # __init__ of the parent (super) class
        self.breed = breed
        self.cute = True # attributes don't have to be specified as parameters


    def meow(self):
        print(f"{self.name} meowwwww")



lenny = Cat("Lenny-roo", "Tabby")
lenny.eat('Tuna')

# print(lenny.name)