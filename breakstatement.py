shopping_list = ["milk", "pasta", "Tidy", "spam", "vegatables", "soda"]

item_to_find = "alba"

found_at = None
#one way
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

#another way
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))

