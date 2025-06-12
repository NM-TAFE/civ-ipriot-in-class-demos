# file: cat.py

class Cat:
    enunciation = "Meow"
    def __init__(self, name, coat):
        self.name = name
        self.coat = coat
        assert "moo" not in self.enunciation.lower()

    def speak(self):
        return f"{self.name} with {self.coat} {self.enunciation}"

# as bad as the OG code was no errors without instantiating
# even instantiating doesn't reveal anything unless we have a contract
Cat("Kenny", "Tuxedo")
# what do you instantiate with?? It is only when we said "name" and "coat"
# that the first error was revealed.
c = Cat("Kenny", "Tuxedo")
# instantiating alone is not enough - we never called speak so all its problems
# remain hidden

response = c.speak()
# print(response)
# assert "meow" in response.lower()
