fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# ordered_keys = list(fruit.keys())
# print(ordered_keys)

ordered_keys = sorted(list(fruit.keys()))
for f in ordered_keys:
    print(f + " - " + fruit[f] )

