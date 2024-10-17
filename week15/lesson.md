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
        this_cant_possibly_work()
        self.speak()
        return f"{self.name} with {self.coat} Moos"
```

Do you think this code will run? Write down everything that's wrong with it (find at least six serious problems)

Write down every error you found:

> 1.
> 2.
> 3.
> 4.
> 5.
> 6.
> 7.
> 8.

Without fixing the code, try running it! The result may surprise you.

That's right. If you accurately copied this code, it should run without raising any exceptions. Yeaks.

Hopefully, this shows you how little actually gets validated by running code, particularly when it consists mostly of definitions (as it usually does in OOP).

The very least we can do is just try and instantiate our definitions and see if that works. This will actually itself find a lot more bugs.

```python

# Add the following to the end of the file:

def test():
    cat = Cat("Whiskers", "black")
    cat.speak()

if __name__ == '__main__':
    test()

```

By adding the previous snippet, you'll now (and only now) be able to find at least seven of the errors above. But it is still not enough.

Try adding the code above and fix each error as it comes up. Did any of the errors you found not get caught by the test function?

...

---

Our testing didn't reveal the fact that our cat, rather than meowing, is mooing! We need some way to _assert_ that a cat should meow! We can't just leave it to careful observation.

### The `assert` statement

The `assert` statement is used to _assert_ that a condition must be true. If the condition is false, the program will raise an `AssertionError`, and usually end the program.

```python
a = 42
assert a == 42 # True -> runs
assert a == 43 # False -> raises an AssertionError KA-BOOM
```

> Add an assert statement to the `test()` function above to check that the cat meows. Only after the program **fails** fix the error and ensure you get a return code 0!

### What are the issues with that?

Okay, so so long as we drive our definitions, maybe add a couple of assert statements, we should be good, right? Well, not quite. There are a few issues with this approach:

1. **It's manual**: We have to remember to run our tests every time we make a change.
2. **We can only discover one error at a time**: If we have multiple errors, we have to fix one, run the tests, fix the next, run the tests, and so on.
3. **It's not standardized**: should we just put assertions anywhere? How do they relate to other tests? What if I just want to test the code without running the program?
4. **I didn't test importing**: Would importing the module and then running the tests work? I don't know. I hope so.

There is no clear separation between the tests and the code. There is no standard way to run the tests, particularly as the number of modules grows. We need a better way.

Keep in mind that testing code is about testing multiple pathways through the code, so just like as our code grew we needed to start organizing it, we need to start organizing our tests.

## The `unittest` module

The `unittest` module is a testing framework that comes with Python. It makes it easy to write tests for your code. It's based on the xUnit framework, which is a testing framework for many languages. It is object-oriented and has a lot of features, but we'll only cover the basics. The fact that it is object-oriented and modeled after a framework from other languages, is why it might seem a bit unusual to Python developers.

### Writing a test case

Some rules for writing a test case:

- Usually, create one test case for each class you want to test. Either prefix the file name with `test_` or suffix it with `_test` - whichever you choose, stick to it.
- Create a class that inherits from `unittest.TestCase`.
- Create methods that start with `test_` that test the functionality of your code (not optional)
- (Optional) Use the `setUp` method to create objects that are used in multiple tests (think, **arrange**). Unlike an **init** method, `setUp` is called before every test method.
- Give your test methods descriptive names that explain exactly what you are testing. Your test case name should make it clear why it matters. For example:
  - `test_speak` is better than `test_1`
  - `test_cat_meows` is better than `test_speak`
  - `test_plane_fly_method_when_t_equals_true` is **not** as good as `test_plane_can_fly_in_turbulence` :)
- Each test method should test one thing.

```python
# in tests/test_cat.py
import unittest
from cat import Cat # will work if you have the PYTHONPATH set

class TestCat(unittest.TestCase):

    def test_speak(self):
        # arrange
        cat = Cat("Whiskers", "black")

        # act
        result = cat.speak()

        # assert
        self.assertIn(result, "meows")
        self.assertIn(result, "Whiskers")
        self.assertNotIn(result, "moo")

```

> Are you getting warnings in PyCharm? Mark the `tests` folder as test sources root: right-click on the folder and select `Mark Directory as` -> `Test Sources Root`.

### Running the tests

To run the tests, you can execute the following command in the terminal:

```bash
python -m unittest discover tests
```

Alternatively you can run the tests from PyCharm by right-clicking on the `tests` folder and selecting `Run 'Unittests in tests'`.

## Activity: Define Tests

Write tests for the other methods in the `Cat` class. And then create the dog class. Try the buggy cat class we create early and see how well your tests go catching the errors?

## Intermediate topics

Optional (but recommended) primers on more advanced topics

### KISS your tests

The key to writing good tests is to write simple tests and the key to writing simple tests is to write code that can be tested simply.

So as much as you can keep it simple (KIS). However, sometimes it is hard to avoid some complexity, this can arrise when tests require a lot of set up, or when your program must predominantly produce side effects, or when you have to test varied and complex interactions and inputs.

### Testing for exceptions

Sometimes you want to test that a function or method raises an exception. You can do this with the `assertRaises` method. This method takes the exception you expect to be raised and the function you want to test. Because the function should raise an exception, we can't just call it because it will, well raise an exception, we need to either create a safe context for the exception to be raise in (`with`), or pass the function/method and its arguments as parameters to the `assertRaises` method.

Consider:

```python

