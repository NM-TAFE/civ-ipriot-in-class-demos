from work_formatter import WorkFormatter
from base64 import b64encode

class PdfFormatter(WorkFormatter):
    """
    Fake pdf serialiser.
    This doesn't represent reality at all.
    I didn't even create a canvas. Please blur your eyes a little.
    """
    def serialise(self):
        work = self.work

        format = b64encode(f"{work.title}, {work.authors}, {work.chapters}".encode("utf-8"))
        return format

