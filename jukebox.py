
from Tuples.nested_data import albums

while True:
    print("Please choose your album(invalid choice exists):")
    for index,(title,artist,year, songs) in enumerate (albums):
        print("{}: {}, {}, {}, {}".format(index+1, title ,artist, year, songs))

    break