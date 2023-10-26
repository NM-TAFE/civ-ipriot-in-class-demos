my_dict = {'a': 4, 'b':10, 'z': 5, 'c': 3}
# item_list = []
# for k, v in my_dict.items():
#     item_list.append((v, k))
#
# for v, k in sorted(item_list):
#     print('')

for v, k in sorted(
        [(v, k) for k, v in my_dict.items()], reverse=True):


