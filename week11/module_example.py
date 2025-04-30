# I've named this arbitrary method "choice" so that you can see, later, on line 11,
# that it can be used alongside random.choice, due to the power of namespaces.
def choice():
    print("conflict avoided!")

# from random import * <= This pollutes the global namespace! Don't do it.
import random
import animals

# Remember, this is a fancy way of letting a Python file be both a Script AND a Module.
# If you do an `import module_example` from another file, you'll be able to use the
# choice function defined on line 3, but it won't run the code below.
if __name__ == "__main__":
    print(choice())
    print(random.choice([1,3,5,6,7]))
    
    print("These are the animals we imported from animals.py")
    animals.giraffe()
    animals.tiger()
