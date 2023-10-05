# Revision: Object-Oriented Programming (OOP) in Python

## Overview

Quick revision of the fundamentals of OOP in Python.  You will learn about OOP concepts such as classes, objects, inheritance, and encapsulation.

## Objectives

By the end of this lesson, students will be able to:

1. Understand the basic concepts of OOP, including classes, objects, inheritance, and encapsulation.
2. Write simple Python programs using OOP concepts.

## Prerequisites

- Basic understanding of Python programming
- Familiarity with programming concepts such as functions, loops, and conditionals

## Outline

1. Introduction to OOP
2. Classes and objects
3. Inheritance
4. Encapsulation

## Details

### Introduction to OOP

OOP attempts to address issues of maintainability, code reuse, and concurrent development. It does so by defining objects that encapsulate data and behavior. Objects are instances of classes, which are blueprints for objects. Classes define the attributes and methods that objects will have.

The best way to think about OOP is that, unlike a procedural mindset, which focuses on the actions and steps you want to perform (and usually comes naturally to most people), OOP focuses on the things/objects/nouns first, what they are, how they **should** behave, how they **could** interact. Only when you have all the blueprints in place, do you then create instances of data and their associated behavior.

 This is a very different way of thinking about programming, and it can be difficult to wrap your head around at first, and it doesn't come naturally to most people. 

 Moreover, because OOP addresses issues of software development at scale, it can be difficult to see the benefits of OOP when you're writing small programs. However, as your programs grow in size and complexity, you will find that OOP is an important tool for managing complexity.

### Classes and objects

- Recall a class defines a blueprint for objects.
- Explain how objects are instances of classes.
- Can you create a class in Python? Can you instantiate an object from that class?

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

## Inheritance

- Explain the concept of inheritance and how it promotes code reusability.
- Can you create a subclass that inherits from a parent class?
- What are some of the pitfalls of inheritance?

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

fido = Dog('Fido', 'Labrador')
fido.bark()
fido.eat('steak')
```

### Encapsulation

- Explain the concept of encapsulation and how it promotes modularity and data protection.
- Can you create "Private" attributes and methods in Python? How is Python different from other languages in this regard?
- Data as state
- The state of an object should be protected
