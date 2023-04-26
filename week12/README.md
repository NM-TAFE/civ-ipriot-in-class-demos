# Lesson Plan: Introduction to Object-Oriented Programming (OOP) in Python
##### Part2
## Overview

In this lesson, we will introduce you to the fundamentals of Object-Oriented 
Programming (OOP) using Python. 
You will learn about abstraction and polymorphism.

We will then introduce the Raspebrry PI
## Duration

2 hours

## Objectives

By the end of this lesson, students will be able to:

1. Define abstraction, polymorphism
2. Differentiate between each of the four pillars
3. Use abstract classes and methods


## Prerequisites

- Basic understanding of Python programming
- Familiarity with programming concepts such as functions, loops, and conditionals
- Familiarity with basic OOP

## Materials

- Python 3.x installed on students' computers
- A text editor or Integrated Development Environment (IDE) for writing Python code

## Lesson Outline

1. Revision: creating objects
2. Commonality between objects
3. Inheritance facilitated polymorphism
4. Abstraction facilitated polymorphism
5. Hands-on practice
6. Recap and closing

## Lesson Details

### 1. Revision  (15 minutes)

- Create two classes: Circle and Square. Each class has the appropriate 
  attributes for that shape and a method to return the area.


### 2. Classes and objects (30 minutes)

- Introduce the concept of a class and how it defines a blueprint for objects.
- Explain how objects are instances of classes.
- Teach students how to create a class in Python.
- Show how to create objects and access their attributes and methods.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

fido = Dog("Fido", "Labrador")
fido.bark()
```

## Inheritance (20 minutes)

- Explain the concept of inheritance and how it promotes code reusability.
- Teach students how to create a subclass that inherits from a parent class.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self, food):
        print(f"Yum Yum delicious {food}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

fido = Dog(fido, Labrador)
fido.bark()
fido.eat('steak')
```

### 4. Encapsulation (20 minutes)

- Explain the concept of encapsulation and how it promotes modularity and data protection.
- Private attributes and methods
- Data as state
- The state of an object should be protected
