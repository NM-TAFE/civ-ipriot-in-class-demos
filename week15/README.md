# Lesson Plan: Unit Testing Fundamentals

## Overview

In this lesson, we will introduce you to the fundamentals of unit testing.

## Duration

1 hour

## Objectives

By the end of this lesson, students will be able to:

1. Understand the basic concepts of unit testing.
2. Write simple `assert` statements
3. Use the unit test framework `unittest` to write a basic test case

## Prerequisites

- Basic understanding of OOP Python programming


## Materials

- Python 3.x installed on students' computers
- A text editor or Integrated Development Environment (IDE) for writing Python code

## Lesson Outline

1. Introduction to unit testing
2. Assertions
3. Python's unittest framework
4. Writing a simple unit test

## Lesson Details

### 1. Introduction to unit testing (15 minutes)

- Briefly explain the history and purpose of unit tests.
- Discuss the importance of unit testing:
  - Agility
  - Quality
  - Design
- Define the problem: "how do we test code that is part of a larger system?"

### 2. Assert! (15 minutes)
- Let's create our own unit tests
- Introduction to assert statements: the foundation of unit testing
- Limitations
- Why we need a framework

Recall the following code:
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

## Unit test frameworks (20 minutes)

- Using unit tests instead

```python
class TBD: ...
```

### 4. Exercise (20 minutes)

- Write your own unit test to test the Dog class
