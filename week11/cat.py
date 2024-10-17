# %%
class Cat: # PascalCase
    def __init__(self, name, coat):
        self.is_cute = True
        self.lives = 9
        self.coat = 'Tabby'
        self.name = name
        self.coat = coat

    def meow(self):
        return f'{self.name} meows'



cat = Cat('Lenny', 'Tabby')
cat1 = Cat('Kenny', 'Tuxedo')
cat1.lives -= 1
print(cat.name, cat.is_cute, cat.lives, cat1.name, cat1.lives)
print(cat.meow())


#


