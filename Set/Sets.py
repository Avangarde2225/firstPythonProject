farm_animals = {"sheep", "cow" , "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

wild_animals = set(["lion", "tiger", "panter", "elephant"])
print(wild_animals)


print("=" * 40)

even = set(range(0,40,2))
print(even)
print(len(even))

squares_tuple=(4,6,9,16,25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

print(even.union(squares))
print(len(even.union(squares)))

print("=" * 40)

print(even.intersection(squares))
print(even & squares)

print(squares.intersection(even))
print(squares & even)


print("=" * 40)

even = set(range(0,40,2))
print(sorted(even))
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares)))
print(len(sorted(even.difference(squares))))
print(sorted(even-squares))

print("squares minus even")
print(squares.difference(even))
print(squares - even)


print("=" * 40)

squares.discard(4)
squares.remove(16)
squares.discard(8)
print(squares)
if 8 in squares:
    squares.remove(8)


