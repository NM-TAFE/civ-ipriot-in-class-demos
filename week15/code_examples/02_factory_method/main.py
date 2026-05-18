from work import Work
from work_formatter import WorkFormatter

complete_work = Work()
complete_work.title = "Raven of Eternity"
complete_work.summary = "Look there's something happening in this story."
complete_work.authors = ["Ira", "Dale"]
complete_work.chapters = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."]

pdf = WorkFormatter.run('pdf', complete_work)
epub = WorkFormatter.run('epub', complete_work)
mobi = WorkFormatter.run('mobi', complete_work)
junk = WorkFormatter.run('junk!', complete_work)

for type in [pdf, epub, mobi]:
    print("=====================================")
    print(type.serialise())