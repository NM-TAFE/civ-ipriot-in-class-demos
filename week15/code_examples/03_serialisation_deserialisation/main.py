from work import Work
from random import choices, randint

def random_letter_string(length):
    monkey_letters = list("qwertyuiopasdfghjklzxcvbnm ")
    return "".join(choices(monkey_letters, k=length))

def a_different_kind_of_factory():
    """
    Terrible method name so that you can notice that this is another kind of object
    factory.
    """
    work = Work()
    work.title = random_letter_string(16)
    work.summary = random_letter_string(64)
    work.authors = [random_letter_string(16)]

    chapter_temp = []
    for _ in range(randint(1,12)):
        chapter_temp.append(random_letter_string(512))

    work.chapters = chapter_temp

    return work


work_a = a_different_kind_of_factory()
work_b = a_different_kind_of_factory()
work_c = a_different_kind_of_factory()
work_d = a_different_kind_of_factory()

for work in [work_a, work_b, work_c, work_d]:
    print(str(work))
    work.save()