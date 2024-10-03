# Problem
# I want to look up results based on student numbers

# Solution using a list
results =    [['2001234', 'CO'],
                       ['2001235', 'CO'],
                       ['2001236', 'CO'],
                       ['2004321', 'NYC']]

results1 = ['2001234',
           'CO',
           '2001235',
           'CO',
           '2001236',
           'CO',
           '2004321',
           'NYC']

def to_dictionary99(list_):
    # given list [k, v, k, v, k, v]
    d = dict()
    for i in range(len(list_)):
        if i % 2:
            continue
        d[list_[i]] = list_[i+1]
    return d

def to_dictionary0(list_):
    # given list [k, v, k, v, k, v]
    d = dict()
    for i in range(len(list_)):
        if i % 2 == 0:
            d[list_[i]] = list_[i+1]
    return d
def to_dictionary1(flat_list):
    # given list [k, v, k, v, k, v]
    d = dict()
    for i in range(0, len(flat_list), 2):
        d[flat_list[i]] = flat_list[i + 1]
    return d

def to_dictionary(nested_list):
    # given list [[k, v], [k, v] ...]
    d = dict()
    for item in nested_list:
        d[item[0]] = item[1]
    return d

def to_flat_list(d):
    # [k, v, k, v]
    flat_list = []
    for k, v in d.items():
        flat_list.extend([k, v])
    return flat_list

def to_nested_list(dict_):
    # [[k, v], [k,v]...]
    nested_list = []
    for k, v in dict_.items():
        nested_list.append([k, v])
    return nested_list

def to_dictionary42(list_):
    # given list [k, v, k, v, k, v]
    return {k: v for k, v in zip(list_[0::2], list_[1::2])}
    # given list [[k, v], [k, v] ...]
    return {k: v for k, v in list_}
def get_grade(student_number, result_list):
    result = "??"
    return result

print(to_dictionary(results))
print(to_dictionary1(results1))
print(to_dictionary0(results1))
print(to_dictionary99(results1))

coordinates = [24, 14]
coordinates = (24, 14)
x = 24
y = 14
x, y = (24, 14)
first, last, coordinates, grades = 'raf', 'avigad', (2, 3), 'CO'
first, last = 'raf', 'avigad'

color = (255, 0, 0)
r, g, b = color