class Animal():
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name, coolness):
        super().__init__(name)
        self.coolness = coolness
