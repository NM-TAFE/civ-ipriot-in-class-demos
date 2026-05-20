import json
from abc import ABC, abstractmethod

class Loadable(ABC):
    @classmethod
    @abstractmethod
    def load(self, object_dictionary):
        # This should return an instance of whatever is inheriting Loadable
        raise NotImplementedError
