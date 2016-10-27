import socket
s=socket.socket()
addr=("127.0.0.1",4500)
s.connect(addr)
getmsg= s.recv(4068)
print getmsg
msg=raw_input()
s.send(msg)
while msg[0]!="4":
    if msg[0]=="1":
        print s.recv(4068)
    elif msg[0]=="2":
        print s.recv(4068)
    
        
    
    msg=raw_input()
    s.send(msg)
print s.recv(4068)
s.close()
