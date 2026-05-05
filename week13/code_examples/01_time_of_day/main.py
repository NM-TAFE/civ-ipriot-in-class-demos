from datetime import datetime
from time_of_day import humanise

running = True

while running:
    user_input = input("Hello! What's your name? ")
    if user_input.lower() in ["q", "quit", "exit", "e"]:
        print("Bye!")
        running = False
    elif user_input.lower() in ["what", "why", "how", "???"]:
        print("Reasons! Go with it!")
    else:
        now = datetime.now()
        print(f"Good {humanise(now)}, {user_input}!")