from store import Store
from product import Product

store = Store()
store.name = "Moongst Store PTY LTD"
store.add_department("Produce")
store.add_department("Homewares")
store.add_department("Books")


print(store.departments)

# class Team:
#     def __init__(self):
#         self.name = "Sick Sharks"
#         self.sport = "Sport"
#         self.players = []

#     def add_player(self, player):
#         self.players.append(player)


# class Player:
#     def __init__(self):
#         self.name = ""
#         self.position = ""

# t = Team()
# p1 = Player()
# p2 = Player()
# t.add_player(p1)
# t.add_player(p2)