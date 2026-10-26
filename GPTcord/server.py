## These where the test run as they will only work locally on one device

import socket
from cryptography.fernet import Fernet


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0", 4412))

server.listen()

client, addr = server.accept()

done = False
done1=False
i=2
j=2
while not done:
    if i % 2 == 0:
        msg = client.recv(1024)
        i=i+1
    else:
        if j%2==0:
            j=j+1
            key= client.recv(1024)
            cipher=Fernet(key)
            decrypted_msg=cipher.decrypt(msg)
            print(decrypted_msg.decode('utf-8'))
            non_encrypted_msg=(input("Input message: ").encode("utf-8"))
            key=Fernet.generate_key()
            cipher=Fernet(key)
            encrypted_msg=cipher.encrypt(non_encrypted_msg)
            client.send(encrypted_msg)
            print(non_encrypted_msg)
        else:
            j=j+1
            i=i+1
            client.send((key))


client.close()
server.close()

