from work import Work

print("This is a fresh work with no attributes set:")
fresh_work = Work()
fresh_work.is_valid()
print(str(fresh_work))
print("================================")
print(f"Valid?: {fresh_work.is_valid()}")
print("Errors:")
print(fresh_work.errors)
print("================================")

print("\n\n\n")

print("This is a work with some attributes set:")
incomplete_work = Work()
incomplete_work.title = "An excellent adventure"
incomplete_work.summary = ""
incomplete_work.is_valid()
print(str(incomplete_work))
print("================================")
print(f"Valid?: {incomplete_work.is_valid()}")
print("Errors:")
print(incomplete_work.errors)
print("================================")

print("\n\n\n")

print("This is a complete work:")
complete_work = Work()
complete_work.title = "Raven of Eternity"
complete_work.summary = "Look there's something happening in this story."
complete_work.authors = ["Ira", "Dale"]
complete_work.chapters = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."]
print(str(complete_work))
print("================================")
print(f"Valid?: {complete_work.is_valid()}")
print("Errors:")
print(complete_work.errors)
print("================================")
