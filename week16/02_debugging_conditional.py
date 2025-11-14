# It's the same scenario
# But bigger

# Exercise: now find out why `deeper_function(1)` returns 4

# (Have a think about `if 1:` and `if 0:`, where 1 and 0 are "the conditions"
#   of these if statements.)

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
    for counter in range(12000):
        result = deeper_function(counter)
        print(result)


if __name__ == "__main__":
    main()

