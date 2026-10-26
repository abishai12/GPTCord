## These where the test run as they will only work locally on one device

import socket, threading
from _thread import start_new_thread
from cryptography.fernet import Fernet
lock=threading.Lock()

def handle_client(client):
    while True:
        msg=client.recv(1024)
        key=client.recv(1024)
        cipher=Fernet(key)
        decrypted_msg=cipher.decrypt(msg)
        client.send(decrypted_msg)
    client.close()

def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 4412))

    server.listen()
    while True:
        client, addr = server.accept()
        lock.acquire
        start_new_thread(handle_client, (client,))
        done = False
        done1=False
        i=2
        j=2

if __name__=="__main__":
    main()

# while not done:
#     lock.acquire()
#     start_new_thread(handle)
#     if i % 2 == 0:
#         msg = client.recv(1024)
#         if not msg:
#             lock.release()
#             break
#         client.send(msg[::-1])
#         i=i+1
    # else:
    #     if j%2==0:
    #         j=j+1
    #         key= client.recv(1024)
    #         cipher=Fernet(key)
    #         decrypted_msg=cipher.decrypt(msg)
    #         print(decrypted_msg.decode('utf-8'))
        #     non_encrypted_msg=(input("Input message: ").encode("utf-8"))
        #     key=Fernet.generate_key()
        #     cipher=Fernet(key)
        #     encrypted_msg=cipher.encrypt(non_encrypted_msg)
        #     client.send(encrypted_msg)
        #     print(non_encrypted_msg)
        # else:
        #     j=j+1
        #     i=i+1
        #     client.send((key))


# client.close()
server.close()

