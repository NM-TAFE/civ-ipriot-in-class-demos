# countdown loop
n = 10
while n > 0:
    print(n)
    n = n - 1 # forget me at your own peril!
print("Blast off!")

# loops for validation
while True:
    number = input("Give me a number (0-10)? ")
    try:
        number = int(number)
        if number > 10:
            print("Too high!")
            continue

    except:
        print("That's not a number!")
        continue
    break

print("Done!")