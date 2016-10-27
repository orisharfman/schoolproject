import socket
import time
import os
s=socket.socket()
addr=("127.0.0.1",4500)
s.bind(addr)
s.listen(3)
s1=s.accept()[0]
s1.send(" 1.send messege\n 2.get list of files\n 3.downlowad file\n 4.quiet")
msg=s1.recv(4068)
while msg[0]!="4":
    if msg[0]=="1":
        s1.send(time.asctime())
    
    elif msg[0]=="2":
        os.chdir("c:\\")
        listt=os.listdir(os.getcwd())
        strr=""
        for i in listt:
            strr= strr+i+"\n"
        s1.send(strr)    
    
    elif msg[0]=="3":
        os.chdir("d:\\")
    msg=s1.recv(4068)

s1.send("goodbye")
s1.close()
s.close()


