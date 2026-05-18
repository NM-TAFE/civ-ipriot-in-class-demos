from work_formatter import WorkFormatter

class EPubFormatter(WorkFormatter):
    """
    Fake epub serialiser.
    (Yes, epub is xml.)
    (No, this won't work on its own.)
    """
    def serialise(self):
        work = self.work

        format = f"""
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
  <head>
    <meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
    <title>{work.title}</title>
    <link rel="stylesheet" href="css/main.css" type="text/css" />
  </head>
  <body>
    <h1>{work.title}</h1>
    <h2>{"; ".join(work.authors)}</h2>
    <p>
    {"</p><p>".join(work.chapters)}
    </p>
  </body>
</html>
"""
        return format

