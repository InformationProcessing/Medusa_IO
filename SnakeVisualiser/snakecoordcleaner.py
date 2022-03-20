import time

NUMBER_OF_CLIENTS = 6
coord = []
for i in range(NUMBER_OF_CLIENTS + 1):
    f = open("snakecoordinates/" + str(i) + ".txt", "r")
    coord.append(f.read())
    f.close()

for i in range(NUMBER_OF_CLIENTS + 1):
    f = open("snakecoordinates/" + str(i) + ".txt", "r")
    new = f.read()
    f.close()
    if new == coord[i] and new != "client|0,0;|0,0,0,0,0":
        f = open("snakecoordinates/" + str(i) + ".txt", "w")
        f.write("client|0,0;|0,0,0,0,0")
        f.close()
        print("cleaned folder", i)
    else:
        coord[i] = new
