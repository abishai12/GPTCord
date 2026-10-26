## These where the test run as they will only work locally on one device

import socket
from cryptography.fernet import Fernet


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("192.168.0.18", 4412)) #need public ip of server 

done = False

while not done:
    client.send(input("Input message: ").encode("utf-8"))
    msg = client.recv(1024).decode("utf-8")
    if msg == "quit":
        done = True
    else:
      print (msg)

client.close()