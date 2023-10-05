from dataclasses import dataclass

@dataclass
class Feline:
    name: str = "Harry"

    def eat(self):
        print("yum yum")

f = Feline("Raf")
print(f)
Feline(name='Raf')