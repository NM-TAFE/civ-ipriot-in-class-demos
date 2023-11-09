def wobble(thingies = None):
    thingies = thingies or [] # using or as a shorthand for select the first non-falsey thingy
    thingies.append(42)
    print(thingies)

wobble([1,2,3])
wobble()
wobble()

