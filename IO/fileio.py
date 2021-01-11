# jabber = open("/Users/suler/Downloads/sample.txt", "r")
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end=" ")
#
# jabber.close()

# with open("/Users/suler/Downloads/sample.txt", "r") as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end="")

# Converting lines to the list
# with open("/Users/suler/Downloads/sample.txt", "r") as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end="")


with open("/Users/suler/Downloads/sample.txt", "r") as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end="")

with open("/Users/suler/Downloads/sample.txt", "r") as jabber:
    lines = jabber.read()
print(lines)

for line in lines[::-1]:
    print(line, end="")