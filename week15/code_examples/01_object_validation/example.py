from work import Work, Author

work = Work()

work.title = "something moon"
work.summary = "a epic drama"

print(work)
print(work.is_valid())
print(work.errors)

work.add_chapter("lots of text")

author = Author()
author.name = "Sarah"
work.authors.append(author)

print(work.is_valid())
print(work.errors)