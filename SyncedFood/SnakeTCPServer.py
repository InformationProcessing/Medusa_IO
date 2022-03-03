import socket
import random

time1 = ''

server_port = 12001
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
welcome_socket.bind(('',server_port))

c1add = ('localhost',13000)
c2add = ('localhost',14000)

msg1 = ""
msg2 = ""

power_upXCOORD = random.randint(1,1000)
power_upYCOORD = random.randint(1,1000)
power_upID = random.randint(0,3)


while 1:
    power_upMSG = str(power_upID)+';'+ str(power_upXCOORD)+';'+str(power_upYCOORD)
    welcome_socket.sendto(power_upMSG.encode(), c1add)
    welcome_socket.sendto(power_upMSG.encode(), c2add)
    
    cmsg, cadd = welcome_socket.recvfrom(2048)  	
    cmsg = cmsg.decode()
    
    if cadd[1]==13000:
        msg1 = cmsg + '|' + power_upMSG
        welcome_socket.sendto(msg1.encode(), c2add)
        
    else:
        msg2 = cmsg + '|' + power_upMSG
        welcome_socket.sendto(msg2.encode(), c1add)
    
    
    # msg = cmsg
    # array=[]
    # temparray = msg.split(";")
    
    # for i in range(len(temparray)):
    #     if len(temparray[i])>2:
    #         array.append([temparray[i].split(",")[0],temparray[i].split(",")[1]])
    # otherplayer=[array]
    
    