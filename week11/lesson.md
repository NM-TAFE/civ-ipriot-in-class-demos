# Overview

Provides sample code for OOP fundamentals in Python. The code is designed to help you understand the mechanics of OOP over and above the **concepts**, which we will focus on next week.

## The simplest class you can create

Let's create a class that does nothing (a Cat?). It's the simplest class you can create in Python.

```python
class Cat:
    pass
```

That's it - that's a class.

Let's check the type of the class:

```python
print(type(Cat))
```

Instantiating a class:

```python
cat = Cat()
print(type(cat))
```

Notice that we **call** a class to get an _instance_ of that class.

Notice some naming conventions: classes are typically named in `PascalCase`, while instances (like all variables!) are named in `snake_case`.

## Adding attributes to an instance

Attributes are variables that are attached to an instance of a class. In Python, we can attach attributes dynamically to an instance. For example:

```python
cat.name = 'Lenny'
cat.age = 3
```

We can access these attributes using the `.` operator:

```python
print(cat.name)
print(cat.age)
```

While this is syntactically valid, it's not much of a **blueprint**. We can't guarantee that all cats shall have a name and an age, nor can we guarantee the properties of these attributes.

```python
  cat2 = Cat()
  cat2.bark = "Woof, Woof" # Oh no! A barking cat
  print(cat2.name) # Oops forgot to set the name!
  # Disaster!
```

## Adding attributes to a class

What we want is to define a `Cat` blueprint that says "when a cat is created (instantiated is the technical term), it must have a name and an age". We can do this by defining a special method called `__init__`:

```python
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

The `__init__` method is a special method that is called when an instance of a class is created. It is called an **initializer**, but if you've had some experience with other OO languages, you can think of it as the **constructor**, at least for now.

What is a method? Just like a variable on an instance is called an attribute, a function defined in a class is called a method. Why? "Just to be confusing" is the technical answer.

The `self` parameter is more interesting: it is a reference to the instance of the class. We can then attach attributes to the instance using `self`.

Say what?

## Meet `self`

All object-oriented programming (OOP) languages create definitions at the class level: "what attributes can an object of this type have?" "what behaviors (methods) can an object of this type perform?". However, when you create an instance of an object, ths instance only needs to contain the values for its attributes. Notice we don't need to copy the methods into the instance. since the methods are the same: they just might act differently depending on the values of the attributes for a given instance.

That is, while conceptually and semantically it might make more sense to think of a method like "meow" as being something my cat (or a **particular** cat) does, in reality its more accurate to say that the type `Cat` performs behaviors on instances of cats.  That is, `my_cat.meow()` really means "call the `meow` method on the `Cat` class and get the class to make the specific cat, `my_cat`, meow.

This is rather unintuitive. Different languages deal with this unintuitive fact in different ways.

- Some languages, like Python, Ruby, and PHP, explicitly pass and reference the instance within methods. That is, no smoke and mirrors: what you see is what you get. But the price you pay is you have to always be explicitly referencing the instance even when that's clearly what you mean.
- Others, such as C# or Java, implicitly refer to the instance, making an explicit reference unnecessary. This is often more intuitive (at first) but gets more confusing and less flexible as your programs get more complex.

In Python, when you define methods in a class, the first parameter always explicitly refers to the object instance. By a very strong convention (think: rule), this parameter is named `self`. Unlike languages that implicitly use the object instance, Python explicitly requires this reference.

For example:

```python
class Cat:
    def meow(self):
        print("Meow!")

my_cat = Cat()
my_cat.meow()  # Python internally calls Cat.meow(my_cat)

# in fact you can do exactly that, and the two are equivalent:
Cat.meow(my_cat)

```

Notice that when you want to associate attributes with an instance, you use `self` to refer to that instance. When you want to call a method **for** an instance, you must also use `self` since that tells Python to pass this particular instance to the method.

## Using the `__init__` method

The parameters defined in the `__init__` method determine the arguments that must be passed when creating an instance of the class. For example:

```python
cat = Cat('Whiskers', 3)
print(cat.name)
print(cat.age)

cat2 = Cat('Kenny') # Error! We must pass the age
```

## Defining methods

Okay, we keep talking about meowing let's finally make a cat that can perform their own **individual** meow:

```python
  class Cat:
      def __init__(self, name, age):
          self.name = name
          self.age = age

      def meow(self):
          print(f'{self.name} says "Meow"')
```

Now we can call the `meow` method on an instance of the `Cat` class:

```python

cat = Cat('Lenny', 3)
cat.meow()
```

## Exercises

1. Add a coat color attribute to the `Cat` class. Instantiate a `Cat` instance and print the `name`, `age`, and `coat_color` attributes.

2. Add a purr method to the `Cat` class that prints &lt;name&gt; purrs. Call the purr method on the `Cat` instance.

3. Define a class `Dog` that has a `name` and an `age` attribute. Instantiate a `Dog` instance and print the `name` and `age` attributes.

4. Add a `bark` method to the `Dog` class that prints &lt;name&gt; barks. Call the `bark` method on the `Dog` instance.

### Challenge exercise

1. Define a method in both the Cat and Dog class called "meet" when a cat gets passed a cat or a dog it will "hisses at &lt;other's name&gt;".

2. When a dog gets passed a cat it will bark but when passed a dog it will wag its tail.

**Clue**: You can use the `isinstance` built-in function to check the type of an object (this is better than using `type`, for reasons we'll explain next week).

```python
if isinstance(other, Cat):
    print(f'{self.name} hisses at {other.name}')
```
