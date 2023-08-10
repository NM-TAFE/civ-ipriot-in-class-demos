doo_doo = 'doo ' * 6

def sing_baby_shark(entity, is_shark=True):
    if is_shark:
        entity = entity + " shark"
    print(entity + ",", doo_doo)
    print(entity + ",", doo_doo)
    print(entity + ",", doo_doo)
    print(entity)
    print()

sing_baby_shark("Baby")
sing_baby_shark("Mummy")
sing_baby_shark("Daddy")
sing_baby_shark("Grandma")
sing_baby_shark("Grandpa")
sing_baby_shark("Let's go hunt", is_shark=False)
sing_baby_shark("Run away", is_shark=False)
sing_baby_shark("Safe at last", is_shark=False)
sing_baby_shark("It's the end", is_shark=False)


