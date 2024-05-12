# Overview

In this lesson, we will cover testing in Python. Our emphasis will be on testing using the `unittest` module and we'll look at testing classes and class definitions.

By the end of this lesson, you should be able to:

- Structure a Python project in PyCharm to support testing.
- Write test classes using the `unittest` module.
- Apply best practices when writing tests.

## Structuring Python projects

As we enter the realm of object-oriented programming (OOP), you've probably noticed that our Python projects are starting to consist of multiple files. Remember, as a general rule, we create one file per class definition. And we want to group files related to the same application together. As we add testing to the mix, we typically test our classes from a different file, so that even our simple example of `Animal`, `Cat`, and `Dog` from last week will need at least seven files: one for each class, one for each test class, and one for the main program.

To keep things organized we tend to follow standard folder structures (though Python itself does not dictate a particular structure). Here's a common structure for a Python project:

```text
project/
│
├── src/
│   ├── __init__.py
│   ├── animal.py
│   ├── cat.py
│   └── dog.py
│
├── test/
│   ├── __init__.py
│   ├── test_animal.py
│   ├── test_cat.py
│   └── test_dog.py
│
├── .git/
├── .gitignore
├── README.md
└── main.py
```

Notice the following:

- We often keep tests and source code in separate folders.
- Each folder has an `__init__.py` file to make it a package. Since Python 3.3 (a long time ago), this file is not strictly necessary, but it's still a good practice.
- The `__init__.py` file can be empty, but it can also contain initialization code for the package. In our examples, we'll keep it empty.
- The `main.py` file is the entry point for the application. It's where we'll instantiate our classes and run our program.
- The `README.md` file is a good place to document the project.
- The "root" of our project in PyCharm is usually the root of the git repository.

### Activity

Take the time to organize last week's activities into the above folder structure, if you are missing any of these files, create empty files for now.

Continue only when you have done the above.

## Main program, and if **name** equals "**main**"

In many programming languages we define a `main` entry point for our program. In Python, any file can potentially be a main (basically, a script) if we run it as main and main methods and programs and not required but they make life easier.

### Modules versus scripts

In Python, a **module** is a file containing Python definitions and statements. A **script** is also a file containing Python definitions and statements. So what is the difference?

Answer: **The only difference is how you execute the file.**

When you import a Python file, it is a module. When you run it directly, it is a script. It's important to recognize that in **both** cases the code is executed - top to bottom. There is only one small but crucial difference: when you run a script, the special variable `__name__` is set by Python to `__main__`. When you import a module, `__name__` is set to the name of the module.

This is why you will often see code that looks like this:

```python
# file: cat.py
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} Meows"

def main():
    cat = Cat("Whiskers")
    print(cat.speak())

if __name__ == "__main__":
    main()
```

This pattern allows us to _effectively_ use the above file as both a module that only contains definitions and as a script that executes those definitions. When we run the file, the `main()` function is called. When we import the file, the `main()` function is not called.

### Writing `main.py`

In our project structure, we have a `main.py`, think of that as an entry point for the overall program, potentially integrating all the classes we've written so far. It's a good place to instantiate our classes and run our program.

```python
# file: main.py
from src.cat import Cat
from src.dog import Dog


cat = Cat("Whiskers")
dog = Dog("Fido")

cat.speak()
dog.speak()

cat.meet(dog)
```

Notice that because our files were in the subfolder (with or without an `__init__.py`) Python treats them as a package and we can import them using the `.` notation.

However, `src` is a spurious name and in our case we want to treat the `src` folder as the root of our project files. We can do this by adding the root of our project to the Python path. This is done by adding the following code to the top of `main.py`:

```python
import sys
sys.path.append("src")
```

Alternatively, we can set the `PYTHONPATH` environment variable to include the `src` folder. This is done by running the following command in the terminal:

```bash
export PYTHONPATH=$PYTHONPATH:src
```

Or, most easily, we can **mark the `src` folder as a source root** in PyCharm. This is done by right-clicking on the `src` folder and selecting `Mark Directory as` -> `Sources Root`.

> IMPORTANT: You only need to know about that last approach in this course. The other approaches are useful to know about, but you don't need to use them.

### Simple testing

#### Definitions mask errors

