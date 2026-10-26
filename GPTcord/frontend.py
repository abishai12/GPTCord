import customtkinter, tkinter, socket
from cryptography.fernet import Fernet
from client import main
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("192.168.0.18", 4412)) #need public ip of server 

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root=customtkinter.CTk()
root.geometry("500x300")

def send():
    print("test")
    msg_from_user=entry1.get()
    entry1.delete(0,len(msg_from_user))
    non_encrypted_msg=(msg_from_user.encode("utf-8"))
    key=Fernet.generate_key()
    cipher=Fernet(key)
    encrypted_msg=cipher.encrypt(non_encrypted_msg)
    client.send(encrypted_msg)
    print(non_encrypted_msg)
    client.send((key))


    msg_recieved = client.recv(1024)
    key= client.recv(1024)
    cipher=Fernet(key)
    decrypted_msg=cipher.decrypt(msg_recieved)
    print(decrypted_msg.decode('utf-8'))
    output_text_box.delete("0.0", "end")
    output_text_box.insert("0.0", decrypted_msg.decode('utf-8'))


def Password():
    print("test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=40, padx=60, fill="both", expand=True)



entry1=customtkinter.CTkEntry(master=frame, placeholder_text="Enter Message:")
entry1.pack(pady=20, padx=10)

button=customtkinter.CTkButton(master=frame, text="Send Message", command=send, fg_color="#592C82")
button.pack(pady=12, padx=10)

output_text_box=customtkinter.CTkTextbox(master=frame, width=200, height=100)
output_text_box.pack(pady=12, padx=10)



root.mainloop()
client.close()