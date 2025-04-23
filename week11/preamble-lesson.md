# Overview

This session provides a preamble to our deep dive into object-oriented programming concepts. In this session we will:

1. Review key concepts and semantics from last term's ICTPRG302 class
2. Expand our idea of the kind of problems programmers solve:

- modularity
- reusability
- maintainability

3. Look at some of the more basic mechanisms in Python for achieving the above:

- Modules and imports (NEW!)
- Functions

4. Show how just writing functions and modules doesn't necessarily achieve our objectives.

## ICTPRG302 Review

The key concepts you will need from last term are:

- Defining functions
- Variables and scopes
- Python primitives as objects

### Defining functions

#### Fill in the blanks

  > Define a function with the `___` keyword
  > After this keyword, we specify the `____` of the function we are declaring
  > We then open `_____` brackets and inside them we place the `________` names.
  > The body of the function is `________` and we end the definition by `____________`
  > The `______` keyword tells the function to immediately return to the caller with the result of evaluating the expression following that keyword.

> Call a function by using its `____` followed by `___________` containing any required `_________`.
> When a function completes, the function call is replaced by whatever the function `_______`.

*Whatever happens in Vegas, stays in Vegas*
> Whatever variables/names get `___________` in a function stay in the function

Note: **Answers to fill in the blanks at the bottom of this document**

#### Short Answers
>
> Note: if you don't know the answer to any of these questions, they are designed such that you can check your answer by writing simple snippets of code!

1. What will happen if you call a function before declaring it?

> Answer here

2. What will happen if you specify a function name without calling it (but after defining it)? Hint: print() the function.

> Answer here

3. The following are different definitions of a "hello" function:

```python
def hello1():
    print("Hello, world!")

def hello2()
    return "Hello, World!"

```

Which of these programs will print "Hello, World!" and **only** "Hello, World!"

```text
#1
print(hello1())
#2
print(hello2())
#3
hello1()
#4
hello2()
#5
print(hello1)
#6
print(hello2)
```

4. The following are different definitions of an "add_two" function:

```python
def add_two_a(x):
    return x + 2

def add_two_b(x):
    print(x + 2)

```

Which of the following snippets will **print** 4? Which will result in an error?

```
#1
print(add_two_a(2))
#2
print(add_two_b(2))
#3
add_two_a(2)
#4
add_two_b(2)
#5
print(add_two_b)
#6
x = 2
add_two_b()
#7
print(add_two_a(1) + 1)
#8
print(add_two_a(1) + add_two_a(-1))
#9
x = -1
print(add_two_a(1) + add_two_b(x))

```

## Problems programmers solve

In ICTPRG302, we looked at how to write programs to solve problems. While sometimes the solutions were not easy: the problems were.

- How do you calculate the area of a rectangle?

- How do you determine the payable tax on a salary?

- How do you print out the lyrics of Baby Shark as efficiently as possible?

Every time we learned about some new capability or syntax, we were able to solve more complex problems or solve these problems in a more straightforward way. In this sense *why* we were learning certain aspects of programming was generally clear cut.

However, as programming scales up, we realize that programming itself presents its own problems (i.e. "Second-order problems").

For example:

- How do you structure the code in such a way that multiple people can work on it at the same time?
- As the project gets more complex, how do you onboard new developers when the codebase is no longer comprehensible by a single person?
- How do you stay productive as the code base grows and there are more dependencies and more moving parts?
- How do you maintain quality and identify/avoid bugs?

Notice that, unlike the first set of questions, these questions are not about **solving** a specific problem, but about **organizing** solutions to problems.

Generally, how teams of developers answer these questions plays the most central role in the success of a project, over and above how specific technical problems are solved.

A challenge for you, as a novice programmer, is that, chances are, you haven't encountered very many second-order problems. This is because you are currently only writing small, short-lived programs individually and so usually the fastest and simplest path to a solution is the best.

The concepts we have covered so far have generally helped you find the "shortest path" to a solution. But many of the programming concepts we will cover this term will not make coding a solution to any specific problem easier (often it will make it harder).

This in itself can be a source of confusion and an obstacle to learning.

Recognize that often it is the **problem** we are solving that is harder to grasp than the **solution** for no other reason than you haven't experienced these problems.

But as the projects you will be working on become larger and more complex, and you will be working with other people, the concepts we will cover this term will be essential to your success.

### Reflection

Jot down some strategies you can think of to addressing some of the second-order problems above.
> a. Answer here
> b. Answer here
> c. Answer here

## Modularity, reusability, maintainability

### Modularity

Modularity is the idea that we can break down (decompose) a large problem into a set of small problems. Each of these small problems can be solved independently and then combined to solve the larger problem.

This is a powerful idea, even for working individually, because this is how most complex problems are tackled, not just in programming, but in life. If you think about how you last successfully tackled a complex or overwhelming task it was probably by first breaking it down into smaller tasks.

