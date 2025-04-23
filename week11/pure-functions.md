# Overview

This quick guide explains the principles of decomposition and uses the idea of pure functions to demonstrate that we can identify patterns for decomposition that are more likely to lead to maintainable and correct code.

## Decomposition

Decomposition is the process of breaking down a complex problem into smaller, more manageable problems. Functions are an important language construct for doing so. However, as we'll demonstrate, some forms of decomposition are likely to lead to implicit dependencies between different parts of a program, which can make the code more difficult to understand, modify, and test^.

(^more difficult even than writing one monolithic procedure!)

Using the example of pure functions, we'll demonstrate this contrast.

## The challenge of coding

As a beginner programmer, you have to keep reminding yourself that the biggest challenge in coding isn't writing code (though that might be your challenge, now), instead it is managing complexity. Specifically, a successful software system must be sustainable over time, and maintainable not just by the original author, but by changing teams of developers. These developers often work concurrently on the same codebase.

A codebase will rapidly become more complex than any single programmer can fully comprehend.

## Pure functions

A pure function is a function that has the following characteristics:

1. It only interacts with the outside world through its parameters and return value.
2. Given the same arguments, it will always return the same result.
3. The outside world is not affected by the function's execution and, inside, the function maintains no state.

Everything else a function could conceivably do is called a **side effect** and any function that has a side effect is not a pure function.

### Functional decree

An increasingly popular way to write code is to favour pure functions and to avoid side effects.

### Side effects

The hardest thing to understanding side effects, a technical term related to pure functions, is that it is misleading. Before reading on, let go of your preconceptions of what the term "side effect" means.

Since a side effect is anything whatsoever that a function does other than compute and return a value, it incorporates everything we might ever want a program to actually do to be useful. Which, if you are still holding on to the common meaning of side effects, sounds like a contradiction.

Remember, if a function calculates `2 + 2` and returns `4`, if you want to see that result you have to display it - a side effect!

So clearly side effects are required for any program that actually does anything useful (otherwise, "tree falling in the woods", not making a sound, not even staying on the ground long enough for anyone to ever find it).

So looking at the decree previously, we recognize that at some point we *need* side effects, the decree just tells us to isolate the side effects as much as possible.

### Purity test

Categorize the following built-in Python functions as pure or impure:

```python
print
len
input
dir
help
min
max
```

