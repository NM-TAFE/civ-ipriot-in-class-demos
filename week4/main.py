smallest = None
for number in [3, 0, 12, -9, 74, 15]:
    if smallest is  None or number < smallest:
        smallest = number
print("smallest", smallest)