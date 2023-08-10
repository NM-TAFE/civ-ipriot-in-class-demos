doo_doo = 'doo ' * 6

def sing_baby_shark(entity, n = 3, is_shark=True):
    if is_shark:
        entity = entity + " shark"
    while n > 0:
        print(entity + ",", doo_doo)
        n = n - 1
    print(entity)
    print()

def sing_baby_shark(entity, n = 3, is_shark=True):
    if is_shark:
        entity = entity + " shark"
    for _ in range(n):
        print(entity + ",", doo_doo)
    print(entity)
    print()

sharks = ["Baby",
          "Mummy",
          "Daddy",
          "Grandma",
          "Grandpa"]

non_sharks =["Let's go hunt",
             "Run away",
             "Safe at last",
             "It's the end"]

for entity in sharks:
    sing_baby_shark(entity, n = 5)

for entity in non_sharks:
    sing_baby_shark(entity, n = 10, is_shark=False)



