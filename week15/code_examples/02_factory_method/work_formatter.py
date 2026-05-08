from abc import ABC, abstractmethod


class WorkFormatter(ABC):
    def __init__(self, work):
        self.work = work

    @abstractmethod
    def serialise(self):
        raise NotImplementedError

    @classmethod
    def run(cls, type, work):
        """
        It's not very nice that I've had to lodge my imports in here -- it's because I would have
        otherwise created a 'circular import'.

        In some languages, having a classmethod like this one makes sense.
        In Python, it can be considered a code smell.  It might require you to think about what
        `run` is actually doing -- it makes a lot more sense as a module function, rather than a
        class function.

        Nevertheless, we need to show you Factory Pattern somehow.
        """
        from epub_formatter import EPubFormatter
        from mobi_formatter import MobiFormatter
        from pdf_formatter import PdfFormatter

        types = {
            "epub": EPubFormatter,
            "mobi": MobiFormatter,
            "pdf": PdfFormatter
        }

        if type in types:
            formatter = types.get(type)
            instance = formatter(work)
            return instance
        else:
            print(f"Error: type {type} not yet supported")
