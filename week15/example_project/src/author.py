"""
Represents an Author of a blog post.

This file includes 2 new concepts
1. UUIDs <- Don't bother learning this yet -- it's a unique string generator, let's say.
2. Properties -- if you found yourself writing methods to help you encapsulate your attributes safely,
    this is a 'more pythonic' way of doing it.
    You could have almost as easily defined a `get_name` and `set_name` method, instead.
"""
from uuid import uuid4

class Author:
    def __init__(self, name, id=None):
        self._name = name
        self._id = id or uuid4() # What is this? I wanted a unique ID in the laziest possible way.

    # What are these!?
    # This is the 'pythonic' way to make `getters` and `setters`.
    @property
    def name(self):
        return self._name

    # Here, @name comes from the name of the function definition on line 20.
    # Wait, the name of this function is exactly the same as L20? Won't this break?
    # I believe that the annotation is doing some heavy lifting for us here.
    @name.setter
    def name(self, name):
        if self.is_valid(name):
            self._name = name

    def is_valid(self, name):
        return isinstance(name, str) and len(name) > 0