"""A program that helps you use a debugger!

Your mission is to set up breakpoints, inspect variables, and control where the program pauses.

You can only pause on treasure - you must never pause on a mine!


The game gets progressively harder as you advance, you need to think about what these functions do:
- step over
- step into
- step out

You need to set your breakpoints wisely, so you can inspect the variables and understand the program flow.


As well as predict where the interpreter will want to go to next. That is, the program flow!

"""
##################################################
# YOU ARE NOT ALLOWED TO SET BREAKPOINTS ANYWHERE
# IN THIS SECTION
###################################################
import random

MAX_GUESS = 100
SECRET_NUMBER = random.randint(1, MAX_GUESS)

def here_be_mines():
    """If your debugger pauses here, it's mines you should fear!"""
    print("BOOM! 💣💣💣", "Start again.")


def easy_loot():
    """If your debugger pauses here, treasure is near!"""
    print("Yay! 💰💰💰", "Keep going!")





def a_mystery_wrapped_in_an_enigma():
    """Some loot, but you better know when to scoot"""
    print("You might want to override this variable if you want to still be able")
    is_treasure = False
    if is_treasure:
        easy_loot()
    else:
        here_be_mines()

    bonus = "💰💰💰" if is_treasure else "💣💣💣"
    print("Yay or nay, your bonus is on the way:", bonus)
    print("Get out now!")
    print("This is your last chance!")


    print("KABOOM! 💣💣💣", "You should have stepped out when  you had a chance")
    return bonus

#################################
# SET BREAKPOINTS BELOW THIS LINE
#################################

def treasure_roulette():
    """Like a real casino, it is probably going to be a NO! But if you set a conditional breakpoint, you might get lucky!"""

    while True:
        guess = random.randint(0, MAX_GUESS)
        if guess == SECRET_NUMBER:
            print("You Win! 💰💰💰")
            if guess % 2 == 0:
                print("You Win some more! 💰💰💰")
            else:
                print("House always wins! 💣💣💣 (you went KABOOM)")
            return True
        if guess == (SECRET_NUMBER - 0):
            print("House wins! 💣💣💣 (you went KABOOM)")
            return False
        print("No mines here (phew) - but if your debugger is here, you need a hobby!")

def play():
    """The game starts here!"""
    print("Welcome to the Debugging Game!")
    print("Your mission is to find the treasure without hitting a mine.")

    print(
        "For example, if you set a breakpoint here, that's no good. Because, I am a mine! 💣 HAHA!"
    )
    print(
        "On the other hand, if you set a breakpoint here, that's good! Because, I am treasure! 💰"
    )

    print("See, it's pretty easy")

    print("Here's some more treasure: 💰💰💰")
    print("You better step over this function though:")
    here_be_mines()
    print("But this one is pretty cruisy, so step inside:")
    easy_loot()
    print(
        "If you want to skip swaths of code, you can set breakpoints after and then continue execution."
    )
    print(
        "For example, there is a bunch of mines here, and the only way to get past them "
        "is to set a breakpoint beyond this area and continue till..."
    )

    for _ in range(12):
        print("Boom!! 💣💣💣")
    else:
        print("Treasure! 💰💰💰")

    print("Now that you get it, here is something a bit more challenging:")

    bonus = a_mystery_wrapped_in_an_enigma()
    print("Your bonus is:", bonus)

    print("We are almost at the finish. How about a game of roulette?")

    for _ in range(5):
        print("Spin the wheel! 🎰🎰🎰")
        safe_journey = treasure_roulette()
        assert safe_journey, "KABOOM! 💣💣💣"

    print("If you got here, you are a debugging master! 🎉")
    print("More treasure for you: 💰💰💰")


def main():
    """Run the game."""
    play()


if __name__ == "__main__":
    main()
