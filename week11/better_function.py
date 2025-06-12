PI = 3.141592654
def convert_temp(temp, unit):
    if unit.lower() not in ['c', 'f']:
        raise ValueError("Invalid Unit")
    if unit.lower() == 'f':
        converted_temp = (temp - 32) * 5 / 9
    else:
        converted_temp = temp * 9 / 5 + 32
    return converted_temp

def main():
    t = convert_temp(temp=42, unit='c')
    print("value of t in here", t)


if __name__ == "__main__":
    main()
