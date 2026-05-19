import json
from abc import ABC, abstractmethod

class Loadable(ABC):
    @abstractmethod
    @classmethod
    def load(self, object_dictionary):
        # This should return an instance of whatever is inheriting Loadable
        raise NotImplementedError
