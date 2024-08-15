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

def get_grade(student_number, result_list):
    for result in result_list:
        if result[0] == student_number:
            return result[1]
    return None

def get_grade2(student_number, result_list):
    result_position = (result_list.index(student_number)
                       + 1)
    return result_list[result_position] # uncaught

print(get_grade('2001234', results))

print(get_grade2('2001234', results1))