class Cat:
    # other code
    def meet(self, other):
        if not isinstance(other, Cat):
            raise ValueError("Only willing to meet other cats")
        return f"{self.name} meets {other.name}"

```

Here we want to test that when a cat meets a non-Cat type, a `ValueError` is raised. We can do this with the following test:

```python

# imports...

class TestCat(unittest.TestCase):

    def test_meet(self):
        # arrange
        cat = Cat("Whiskers", "black")
        dog = Dog("Rex", "brown")

        # act and assert
        with self.assertRaises(ValueError):
            cat.meet(dog)

```

This is the preferred way to test exceptions. You can also use the `assertRaises` method without a `with` statement, but we think it is less readable:

```python
# in test class
    def test_meet(self):
        # arrange
        cat = Cat("Whiskers", "black")
        dog = Dog("Rex", "brown")

        # act and assert
        self.assertRaises(ValueError, cat.meet, dog)
```

Notice that the cat.meet method is passed to the `assertRaises` method - not called directly. This is because if we called it directly, the exception would be raised before the `assertRaises` method could catch it.

### Testing fruitful and void functions/methods

You may remember from introductory programming how we distinguished between functions that return a value and those that don't. Sometimes, they may be referred to as **fruitful** and **void** functions (in Python, recall, even void functions return a value – a `NoneType`).


Since void functions don't exist for the purpose of returning a value, we also say that we use them for their side effects. For example, a function that prints something to the console is a void function - it produces a side effect (printing to the console) but returns `None`.

As a general rule it is easier to test fruitful functions than void functions. This is because we can test the return value of a fruitful function, but we can't test the return value of a void function.

The best way to test void functions is not to have them - minimize the number of void functions. Most of the time, any function that has a side effect can be rewritten to return a value instead, and then the value can be used to produce the side effect.


> Recall our discussion about pure and impure functions. Notice that the more our code consists of pure functions, the easier it is to test.

For example:

```python

class Dog:
   # other code here
    def bark(self):
        print(f"{self.name} barks")
        # this function returns None and produces a side effect

def main()
    dog = Dog("Rex")
    dog.bark()

# if/name/main ... etc
```

Can be refactored as:

```python
class Dog:
   # other code here
    def bark(self):
        return f"{self.name} barks"
        # this function returns None and produces a side effect

def main()
    dog = Dog("Rex")
    print(dog.bark())

#if/name/main... etc
```

Notice that both these code snippets produce exactly the same result. But the first one is harder to test. Moreover, the second one is more flexible. We can now use the return value of the `bark` method in other parts of the program, not just when we need to print `woof, woof`. Most of the time, code that is easy to test is also more flexible and easier to maintain in general. So, in general, when you find code that is hard to test, you should first try and change the code to be easier to test, rather than trying to write tests for the hard-to-test code.

**Activity**: If your code from last week is full of void functions, refactor it to return values instead of producing side effects. Then write tests for the new functions. Notice that refactoring means changing the code without changing the functionality.

### If you have to: testing `print` and `input`

Though print and input are introduced early in the course, they are actually difficult to test. The `print` function is a void function, the input function is a fruitful function, but with one serious side effect: it pauses the program and waits for user input. This means that it will stop an automated test dead in its tracks.

Consider the following functions, for simplicity, we are going to test them in the same file, but in a real-world scenario, they would be in separate files.

```python
import unittest

def greet(name):
    print(f"Hello, {name}")

def get_name():
    return input("What is your name? ")

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice")

    def test_get_name(self):
        self.assertEqual(get_name(), "Alice")
```

The first test will fail because the 'greet' function returns `None`. The second test will pause the program and wait for user input so the tests will never finish.

Given this situation, we either refactor the code (best option) or we can patch the `print` and `input` functions. We can do this by using the `unittest.mock` module. This module allows us to replace functions with mock functions that we can control. We can use this to replace the `print` and `input` functions with functions that don't produce side effects.

The danger with mocking is that we can end up testing the mock, not the actual code. So we should use mocking sparingly and only when we have no other choice.

```python
# refactor
def greet(name):
    return f"Hello, {name}" # rewrite to return - no need to test print!

def get_name(_get_func=input): # use the input function as a parameter
    return _get_func("What is your name? ") # use the input function

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice")

    def test_get_name(self):
        self.assertEqual(get_name(lambda x: "Alice"), "Alice") # use a lambda function to simulate input
```

We haven't studied lambda functions yet, but they are a way to create a function on the fly. In this case, we are creating a function that takes one argument and returns "Alice". This is a way to simulate the `input` function without actually calling it.

If we must test these functions without refactoring, we can use the `unittest.mock` module to patch the `print` and `input` functions.

Here's an example of how you might use `unittest.mock` to test the `greet` function:

```python
import unittest
from unittest.mock import patch

class TestGreet(unittest.TestCase):
    @patch('builtins.print')
    def test_greet(self, mock_print):
        greet("Alice")
        mock_print.assert_called_with("Hello, Alice")

    @patch('builtins.input', return_value="Alice")
    def test_get_name(self, mock_input):
        self.assertEqual(get_name(), "Alice")

```

This is a more advanced topic, so we won't cover it in any more detail here. But you can read more about it in the [Python documentation](https://docs.python.org/3/library/unittest.mock.html).
