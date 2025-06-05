def add(a, b):
    if(not isinstance(a, (int, float, complex)) or not isinstance(b, (int, float, complex))):
        raise TypeError("Must be numerical type")

    return a + b