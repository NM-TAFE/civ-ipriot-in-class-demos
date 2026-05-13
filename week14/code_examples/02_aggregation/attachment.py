from abc import ABC, abstractmethod

class Attachment(ABC):
    @property # Order matters here.  Property has to be before abstractmethod.
    @abstractmethod
    def type(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def filepath(self):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        """
        This is actually built in -- by declaring it abstract, I
        force the implementor to have to write a __str__ method.
        __str__ is how Python knows how to render an object when
        you call `str` on it.
        """
        raise NotImplementedError