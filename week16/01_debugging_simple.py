# Question: why does `deeper_function(0)` return 2?

def deeper_function(an_argument):
    if an_argument % 6 == 0:
        return an_argument ^ 2
    elif an_argument % 3:
        return an_argument + 3
    elif an_argument % 5 == 0 and not an_argument % 10 == 0:
        return deeper_function(an_argument + 1000)
    elif an_argument > 10 and an_argument % 2 == '0':
        return an_argument / 2
    return an_argument

def main():
    result = 0
    for counter in range(24):
        result = deeper_function(counter)
        print(result)


if __name__ == "__main__":
    main()
