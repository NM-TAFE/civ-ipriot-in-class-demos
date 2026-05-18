from work_formatter import WorkFormatter

from base64 import b64encode

class MobiFormatter(WorkFormatter):
    """
    Fake mobi serialiser.
    This doesn't represent reality at all, but mobi is binaryish, so I'm pretending.
    """
    def serialise(self):
        work = self.work

        format = b64encode(f"{work.title}, {work.authors}, {work.chapters}".encode("utf-8"))
        return format

