import time
coord = []
for i in range(6):
      f = open("snakecoordinates/"+str(i)+".txt","r")
      coord.append(f.read())
      f.close()
while 1:
      time.sleep(5)
      for i in range(6):
           f = open("snakecoordinates/"+str(i)+".txt","r")
           new = f.read()
           f.close()
           if new==coord[i] and new!="client|0,0;|0,0,0,0,0":
                 f = open("snakecoordinates/"+str(i)+".txt","w")
                 f.write("client|0,0;|0,0,0,0,0")
                 f.close()
                 print("cleaned folder",i)
           else:
                coord[i] = new
