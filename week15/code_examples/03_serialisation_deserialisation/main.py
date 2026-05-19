from work import Work
from random import choices, randint

def random_letter_string(length):
    letters = list("qwertyuiopasdfghjklzxcvbnm ")
    return "".join(choices(letters, k=length))

def random_work_generator():
    work = Work()
    work.title = random_letter_string(16)
    work.summary = random_letter_string(64)
    work.authors = [random_letter_string(16)]

    chapter_temp = []
    for _ in range(randint(1,12)):
        chapter_temp.append(random_letter_string(512))

    work.chapters = chapter_temp

    return work


work_a = random_work_generator()
work_b = random_work_generator()
work_c = random_work_generator()
work_d = random_work_generator()

for work in [work_a, work_b, work_c, work_d]:
    print(str(work))
    work.save()

