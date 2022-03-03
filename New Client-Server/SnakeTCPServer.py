import socket

time1 = ''

server_port = 12001
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
welcome_socket.bind(('',server_port))

c1add = ('0.0.0.0',13000)
c2add = ('0.0.0.0',14000)

msg1 = ""
msg2 = ""

while 1:
    
    cmsg, cadd = welcome_socket.recvfrom(2048)  	
    cmsg = cmsg.decode()
    if cadd[1]==13000:
        msg1 = cmsg
        welcome_socket.sendto(msg1.encode(), c2add)
    else:
        msg2 = cmsg
        welcome_socket.sendto(msg2.encode(), c1add)
    
    
    msg = cmsg
    array=[]
    temparray = msg.split(";")
    
    for i in range(len(temparray)):
        if len(temparray[i])>2:
            array.append([temparray[i].split(",")[0],temparray[i].split(",")[1]])
    otherplayer=[array]
