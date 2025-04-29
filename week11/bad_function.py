unit = 'c'
temperature = 38.8

# def convert_temp():
#     global converted_temp
if unit.lower() == 'f':
    converted_temp = (temperature - 32) * 5 / 9
else:
    converted_temp = temperature * 9 / 5 + 32

# convert_temp()
print(converted_temp)