In programming, modularity not only allows us to treat a big problem as a bunch of more manageable problems but also to employ other programmers to work on these smaller problems concurrently.

#### Reusability

Reusability takes modularity a step further by recognizing that while complex problems are often unique, the smaller problems that make them up are often not. This means that we can take a solution to a small problem and use it in multiple places. This allows us to write less code, and to write code that is more reliable (because it has been tested in multiple places).


#### Maintainability

Writing modular code that is reusable is a good start, but it doesn't guarantee that the code will be maintainable. In fact, writing modular code using reusable components can sometimes make the code less maintainable. Maintainability is about writing code that is easy to understand, easy to change, and easy to test. It is about following patterns that help us avoid some of the pitfalls of modularity and reusability. 


### Technical stuff

You may have already guessed that this is all leading us to object-oriented programming (OOP) but before we get to OOP, let's look at some of the tools we already have to address modularity and reusability and then highlight a common pitfall for achieving maintainability.

#### Modularity and imports

Python comes with a fairly limited set of built in functions, but beyond the built in functions is the standard library which provides a set of **modules** each with their respective set of functions to do anything from network programming to data analysis to web scraping. Other python developers can also create modules and share them with the community via the [Python Package Index (PyPI)](https://pypi.org).

In this topic, we are going to learn about the different ways to use modules in our code and finally how we can use our own code as modules.

#### Importing modules

Python has a built in keyword `import` that allows us to import modules. A module may be installed on the system, the current python virtual environment, or it can be any python file in the current directory.

```python
import math
print(math.pi)
```

When we import a module python creates a `name` for us - think of it as a variable name, because it is. But usually this variable name isn't something we want to reference directly rather we want to reference functions within that module using the dot operator - almost as though it is a folder name as opposed to a file name. We call the use of names to partition other names (like directories distinguish between files of the same name) **namespacing**. Thus we say that `import math` creates a namespace called `math` and we can access the functions within that namespace using the dot operator.

We can also alias the module name using the `as` keyword the keyword will import the module into a namespace of our choosing:

```python
import math as m
print(m.pi)
```

Generally, unless you have seen other people use `as` to alias a module (particularly a built in one) - don't do it. It will just confuse you and others.

Finally, we can import definitions from a module into the global/current namespace like so:

```python
from math import pi
print(pi)
```

This is more commonly done than aliasing but you should still err on the side of using "vanilla" imports. 

All of the above can be used with a python file in the current directory - so long as that file uses legal python variable names (which you've been doing right!)

---
List three commonly used characters in file names that are not legal python variable names:
> a. Answer here
> b. Answer here
> c. Answer here
---

#### What happens when you import a file?

When you import a file, Python **executes everything in the file** just as if you had run it as a script: it has to do this in order to create the definitions in the file. But often that can lead to undesirable side effects. For example, consider what would happen in the following situation (imagine each comment represents a separate file):

```python
# file: hello.py

def greet(name):
    print(f"Hello, {name}!")

name = input("Enter your name: ")
greet(name)

# file: main.py

import hello
hello.greet("World")
```

`hello.py` is a fine program! With a wonderful and potentially reusable function. But when we import it in `main.py`, it will execute the input statement and wait for user input before we can call the `greet` function. This may have been what we wanted when we ran `hello.py` as a script, but it is not what we want when we use it as a module.

One solution would be to decide in advance whether we want to run a file as a script or a module and then carefully structure our code to avoid this problem. But that is not very flexible and it is not the pythonic way.

Instead, Python uses a special variable `__name__` to determine whether a file is being run as a script or imported as a module. When a file is run as a script, the variable `__name__` is set to the string `"__main__"`. When it is imported as a module, `__name__` is set to the name of the module (i.e. the name of the file without the `.py` extension).

This creates the paradigmatic structure of a python file using `if __name__ == "__main__":`:

```python
# file: hello.py
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    name = input("Enter your name: ")
    greet(name)

# file: main.py
import hello
hello.greet("World")
```

The modified `hello.py` file will now only execute the input statement when it is run as a script. When it is imported as a module, the input statement will not be executed and we can call the `greet` function without any side effects. Notice that the behavior of `hello.py` has not changed when it is run as a script. It will still prompt for user input and greet the user. But now it is not only a useful script, it is a useful module as well.



## Answers to Fill in the blanks

>> Define a function with the `def` keyword
> After this keyword, we specify the `name` of the function we are declaring
> We then open `()` brackets and inside them we place the `parameters` names.
> The body of the function is `indented` and we end the definition by `dedenting/de-indenting`
> The `return` keyword tells the function to immediately return to the caller with the result of evaluating the expression following that keyword.

> Call a function by using its `name` followed by `()` containing any required `arguments`. - Notice **arguments**, not `parameters`
> When a function completes, the function call is replaced by whatever the function `returns`.

> Whatever variables/names get `instantiated/declared` in a function stay in the function: we call variables defined in a function `local variables`. And they can only be accessed within the function and cease to exist when the function completes.
