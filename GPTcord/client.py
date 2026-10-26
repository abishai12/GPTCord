## These where the test run as they will only work locally on one device

import socket
from cryptography.fernet import Fernet


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("10.152.181.17", 4412)) #need public ip of server 

def main():
    done = False
    i=2 # Set i to 2 to iterate the first if statement
    j=2

    while not done:
    
        if i % 2==0: # Runs basically a clock of the if statement first, then else statement in a loop
            i=i+1
            non_encrypted_msg=(input("Input message: ").encode("utf-8"))
            key=Fernet.generate_key()
            cipher=Fernet(key)
            encrypted_msg=cipher.encrypt(non_encrypted_msg)
            client.send(encrypted_msg)
            print(non_encrypted_msg)
        else:
            if j%2==0:
                j=j+1
                client.send((key))
                msg = client.recv(1024)
            else:
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
            

    client.close()

    # I can't believe we found a way to encrypt messages