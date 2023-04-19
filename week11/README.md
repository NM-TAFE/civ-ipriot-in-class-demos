# Lesson Plan: Introduction to Object-Oriented Programming (OOP) in Python

## Overview

In this lesson, we will introduce you to the fundamentals of Object-Oriented Programming (OOP) using Python. You will learn about OOP concepts such as classes, objects, inheritance, and encapsulation.

## Duration

2 hours

## Objectives

By the end of this lesson, students will be able to:

1. Understand the basic concepts of OOP, including classes, objects, inheritance, and encapsulation.
2. Write simple Python programs using OOP concepts.

## Prerequisites

- Basic understanding of Python programming
- Familiarity with programming concepts such as functions, loops, and conditionals

## Materials

- Python 3.x installed on students' computers
- A text editor or Integrated Development Environment (IDE) for writing Python code

## Lesson Outline

1. Introduction to OOP
2. Classes and objects
3. Inheritance
4. Encapsulation
5. Hands-on practice: Designing and implementing a simple object-oriented system
6. Recap and closing

## Lesson Details

### 1. Introduction to OOP (15 minutes)

- Briefly explain the history and purpose of OOP.
- Discuss the advantages of OOP, such as code reusability, modularity, and ease of maintenance.

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
- Introduce some of the pitfalls of inheritance

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

### 4. Encapsulation (20 minutes)

- Explain the concept of encapsulation and how it promotes modularity and data protection.
- Private attributes and methods and pythons conventions and limitations in this regard
- Data as state
- The state of an object should be protected
