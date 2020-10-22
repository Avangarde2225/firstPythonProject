data = [4, 5, 104, 110, 120, 130, 150, 140, 180, 160, 170, 190, 240, 250, 340, 450]

min_val = 100
max_val = 300

for index, value in enumerate(data):
    if(value<min_val) or (value>max_val):
        del data[index]

print(data)

# reverse method
print("Reverse Method")

top_index = len(data)-1
for index, value in enumerate(reversed(data)):
    if value < min_val or value > max_val:
        print(top_index - index, value)
        del data[top_index - index]

print(data)