When we create definitions (let's imagine we are writing a component in a larger project) the act of creating definitions and getting a return code 0, doesn't tell us very much: it just tells us Python could _parse_ the file, which only covers syntax errors (for example, missing colons, or mismatched parentheses). It doesn't tell us if the code is correct or if it works as expected.

```python
# file: cat.py
class Cat:
    def __int__(name, coat):
        self.name = nam
        coat = coat
        oopsy

    def speak(self):
        self.speak()
        return f"{self.name} with {self.coat} Moos"
```

Do you think this code will run? Write down everything that's wrong with it (there are at least seven serious errors)

Write down every error you found:

> 1.
> 2.
> 3.
> 4.
> 5.
> 6.
> 7.

Without fixing the code, try running it! The result may surprise you.

That's right. If you accurately copied this code, it should run without raising any exceptions. Yeaks.

The very least we can do is just try and instantiate our definitions and see if that works. This will actually find a lot more bugs.

```python

# Add the following to the end of the file:

def test():
    cat = Cat("Whiskers", "black")
    cat.speak()

if __name__ == '__main__':
    test()

```

By adding the previous snippet, you'll now (and only now) find six of the errors above. But it is still not enough. Notice that our testing didn't reveal the fact that our cat, rather than meowing, is mooing! We need some way to _assert_ that a cat should meow! We can't just leave it to careful observation.

### The `assert` statement

The `assert` statement is used to check if a condition is true. If the condition is false, the program will stop with an `AssertionError`.

```python
a = 42
assert a == 42 # True -> runs
assert a == 43 # False -> raises an AssertionError
```

> Add an assert statement to the `test()` function above to check that the cat meows. Only after the program **fails** fix the error and ensure you get a return code 0!

### What are the issues with that?

Okay, so so long as we drive our definitions, maybe add a couple of assert statements, we should be good, right? Well, not quite. There are a few issues with this approach:

1. **It's manual**: We have to remember to run our tests every time we make a change.
2. **We can only discover one error at a time**: If we have multiple errors, we have to fix one, run the tests, fix the next, run the tests, and so on.
3. **It's not standardized**: Why did I create a function called `test()` and not `run_tests()`?
4. **I didn't test importing**: Would importing the module and then running the tests work? I don't know. I hope so.

There is no clear separation between the tests and the code. There is no standard way to run the tests, particularly as the number of modules grows. We need a better way.

## The `unittest` module

The `unittest` module is a testing framework that comes with Python. It makes it easy to write tests for your code. It's based on the XUnit framework, which is a testing framework for many languages. It is object-oriented and has a lot of features, but we'll only cover the basics. The fact that it is object-oriented and modeled after a framework from other languages, is why it might seem a bit unusual to Python developers.

### Writing a test case

Some rules for writing a test case:

- Usually, create one test case for each class you want to test. Either prefix the file name with `test_` or suffix it with `_test` - whichever you choose, stick to it.
- Create a class that inherits from `unittest.TestCase`.
- Create methods that start with `test_` that test the functionality of your code (not optional)
- (Optional) Use the `setUp` method to create objects that are used in multiple tests (think, **arrange**). Unlike an **init** method, `setUp` is called before every test method.
- Give your test methods descriptive names that describe exactly what you are. Each test method should test one thing.

```python
import unittest
from cat import Cat # will work if you have the PYTHONPATH set

class TestCat(unittest.TestCase):

    def test_speak(self):
        # arrange
        cat = Cat("Whiskers", "black")

        # act
        result = cat.speak()

        # assert
        self.assertContains(result, "meows")
        self.assertContains(result, "Whiskers")
        selfassertNotContains(result, "moo")

```

> Are you getting warnings in PyCharm? Mark the `tests` folder as test sources root: right-click on the folder and select `Mark Directory as` -> `Test Sources Root`.

### Running the tests

To run the tests, you can run the following command in the terminal:

```bash
python -m unittest discover tests
```

Alternatively you can run the tests from PyCharm by right-clicking on the `tests` folder and selecting `Run 'Unittests in tests'`.

## Activity: Define Tests

Write tests for the other methods in the `Cat` class. And then create the dog class. Try the buggy cat class we create early and see how well your tests go catching the errors?
