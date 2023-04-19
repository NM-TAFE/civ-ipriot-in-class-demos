# the simplest class possible
class Cat:
   pass

# in older versions of python you may see this
class Cat(object):
        pass
# This is an older style that achieves the same thing

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


