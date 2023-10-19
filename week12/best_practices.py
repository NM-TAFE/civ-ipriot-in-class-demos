import random
# MUST fix file/open close
with open("target_words.txt") as target_words: # with -> context manager
    target_content = target_words.read().split()

target_word = random.choice(target_content)

# do the same for valid_words

# MUST constants in ALL_CAPS

# OPTIONAL: use functions instead of one big exec function..

for _ in range(20):
    pass
print("x")


