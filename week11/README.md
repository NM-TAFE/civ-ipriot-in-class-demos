# Unit Testing in Python

> **ICTPRG430: Apply Introductory Object-Oriented Language Skills**

---

## Lesson Objectives

1. Understand the significance of testing in the software development lifecycle.
2. Recognise the importance of developing tests to meet user requirements and application specifications.
3. Learn about the concept of Test-Driven Development (TDD) and its role in object-oriented programming.
4. Familiarise yourself with the Python `unittest` module.
5. Master the basic operations of the `unittest` module to write, conduct, and document tests.
6. Comprehend how to document tests effectively using modern industry best practices.

**Learning Summary:**

- Importance of testing in software development.
- Aligning tests with user requirements.
- Introduction to TDD.
- Python's `unittest` module's role and functions.
- Effective test documentation.

---

## Revision: [Fundamentals of OOP](revision.md)

Before diving into the topic, review the principles of Object-Oriented Programming (OOP). This revision ensures you have a strong foundation to understand the context and importance of the testing concepts that follow.

**Learning Summary:**

- Core concepts of OOP.
- Role of objects, classes, and methods in OOP.

---

## Introduction to the High-Level Concept of Unit Testing

Unit testing involves testing individual "units" or components of software to ensure they function as intended. By ensuring that individual units work correctly, you ensure the integrated software application functions as intended.

**Learning Summary:**

- Definition and purpose of unit testing.
- Role of unit testing in OOP.

---

## Introduction to the Concept of Test-Driven Development (TDD)

TDD is a development approach where you write tests before you write the code. The primary benefits include better code structure, higher code coverage, and enhanced software robustness.

**Learning Summary:**

- What is TDD?
- Benefits of TDD in the software development process.

---

## Introduction to the Python `unittest` Module

Python’s built-in module, `unittest`, allows you to write, execute, and set up your unit tests. Its primary components include TestCase, Test Fixture, Test Suite, and Test Runner.

**Learning Summary:**

- Overview of the `unittest` module.
- Key components and their functions.

---

## Examples of Unit Tests and Traditional Written Test Cases

**Documented Test Case (using `unittest`):**

```python
import unittest
from my_module import Calculator

class TestCalculatorMethods(unittest.TestCase):
    def test_add_positive_numbers(self):
        calc = Calculator()
        self.assertEqual(calc.add(3, 4), 7)

    def test_multiply_negative_and_positive_number(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(-3, 4), -12)
```

**Traditional Written Test Case:**

```text
Test Case Name: Test Addition of Two Positive Numbers
Objective: Verify that the calculator can add two positive numbers correctly.
Steps:
1. Launch the calculator application.
2. Enter the first number: 3.
3. Enter the second number: 4.
4. Press the 'Add' button.
Expected Result: The calculator should display the result as 7.
```

**Learning Summary:**

- Coding a unit test using the `unittest` module.
- Contrasting with a traditional written test case.

---

## "Cheatsheet" for Unit Testing with `unittest`

**unittest Module:**

- `TestCase`: A collection of test functions.
- `Test Fixture`: Setup and teardown operations for tests.
- `Test Suite`: A combination of multiple test cases.
- `Test Runner`: Manages test execution and provides results.

**Test Module Naming:**

- Prefix the test module name with `test_`, e.g., `test_calculator.py`.

**Test Method Naming:**

- Start the test method name with `test_`.
- Ensure the name describes both the condition and expected outcome, e.g., `test_add_positive_numbers`.

**Best Practices:**

- Write self-explanatory and descriptive method names.
- Avoid redundancy in test documentation.
- Utilise setUp() and tearDown() methods for initializing and cleaning up resources.

**Learning Summary:**

- Basic components of the `unittest` module.
- Naming conventions for test modules and methods.
- Essential best practices for unit testing.

---
